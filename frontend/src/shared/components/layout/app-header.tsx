import { AppBreadcrumbs } from "@/shared/components/layout/app-breadcrumbs";
import { ThemeToggle } from "@/shared/components/theme-toggle";
import { Separator } from "@/shared/components/ui/separator";
import { SidebarTrigger } from "@/shared/components/ui/sidebar";

export function AppHeader() {
  return (
    <header className="bg-background sticky top-0 z-10 flex h-14 shrink-0 items-center gap-2 border-b px-4">
      <SidebarTrigger aria-label="Abrir ou fechar menu" />
      <Separator orientation="vertical" className="h-4" />
      <AppBreadcrumbs />
      <div className="ml-auto">
        <ThemeToggle />
      </div>
    </header>
  );
}
