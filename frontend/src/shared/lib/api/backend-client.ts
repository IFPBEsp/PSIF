import "server-only";

import { mapApiError } from "./api-error";

const DEFAULT_TIMEOUT_MS = 10_000;

type BackendRequestOptions = RequestInit & {
  timeoutMs?: number;
};

export async function backendFetch<T>(
  path: string,
  options: BackendRequestOptions = {},
): Promise<T> {
  const { timeoutMs = DEFAULT_TIMEOUT_MS, signal, headers, ...init } = options;
  const url = buildUrl(path);
  const requestHeaders = buildHeaders(headers, init.body);
  const timeoutSignal = AbortSignal.timeout(timeoutMs);
  const requestSignal = signal ? AbortSignal.any([signal, timeoutSignal]) : timeoutSignal;

  let response: Response;
  let body: unknown;

  try {
    response = await fetch(url, {
      ...init,
      headers: requestHeaders,
      signal: requestSignal,
    });
    body = await readBody(response);
  } catch (error) {
    throw mapTimeoutError(error);
  }

  if (!response.ok) {
    throw mapApiError(body, response.status);
  }

  return body as T;
}

function buildUrl(path: string): string {
  const baseUrl = process.env.API_INTERNAL_URL;

  if (!baseUrl) {
    throw new Error("API_INTERNAL_URL não está configurada.");
  }

  return `${baseUrl.replace(/\/+$/, "")}/${path.replace(/^\/+/, "")}`;
}

function buildHeaders(
  headers: HeadersInit | undefined,
  body: BodyInit | null | undefined,
): Headers {
  const requestHeaders = new Headers(headers);

  if (!requestHeaders.has("Accept")) {
    requestHeaders.set("Accept", "application/json, application/problem+json");
  }

  if (typeof body === "string" && !requestHeaders.has("Content-Type")) {
    requestHeaders.set("Content-Type", "application/json");
  }

  return requestHeaders;
}

async function readBody(response: Response): Promise<unknown> {
  const text = await response.text();

  if (text.length === 0) {
    return undefined;
  }

  try {
    return JSON.parse(text);
  } catch {
    return text;
  }
}

function mapTimeoutError(error: unknown): unknown {
  if (!isTimeoutError(error)) {
    return error;
  }

  return mapApiError(
    {
      type: "about:blank",
      title: "Tempo esgotado",
      status: 504,
      detail: "O backend não respondeu dentro do tempo limite.",
    },
    504,
  );
}

function isTimeoutError(error: unknown): boolean {
  return error instanceof DOMException && error.name === "TimeoutError";
}
