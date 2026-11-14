import { Icon } from "@/shared/components/icon";
import { Button } from "@/shared/components/ui/button";

// Dados provisórios, até existir autenticação.
const mockUser = {
  initials: "AP",
  name: "Ana Paula",
  role: "Psicopedagoga",
};

export function SidebarUserCard() {
  return (
    <div className="bg-ink-100 flex items-center gap-3 rounded-xl p-3 group-data-[collapsible=icon]:justify-center group-data-[collapsible=icon]:bg-transparent group-data-[collapsible=icon]:p-0">
      <span
        aria-hidden="true"
        className="bg-sky-300 text-primary text-small flex size-(--sp-8) shrink-0 items-center justify-center rounded-full font-semibold"
      >
        {mockUser.initials}
      </span>
      <div className="flex min-w-0 flex-1 flex-col group-data-[collapsible=icon]:hidden">
        <span className="text-small text-primary truncate font-medium">{mockUser.name}</span>
        <span className="text-caption text-ink-700 truncate">{mockUser.role}</span>
      </div>
      <Button
        type="button"
        variant="ghost"
        size="icon"
        aria-label="Sair"
        className="text-ink-700 min-h-(--target-min) min-w-(--target-min) rounded-full group-data-[collapsible=icon]:hidden"
      >
        <Icon name="psif-sair" size="md" />
      </Button>
    </div>
  );
}
