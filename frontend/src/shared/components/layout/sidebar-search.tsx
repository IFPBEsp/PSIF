import { Icon } from "@/shared/components/icon";
import { Button } from "@/shared/components/ui/button";
import { Input } from "@/shared/components/ui/input";

export function SidebarSearch() {
  return (
    <div role="search" className="px-3 pb-2">
      <div className="relative group-data-[collapsible=icon]:hidden">
        <Icon
          name="psif-busca"
          size="md"
          className="text-ink-600 pointer-events-none absolute top-1/2 left-3 -translate-y-1/2"
        />
        <Input
          type="search"
          aria-label="Pesquisar aluno"
          placeholder="Pesquisar aluno"
          className="bg-ink-100 text-small h-(--target-min) rounded-lg border-0 pl-10 shadow-none"
        />
      </div>
      <Button
        type="button"
        variant="ghost"
        size="icon"
        aria-label="Pesquisar aluno"
        className="text-ink-900 mx-auto hidden min-h-(--target-min) min-w-(--target-min) rounded-full group-data-[collapsible=icon]:flex"
      >
        <Icon name="psif-busca" size="lg" />
      </Button>
    </div>
  );
}
