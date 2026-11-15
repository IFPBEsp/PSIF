import { PageContainer } from "@/shared/components/layout/page-container";
import { PageHeader } from "@/shared/components/layout/page-header";
import { ThemeSelector } from "@/shared/components/theme-selector";

export default function ProfilePage() {
  return (
    <PageContainer>
      <PageHeader title="Meu perfil" description="Ajuste como o PSIF aparece para você." />
      <section
        aria-labelledby="aparencia"
        className="bg-card flex flex-col gap-4 rounded-xl p-4 md:rounded-2xl"
      >
        <h2 id="aparencia" className="text-body text-primary font-semibold">
          Aparência
        </h2>
        <ThemeSelector />
      </section>
    </PageContainer>
  );
}
