import type { ReactNode } from "react";

import { Icon, type IconName } from "@/shared/components/icon";
import { cn } from "@/shared/lib/cn";

type EmptyStateProps = Readonly<{
  title: string;
  description?: string;
  icon?: IconName;
  action?: ReactNode;
  headingLevel?: 1 | 2;
  className?: string;
}>;

export function EmptyState({
  title,
  description,
  icon,
  action,
  headingLevel = 2,
  className,
}: EmptyStateProps) {
  const Heading = headingLevel === 1 ? "h1" : "h2";

  return (
    <div
      className={cn(
        "bg-card flex flex-col items-center justify-center gap-4 rounded-xl p-8 text-center md:rounded-2xl",
        className,
      )}
    >
      {icon ? (
        <span className="text-primary flex size-(--tile-icon-lg) items-center justify-center rounded-md bg-sky-100">
          <Icon name={icon} size="lg" />
        </span>
      ) : null}
      <div className="flex flex-col gap-1">
        <Heading className="text-h2 text-primary font-semibold">{title}</Heading>
        {description ? (
          <p className="text-body text-ink-700 max-w-(--w-form)">{description}</p>
        ) : null}
      </div>
      {action ? <div className="flex items-center gap-2">{action}</div> : null}
    </div>
  );
}
