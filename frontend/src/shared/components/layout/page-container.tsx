import type { ReactNode } from "react";

import { cn } from "@/shared/lib/cn";

type PageContainerProps = Readonly<{
  children: ReactNode;
  className?: string;
}>;

export function PageContainer({ children, className }: PageContainerProps) {
  return (
    <div
      className={cn(
        "mx-auto flex w-full max-w-(--w-content) flex-1 flex-col gap-6 px-(--page-pad) py-6 md:px-8",
        className,
      )}
    >
      {children}
    </div>
  );
}
