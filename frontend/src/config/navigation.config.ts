import type { IconName } from "@/shared/components/icon";

export type NavigationItem = {
  label: string;
  href: string;
  icon: IconName;
  activeIcon?: IconName;
};

export const navigationGroups: readonly (readonly NavigationItem[])[] = [
  [
    {
      label: "Início",
      href: "/",
      icon: "psif-inicio",
      activeIcon: "psif-inicio-ativo",
    },
    {
      label: "Atendimentos",
      href: "/appointments",
      icon: "psif-atendimentos",
      activeIcon: "psif-atendimentos-ativo",
    },
    {
      label: "Alunos",
      href: "/students",
      icon: "psif-alunos",
      activeIcon: "psif-alunos-ativo",
    },
    {
      label: "Relatórios",
      href: "/reports",
      icon: "psif-relatorios",
      activeIcon: "psif-relatorios-ativo",
    },
    { label: "Agenda", href: "/schedule", icon: "psif-calendario" },
  ],
  [
    {
      label: "Notificações",
      href: "/notifications",
      icon: "psif-notificacoes",
    },
    { label: "Meu perfil", href: "/profile", icon: "psif-perfil" },
  ],
];

export const navigationItems: readonly NavigationItem[] =
  navigationGroups.flat();

export const segmentLabels: ReadonlyMap<string, string> = new Map([
  ["new", "Novo"],
  ["edit", "Editar"],
]);

export const dynamicSegmentLabel = "Detalhes";
