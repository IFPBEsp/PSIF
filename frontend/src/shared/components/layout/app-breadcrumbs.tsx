"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { Fragment } from "react";

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/shared/components/ui/breadcrumb";
import { buildBreadcrumbs } from "@/shared/lib/breadcrumbs";

export function AppBreadcrumbs() {
  const pathname = usePathname();
  const items = buildBreadcrumbs(pathname);

  if (items.length === 0) {
    return null;
  }

  return (
    <div className="mx-auto hidden w-full max-w-6xl px-4 pt-6 md:block md:px-6">
      <Breadcrumb aria-label="Trilha">
        <BreadcrumbList className="text-small">
          {items.map((item, index) => (
            <Fragment key={`${index}-${item.label}`}>
              {index > 0 ? <BreadcrumbSeparator /> : null}
              <BreadcrumbItem>
                {item.href ? (
                  <BreadcrumbLink asChild>
                    <Link href={item.href}>{item.label}</Link>
                  </BreadcrumbLink>
                ) : (
                  <BreadcrumbPage>{item.label}</BreadcrumbPage>
                )}
              </BreadcrumbItem>
            </Fragment>
          ))}
        </BreadcrumbList>
      </Breadcrumb>
    </div>
  );
}
