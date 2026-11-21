"use client";

import { Icon } from "@/shared/components/icon";
import { Button } from "@/shared/components/ui/button";
import { useSidebar } from "@/shared/components/ui/sidebar";

export function AppHeader() {
  const { openMobile, setOpenMobile } = useSidebar();

  return (
    <header className="flex items-center justify-end px-(--page-pad) pt-[max(var(--sp-4),env(safe-area-inset-top))] pb-2 md:hidden">
      <Button
        type="button"
        variant="ghost"
        size="icon"
        onClick={() => setOpenMobile(true)}
        aria-label="Abrir menu"
        aria-expanded={openMobile}
        className="text-ink-900 min-h-(--target-min) min-w-(--target-min) rounded-full"
      >
        <Icon name="psif-menu" size="lg" />
      </Button>
    </header>
  );
}
