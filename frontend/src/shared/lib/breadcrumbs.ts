import { dynamicSegmentLabel, navigationItems, segmentLabels } from "@/config/navigation.config";

export type Breadcrumb = {
  label: string;
  href?: string;
};

const sections = navigationItems.filter((item) => item.href !== "/");

export function buildBreadcrumbs(pathname: string): Breadcrumb[] {
  const [first, ...rest] = pathname.split("/").filter(Boolean);
  const section = sections.find((item) => item.href === `/${first}`);

  if (!section) {
    return [];
  }

  const trail: Breadcrumb[] = [{ label: section.label, href: section.href }];
  let currentPath = section.href;

  for (const segment of rest) {
    currentPath += `/${segment}`;

    const label = segmentLabels.get(segment) ?? dynamicSegmentLabel;
    trail.push({ label, href: currentPath });
  }

  if (trail.length < 2) {
    return [];
  }

  return trail.map((crumb, index) => (index === trail.length - 1 ? { label: crumb.label } : crumb));
}
