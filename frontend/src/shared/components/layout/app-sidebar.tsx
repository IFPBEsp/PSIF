"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

import { navigationGroups } from "@/config/navigation.config";
import { Icon } from "@/shared/components/icon";
import { SidebarCollapseButton } from "@/shared/components/layout/sidebar-collapse-button";
import { PsifSymbol } from "@/shared/components/psif-symbol";
import { ThemeSelector } from "@/shared/components/theme-selector";
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupContent,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarSeparator,
} from "@/shared/components/ui/sidebar";

function isActive(pathname: string, href: string) {
  if (href === "/") {
    return pathname === "/";
  }

  return pathname === href || pathname.startsWith(`${href}/`);
}

export function AppSidebar() {
  const pathname = usePathname();

  return (
    <Sidebar collapsible="icon">
      <SidebarHeader className="p-6 group-data-[collapsible=icon]:p-2">
        <div className="flex items-center gap-3 group-data-[collapsible=icon]:flex-col">
          <PsifSymbol decorative />
          <span className="text-h1 text-primary font-semibold group-data-[collapsible=icon]:hidden">
            PSIF
          </span>
          <SidebarCollapseButton className="ml-auto group-data-[collapsible=icon]:ml-0" />
        </div>
      </SidebarHeader>
      <SidebarContent>
        <nav aria-label="Principal">
          {navigationGroups.map((group, index) => (
            <div key={group[0]?.href}>
              {index > 0 ? <SidebarSeparator className="w-auto!" /> : null}
              <SidebarGroup>
                <SidebarGroupContent>
                  <SidebarMenu>
                    {group.map((item) => {
                      const active = isActive(pathname, item.href);

                      return (
                        <SidebarMenuItem key={item.href}>
                          <SidebarMenuButton
                            asChild
                            isActive={active}
                            tooltip={item.label}
                            className="text-body text-ink-700 data-[active=true]:bg-sky-100 data-[active=true]:text-primary h-auto min-h-(--target-min) rounded-lg font-medium data-[active=true]:font-semibold"
                          >
                            <Link href={item.href} aria-current={active ? "page" : undefined}>
                              <Icon
                                name={active && item.activeIcon ? item.activeIcon : item.icon}
                                size="lg"
                                className="size-(--ic-lg)!"
                              />
                              <span>{item.label}</span>
                            </Link>
                          </SidebarMenuButton>
                        </SidebarMenuItem>
                      );
                    })}
                  </SidebarMenu>
                </SidebarGroupContent>
              </SidebarGroup>
            </div>
          ))}
        </nav>
      </SidebarContent>
      <SidebarFooter className="p-6 group-data-[collapsible=icon]:hidden">
        <ThemeSelector />
      </SidebarFooter>
    </Sidebar>
  );
}
