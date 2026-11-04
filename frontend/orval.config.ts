import { defineConfig } from "orval";

const DEV_BACKEND_URL = "http://localhost:8080";
const OPENAPI_PATH = "/v3/api-docs";

const backendUrl = process.env.API_INTERNAL_URL ?? DEV_BACKEND_URL;

export default defineConfig({
  psif: {
    input: {
      target: `${backendUrl}${OPENAPI_PATH}`,
    },
    output: {
      target: "src/generated/api/psif.ts",
      schemas: "src/generated/api/schemas",
      mode: "tags-split",
      client: "fetch",
      clean: true,
      indexFiles: true,
    },
  },
});
