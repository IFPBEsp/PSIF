"use client";

import { useEffect } from "react";

import { EmptyState } from "@/shared/components/empty-state";
import { PageContainer } from "@/shared/components/layout/page-container";
import { Button } from "@/shared/components/ui/button";

type AdminErrorProps = Readonly<{
  error: Error & { digest?: string };
  reset: () => void;
}>;

export default function AdminError({ error, reset }: AdminErrorProps) {
  useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <PageContainer>
      <EmptyState
        headingLevel={1}
        icon="psif-alerta"
        title="Não foi possível carregar a página"
        description="Tente de novo em instantes. Se o erro continuar, fale com a equipe do PSIF."
        action={<Button onClick={reset}>Tentar de novo</Button>}
      />
    </PageContainer>
  );
}
