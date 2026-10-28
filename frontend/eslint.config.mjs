import { defineConfig, globalIgnores } from "eslint/config";
import importPlugin from "eslint-plugin-import";
import nextCoreWebVitals from "eslint-config-next/core-web-vitals";
import nextTypeScript from "eslint-config-next/typescript";
import prettier from "eslint-config-prettier/flat";

export default defineConfig([
  ...nextCoreWebVitals,
  ...nextTypeScript,
  {
    plugins: {
      import: importPlugin,
    },
    rules: {
      "import/order": [
        "error",
        {
          "newlines-between": "always",
          groups: ["builtin", "external", "internal", ["parent", "sibling", "index"]],
          pathGroups: [
            {
              pattern: "@/**",
              group: "internal",
              position: "after",
            },
          ],
          pathGroupsExcludedImportTypes: ["builtin"],
        },
      ],
      "no-restricted-imports": ["error", { patterns: ["../*"] }],
    },
  },
  prettier,
  globalIgnores([".next/**", "node_modules/**", "out/**"]),
]);
