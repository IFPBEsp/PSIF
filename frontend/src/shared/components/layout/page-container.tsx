import type { ReactNode } from "react";

import { cn } from "@/shared/lib/cn";

type PageContainerProps = Readonly<{
  children: ReactNode;
  className?: string;
}>;

export function PageContainer({ children, className }: PageContainerProps) {
  return (
    <div
      className={cn("mx-auto flex w-full max-w-6xl flex-1 flex-col gap-6 p-4 md:p-6", className)}
    >
      {children}
    </div>
  );
}
