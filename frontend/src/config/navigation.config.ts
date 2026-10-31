import { CalendarDays, GraduationCap, House, Users, type LucideIcon } from "lucide-react";

export type NavigationItem = {
  label: string;
  href: string;
  icon: LucideIcon;
};

export const navigationItems: readonly NavigationItem[] = [
  { label: "Início", href: "/", icon: House },
  { label: "Alunos", href: "/alunos", icon: GraduationCap },
  { label: "Agenda", href: "/agenda", icon: CalendarDays },
  { label: "Usuários", href: "/usuarios", icon: Users },
];
