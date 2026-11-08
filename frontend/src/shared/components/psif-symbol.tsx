import { psifSymbolMarkup } from "@/shared/components/svg-assets.generated";
import { cn } from "@/shared/lib/cn";

type PsifSymbolProps = Readonly<{
  decorative?: boolean;
  className?: string;
}>;

export function PsifSymbol({ decorative = false, className }: PsifSymbolProps) {
  return (
    <svg
      viewBox="0 0 512 512"
      className={cn("size-(--ic-xl) shrink-0", className)}
      {...(decorative
        ? { "aria-hidden": true, focusable: false }
        : { role: "img", "aria-label": "PSIF" })}
      dangerouslySetInnerHTML={{ __html: psifSymbolMarkup }}
    />
  );
}
