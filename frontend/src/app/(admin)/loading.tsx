import { PageContainer } from "@/shared/components/layout/page-container";
import { Skeleton } from "@/shared/components/ui/skeleton";

export default function AdminLoading() {
  return (
    <PageContainer>
      <div role="status" aria-live="polite" className="flex flex-col gap-6">
        <span className="sr-only">Carregando…</span>
        <div className="flex flex-col gap-2">
          <Skeleton className="h-8 w-48" />
          <Skeleton className="h-4 w-72" />
        </div>
        <Skeleton className="h-64 w-full" />
      </div>
    </PageContainer>
  );
}
