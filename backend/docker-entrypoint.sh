#!/usr/bin/env bash

set -u

readonly postgres_host="postgres"
readonly postgres_port="5432"
readonly retry_interval=2
readonly timeout=60
readonly started_at=$SECONDS
probe_pid=""

cleanup_probe() {
  if [[ -n "${probe_pid}" ]] && kill -0 "${probe_pid}" 2>/dev/null; then
    kill "${probe_pid}" 2>/dev/null || true
    wait "${probe_pid}" 2>/dev/null || true
  fi
}

trap cleanup_probe EXIT

while true; do
  elapsed=$((SECONDS - started_at))
  remaining=$((timeout - elapsed))

  if ((remaining <= 0)); then
    echo "ERROR: PostgreSQL at ${postgres_host}:${postgres_port} was unavailable after ${timeout}s." >&2
    exit 1
  fi

  echo "Waiting for PostgreSQL at ${postgres_host}:${postgres_port} (elapsed: ${elapsed}s, remaining: ${remaining}s)..."
  (: >"/dev/tcp/${postgres_host}/${postgres_port}") 2>/dev/null &
  probe_pid=$!

  while kill -0 "${probe_pid}" 2>/dev/null; do
    if ((SECONDS - started_at >= timeout)); then
      echo "ERROR: PostgreSQL at ${postgres_host}:${postgres_port} was unavailable after ${timeout}s." >&2
      exit 1
    fi
    sleep 1
  done

  if wait "${probe_pid}"; then
    probe_pid=""
    echo "PostgreSQL is reachable after ${elapsed}s. Starting Spring Boot."
    exec ./mvnw spring-boot:run
  fi
  probe_pid=""

  remaining=$((timeout - (SECONDS - started_at)))
  ((remaining > 0)) || continue
  ((remaining < retry_interval)) && sleep "${remaining}" || sleep "${retry_interval}"
done
