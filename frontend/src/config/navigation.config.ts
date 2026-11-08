import { CalendarDays, GraduationCap, House, Users, type LucideIcon } from "lucide-react";

export type NavigationItem = {
  label: string;
  href: string;
  icon: LucideIcon;
};

export const navigationItems: readonly NavigationItem[] = [
  { label: "Início", href: "/", icon: House },
  { label: "Alunos", href: "/students", icon: GraduationCap },
  { label: "Agenda", href: "/schedule", icon: CalendarDays },
  { label: "Usuários", href: "/users", icon: Users },
];

export const segmentLabels: ReadonlyMap<string, string> = new Map([
  ["new", "Novo"],
  ["edit", "Editar"],
]);

export const dynamicSegmentLabel = "Detalhes";
