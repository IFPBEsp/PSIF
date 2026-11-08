export type ApiError = {
  type: string;
  title: string;
  status: number;
  detail: string;
  fields?: Record<string, string>;
};

export type ProblemDetail = {
  type?: string;
  title?: string;
  status?: number;
  detail?: string;
  instance?: string;
  fields?: Record<string, string>;
};

const DEFAULT_TYPE = "about:blank";
const DEFAULT_STATUS = 500;
const DEFAULT_TITLE = "Erro inesperado";
const DEFAULT_DETAIL = "Não foi possível concluir a operação.";

export function mapApiError(problem: unknown, status?: number): ApiError {
  const source = isRecord(problem) ? problem : {};

  return {
    type: resolveText(source.type, DEFAULT_TYPE),
    title: resolveText(source.title, DEFAULT_TITLE),
    status: resolveStatus(source.status, status),
    detail: resolveText(source.detail, DEFAULT_DETAIL),
    ...(isFieldMap(source.fields) ? { fields: source.fields } : {}),
  };
}

function resolveText(value: unknown, fallback: string): string {
  return typeof value === "string" && value.length > 0 ? value : fallback;
}

function resolveStatus(problemStatus: unknown, fallbackStatus?: number): number {
  if (isStatus(problemStatus)) {
    return problemStatus;
  }

  if (isStatus(fallbackStatus)) {
    return fallbackStatus;
  }

  return DEFAULT_STATUS;
}

function isStatus(value: unknown): value is number {
  return typeof value === "number" && Number.isInteger(value);
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null;
}

function isFieldMap(value: unknown): value is Record<string, string> {
  return isRecord(value) && Object.values(value).every((field) => typeof field === "string");
}
