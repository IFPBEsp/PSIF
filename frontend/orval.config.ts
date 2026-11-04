import { defineConfig } from "orval";

const DEV_BACKEND_URL = "http://localhost:8080";
const OPENAPI_PATH = "/v3/api-docs";

const backendUrl = process.env.API_INTERNAL_URL?.trim() || DEV_BACKEND_URL;

export default defineConfig({
  psif: {
    input: {
      target: new URL(OPENAPI_PATH, backendUrl).toString(),
    },
    output: {
      target: "src/generated/api",
      schemas: "src/generated/api/schemas",
      mode: "tags-split",
      client: "fetch",
      clean: true,
    },
  },
});
