import type { SVGProps } from "react";

import { cn } from "@/shared/lib/cn";

export const iconNames = [
  "psif-voltar",
  "psif-avancar",
  "psif-anterior",
  "psif-abrir-lista",
  "psif-fechar",
  "psif-menu",
  "psif-mais",
  "psif-inicio",
  "psif-inicio-ativo",
  "psif-atendimentos",
  "psif-atendimentos-ativo",
  "psif-alunos",
  "psif-alunos-ativo",
  "psif-relatorios",
  "psif-relatorios-ativo",
  "psif-calendario",
  "psif-perfil",
  "psif-notificacoes",
  "psif-termo",
  "psif-sair",
  "psif-alerta",
  "psif-sucesso",
  "psif-busca",
  "psif-email",
  "psif-cadeado",
  "psif-mostrar-senha",
] as const;

export type IconName = (typeof iconNames)[number];

const sizeClasses = {
  sm: "size-(--ic-sm)",
  md: "size-(--ic-md)",
  lg: "size-(--ic-lg)",
  xl: "size-(--ic-xl)",
} as const;

type IconProps = Omit<SVGProps<SVGSVGElement>, "name" | "children"> & {
  name: IconName;
  size?: keyof typeof sizeClasses;
};

export function Icon({ name, size = "md", className, ...props }: IconProps) {
  return (
    <svg
      aria-hidden="true"
      focusable="false"
      className={cn("shrink-0", sizeClasses[size], className)}
      {...props}
    >
      <use href={`#${name}`} />
    </svg>
  );
}
