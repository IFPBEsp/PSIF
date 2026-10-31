import { Inbox, type LucideIcon } from "lucide-react";
import type { ReactNode } from "react";

import { cn } from "@/shared/lib/cn";

type EmptyStateProps = Readonly<{
  title: string;
  description?: string;
  icon?: LucideIcon;
  action?: ReactNode;
  headingLevel?: 1 | 2;
  className?: string;
}>;

export function EmptyState({
  title,
  description,
  icon: Icon = Inbox,
  action,
  headingLevel = 2,
  className,
}: EmptyStateProps) {
  const Heading = headingLevel === 1 ? "h1" : "h2";

  return (
    <div
      className={cn(
        "flex flex-col items-center justify-center gap-4 rounded-lg border border-dashed p-8 text-center",
        className,
      )}
    >
      <Icon aria-hidden="true" className="text-muted-foreground size-10" />
      <div className="flex flex-col gap-1">
        <Heading className="text-lg font-semibold">{title}</Heading>
        {description ? (
          <p className="text-muted-foreground max-w-md text-sm">{description}</p>
        ) : null}
      </div>
      {action ? <div className="flex items-center gap-2">{action}</div> : null}
    </div>
  );
}
