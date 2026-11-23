import { describe, expect, it } from "vitest";

import { GET } from "./route";

describe("GET /api/health", () => {
  it("responds UP without calling the backend", async () => {
    const response = GET();

    expect(response.status).toBe(200);
    expect(await response.json()).toEqual({ status: "UP" });
  });
});
