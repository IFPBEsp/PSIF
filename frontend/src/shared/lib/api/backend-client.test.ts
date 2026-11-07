import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import { backendFetch } from "./backend-client";

describe("backendFetch", () => {
  beforeEach(() => {
    vi.stubEnv("API_INTERNAL_URL", "http://backend:8080");
  });

  afterEach(() => {
    vi.unstubAllEnvs();
    vi.unstubAllGlobals();
  });

  it("builds the request from API_INTERNAL_URL", async () => {
    const fetchMock = vi.fn<typeof fetch>().mockResolvedValue(
      new Response(JSON.stringify({ ok: true }), {
        status: 200,
        headers: { "Content-Type": "application/json" },
      }),
    );
    vi.stubGlobal("fetch", fetchMock);

    const result = await backendFetch<{ ok: boolean }>("/products", {
      method: "POST",
      body: JSON.stringify({ name: "Mouse" }),
    });

    expect(result).toEqual({ ok: true });
    expect(fetchMock).toHaveBeenCalledTimes(1);

    const [url, init] = fetchMock.mock.calls[0];
    const headers = new Headers(init?.headers);

    expect(url).toBe("http://backend:8080/products");
    expect(init?.method).toBe("POST");
    expect(headers.get("Accept")).toContain("application/problem+json");
    expect(headers.get("Content-Type")).toBe("application/json");
  });

  it("does not force JSON content-type for FormData bodies", async () => {
    const fetchMock = vi.fn<typeof fetch>().mockResolvedValue(new Response(null, { status: 204 }));
    vi.stubGlobal("fetch", fetchMock);

    const formData = new FormData();
    formData.append("file", new Blob(["conteúdo"]), "arquivo.txt");

    await backendFetch("/uploads", { method: "POST", body: formData });

    const [, init] = fetchMock.mock.calls[0];
    const headers = new Headers(init?.headers);

    expect(headers.has("Content-Type")).toBe(false);
  });

  it("ignores NEXT_PUBLIC_API_URL", async () => {
    vi.stubEnv("NEXT_PUBLIC_API_URL", "http://public:9999");

    const fetchMock = vi.fn<typeof fetch>().mockResolvedValue(new Response(null, { status: 204 }));
    vi.stubGlobal("fetch", fetchMock);

    await backendFetch("/products");

    expect(fetchMock.mock.calls[0][0]).toBe("http://backend:8080/products");
  });

  it("throws an ApiError when the timeout elapses", async () => {
    const fetchMock = vi.fn<typeof fetch>((_input, init) => {
      return new Promise<Response>((_resolve, reject) => {
        init?.signal?.addEventListener("abort", () => reject(init.signal?.reason));
      });
    });
    vi.stubGlobal("fetch", fetchMock);

    await expect(backendFetch("/slow", { timeoutMs: 10 })).rejects.toMatchObject({
      type: "about:blank",
      title: "Tempo esgotado",
      status: 504,
    });
  });

  it("throws an ApiError when the timeout elapses while reading the body", async () => {
    const fetchMock = vi.fn<typeof fetch>((_input, init) => {
      const stream = new ReadableStream<Uint8Array>({
        start(controller) {
          init?.signal?.addEventListener("abort", () => controller.error(init.signal?.reason));
        },
      });

      return Promise.resolve(new Response(stream, { status: 200 }));
    });
    vi.stubGlobal("fetch", fetchMock);

    await expect(backendFetch("/slow-body", { timeoutMs: 10 })).rejects.toMatchObject({
      type: "about:blank",
      title: "Tempo esgotado",
      status: 504,
    });
  });

  it("maps ProblemDetail errors from failed responses", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn<typeof fetch>().mockResolvedValue(
        new Response(
          JSON.stringify({
            type: "about:blank",
            title: "Dados inválidos",
            status: 400,
            detail: "Verifique os campos informados.",
            fields: { email: "Email já cadastrado" },
          }),
          {
            status: 400,
            headers: { "Content-Type": "application/problem+json" },
          },
        ),
      ),
    );

    await expect(backendFetch("/products")).rejects.toMatchObject({
      type: "about:blank",
      title: "Dados inválidos",
      status: 400,
      fields: { email: "Email já cadastrado" },
    });
  });

  it("returns undefined for empty responses", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn<typeof fetch>().mockResolvedValue(new Response(null, { status: 204 })),
    );

    await expect(backendFetch("/products/1")).resolves.toBeUndefined();
  });

  it("throws when API_INTERNAL_URL is missing", async () => {
    vi.stubEnv("API_INTERNAL_URL", "");

    await expect(backendFetch("/products")).rejects.toThrow("API_INTERNAL_URL");
  });
});
