import type { ReactNode } from "react";

type PageHeaderProps = Readonly<{
  title: string;
  description?: string;
  actions?: ReactNode;
}>;

export function PageHeader({ title, description, actions }: PageHeaderProps) {
  return (
    <div className="flex flex-col gap-4 md:flex-row md:items-start md:justify-between">
      <div className="flex flex-col gap-1">
        <h1 className="text-display text-primary font-semibold">{title}</h1>
        {description ? <p className="text-body text-ink-700">{description}</p> : null}
      </div>
      {actions ? <div className="flex shrink-0 items-center gap-2">{actions}</div> : null}
    </div>
  );
}
