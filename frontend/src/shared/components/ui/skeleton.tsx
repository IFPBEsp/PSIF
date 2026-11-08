import { cn } from "@/shared/lib/cn";

function Skeleton({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="skeleton"
      className={cn("animate-pulse rounded-md bg-ink-200", className)}
      {...props}
    />
  );
}

export { Skeleton };
