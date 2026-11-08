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
      <AppSidebar />
      <SidebarInset>
        <AppHeader />
        <AppBreadcrumbs />
        {children}
      </SidebarInset>
    </SidebarProvider>
  );
}
