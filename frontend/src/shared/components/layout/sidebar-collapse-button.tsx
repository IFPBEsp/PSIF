"use client";

import { Icon } from "@/shared/components/icon";
import { Button } from "@/shared/components/ui/button";
import { useSidebar } from "@/shared/components/ui/sidebar";
import { cn } from "@/shared/lib/cn";

type SidebarCollapseButtonProps = Readonly<{
  className?: string;
}>;

export function SidebarCollapseButton({ className }: SidebarCollapseButtonProps) {
  const { isMobile, state, toggleSidebar } = useSidebar();

  if (isMobile) {
    return null;
  }

  const expanded = state === "expanded";

  return (
    <Button
      type="button"
      variant="ghost"
      size="icon"
      onClick={toggleSidebar}
      aria-label={expanded ? "Recolher menu" : "Expandir menu"}
      aria-expanded={expanded}
      className={cn(
        "text-ink-900 min-h-(--target-min) min-w-(--target-min) rounded-full",
        className,
      )}
    >
      <Icon name="psif-menu" size="lg" />
    </Button>
  );
}
