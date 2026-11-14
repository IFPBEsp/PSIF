"use client";

import { useTheme } from "next-themes";
import { useSyncExternalStore } from "react";

import { Button } from "@/shared/components/ui/button";

const options = [
  { value: "light", label: "Claro" },
  { value: "dark", label: "Escuro" },
  { value: "system", label: "Sistema" },
] as const;

const subscribe = () => () => {};

function useMounted() {
  return useSyncExternalStore(
    subscribe,
    () => true,
    () => false,
  );
}

export function ThemeSelector() {
  const { theme, setTheme } = useTheme();
  const mounted = useMounted();

  return (
    <div role="group" aria-label="Tema" className="flex flex-col gap-2">
      <span aria-hidden="true" className="text-caption text-primary font-semibold">
        Tema
      </span>
      <div className="flex flex-wrap gap-2">
        {options.map((option) => (
          <Button
            key={option.value}
            type="button"
            variant="ghost"
            aria-pressed={mounted && theme === option.value}
            onClick={() => setTheme(option.value)}
            className="text-small text-primary aria-pressed:bg-primary aria-pressed:text-primary-foreground aria-pressed:hover:bg-navy-800 min-h-(--target-min) rounded-full border border-(--line-on-sky) bg-transparent px-4 font-medium aria-pressed:font-semibold"
          >
            {option.label}
          </Button>
        ))}
      </div>
    </div>
  );
}
