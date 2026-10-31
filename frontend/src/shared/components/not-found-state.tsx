import { SearchX } from "lucide-react";
import Link from "next/link";

import { EmptyState } from "@/shared/components/empty-state";
import { Button } from "@/shared/components/ui/button";

type NotFoundStateProps = Readonly<{
  className?: string;
}>;

export function NotFoundState({ className }: NotFoundStateProps) {
  return (
    <EmptyState
      headingLevel={1}
      icon={SearchX}
      title="Página não encontrada"
      description="O endereço não existe ou foi removido. Confira o link ou volte ao início."
      action={
        <Button asChild>
          <Link href="/">Voltar ao início</Link>
        </Button>
      }
      className={className}
    />
  );
}
