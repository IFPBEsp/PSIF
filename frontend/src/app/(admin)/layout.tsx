import type { CSSProperties, ReactNode } from "react";

import { AppBreadcrumbs } from "@/shared/components/layout/app-breadcrumbs";
import { AppHeader } from "@/shared/components/layout/app-header";
import { AppSidebar } from "@/shared/components/layout/app-sidebar";
import { SidebarInset, SidebarProvider } from "@/shared/components/ui/sidebar";

type AdminLayoutProps = Readonly<{
  children: ReactNode;
}>;

export default function AdminLayout({ children }: AdminLayoutProps) {
  return (
    <SidebarProvider style={{ "--sidebar-width": "var(--w-sidebar)" } as CSSProperties}>
      <a
        href="#conteudo"
        className="text-small text-primary-foreground bg-primary sr-only rounded-lg px-4 py-3 focus:not-sr-only focus:fixed focus:top-4 focus:left-4 focus:z-(--z-modal)"
      >
        Pular para o conteúdo
      </a>
      <AppSidebar />
      <SidebarInset id="conteudo" tabIndex={-1}>
        <AppHeader />
        <AppBreadcrumbs />
        {children}
      </SidebarInset>
    </SidebarProvider>
  );
}
