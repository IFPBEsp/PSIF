"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

import { navigationGroups } from "@/config/navigation.config";
import { Icon } from "@/shared/components/icon";
import { SidebarCollapseButton } from "@/shared/components/layout/sidebar-collapse-button";
import { SidebarSearch } from "@/shared/components/layout/sidebar-search";
import { SidebarUserCard } from "@/shared/components/layout/sidebar-user-card";
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
  useSidebar,
} from "@/shared/components/ui/sidebar";

function isActive(pathname: string, href: string) {
  if (href === "/") {
    return pathname === "/";
  }

  return pathname === href || pathname.startsWith(`${href}/`);
}

export function AppSidebar() {
  const pathname = usePathname();
  const { setOpenMobile } = useSidebar();

  return (
    <Sidebar collapsible="icon" className="group-data-[side=left]:border-r-0">
      <SidebarHeader className="px-6 pt-6 pb-3 group-data-[collapsible=icon]:p-2">
        <div className="flex items-center justify-between group-data-[collapsible=icon]:justify-center">
          <span className="text-h1 text-primary font-semibold group-data-[collapsible=icon]:hidden">
            PSIF
          </span>
          <SidebarCollapseButton />
        </div>
      </SidebarHeader>
      <SidebarSearch />
      <SidebarContent>
        <nav aria-label="Principal">
          {navigationGroups.map((group, index) => (
            <div key={group[0]?.href}>
              {index > 0 ? <SidebarSeparator className="mx-6 w-auto!" /> : null}
              <SidebarGroup className="px-3 py-2">
                <SidebarGroupContent>
                  <SidebarMenu className="gap-0.5">
                    {group.map((item) => {
                      const active = isActive(pathname, item.href);

                      return (
                        <SidebarMenuItem key={item.href}>
                          <SidebarMenuButton
                            asChild
                            isActive={active}
                            tooltip={item.label}
                            className="text-body text-ink-700 hover:text-ink-700 data-[active=true]:bg-sky-100 data-[active=true]:text-primary data-[active=true]:hover:bg-sky-100 data-[active=true]:hover:text-primary h-auto min-h-(--target-min) gap-2.5 rounded-lg px-3 font-medium data-[active=true]:font-semibold"
                          >
                            <Link
                              href={item.href}
                              onClick={() => setOpenMobile(false)}
                              aria-current={active ? "page" : undefined}
                            >
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
      <SidebarFooter className="p-3">
        <SidebarUserCard />
      </SidebarFooter>
    </Sidebar>
  );
}
