import "server-only";

import { backendFetch } from "./backend-client";

type OrvalMutatorOptions = Parameters<typeof backendFetch>[1];

export function orvalMutator<T>(path: string, options?: OrvalMutatorOptions): Promise<T> {
  return backendFetch<T>(path, options);
}
