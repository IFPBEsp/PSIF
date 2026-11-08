import { describe, expect, it } from "vitest";

import { mapApiError } from "./api-error";

describe("mapApiError", () => {
  it("maps a complete ProblemDetail", () => {
    const error = mapApiError({
      type: "about:blank",
      title: "Recurso não encontrado",
      status: 404,
      detail: "O recurso solicitado não foi encontrado.",
      instance: "/products/1",
    });

    expect(error).toEqual({
      type: "about:blank",
      title: "Recurso não encontrado",
      status: 404,
      detail: "O recurso solicitado não foi encontrado.",
    });
  });

  it("keeps field errors from validation problems", () => {
    const error = mapApiError({
      type: "about:blank",
      title: "Dados inválidos",
      status: 400,
      detail: "Verifique os campos informados.",
      fields: {
        email: "Email já cadastrado",
        name: "Nome obrigatório",
      },
    });

    expect(error.fields).toEqual({
      email: "Email já cadastrado",
      name: "Nome obrigatório",
    });
  });

  it("uses the HTTP status when the body has none", () => {
    const error = mapApiError({ detail: "Serviço indisponível." }, 503);

    expect(error.status).toBe(503);
  });

  it("falls back when the problem is not an object", () => {
    const error = mapApiError("not a problem");

    expect(error).toEqual({
      type: "about:blank",
      title: "Erro inesperado",
      status: 500,
      detail: "Não foi possível concluir a operação.",
    });
  });

  it("ignores invalid field maps", () => {
    const error = mapApiError({ fields: { count: 1 } });

    expect(error.fields).toBeUndefined();
  });
});
