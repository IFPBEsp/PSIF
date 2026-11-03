import { dynamicSegmentLabel, navigationItems, segmentLabels } from "@/config/navigation.config";

export type Breadcrumb = {
  label: string;
  href?: string;
};

const home = navigationItems.find((item) => item.href === "/");
const sections = navigationItems.filter((item) => item.href !== "/");

export function buildBreadcrumbs(pathname: string): Breadcrumb[] {
  const trail: Breadcrumb[] = [{ label: home?.label ?? "Início", href: "/" }];
  let currentPath = "";
  let afterSection = false;

  for (const segment of pathname.split("/").filter(Boolean)) {
    currentPath += `/${segment}`;

    const section = sections.find((item) => item.href === currentPath);
    const label =
      section?.label ??
      segmentLabels.get(segment) ??
      (afterSection ? dynamicSegmentLabel : undefined);

    if (!label) {
      break;
    }

    trail.push({ label, href: currentPath });
    afterSection = section !== undefined;
  }

  return trail.map((crumb, index) => (index === trail.length - 1 ? { label: crumb.label } : crumb));
}
