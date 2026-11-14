import { afterEach, describe, expect, it, vi } from "vitest";

import { backendFetch } from "./backend-client";
import { orvalMutator } from "./orval-mutator";

vi.mock("./backend-client", () => ({
  backendFetch: vi.fn(),
}));

describe("orvalMutator", () => {
  afterEach(() => {
    vi.mocked(backendFetch).mockReset();
  });

  it("delegates the generated call to backendFetch", async () => {
    vi.mocked(backendFetch).mockResolvedValue({ id: 1 });
    const options = { method: "GET", headers: { "X-Trace": "1" } };

    const result = await orvalMutator<{ id: number }>("/alunos/1", options);

    expect(result).toEqual({ id: 1 });
    expect(backendFetch).toHaveBeenCalledWith("/alunos/1", options);
  });

  it("propagates backendFetch errors", async () => {
    const apiError = { status: 404, title: "Não encontrado" };
    vi.mocked(backendFetch).mockRejectedValue(apiError);

    await expect(orvalMutator("/alunos/9")).rejects.toBe(apiError);
  });
});
