import { iconSpriteMarkup } from "@/shared/components/svg-assets.generated";

export function IconSprite() {
  return (
    <svg
      aria-hidden="true"
      focusable="false"
      style={{ position: "absolute", width: 0, height: 0 }}
      dangerouslySetInnerHTML={{ __html: iconSpriteMarkup }}
    />
  );
}
