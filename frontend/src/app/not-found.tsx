import { NotFoundState } from "@/shared/components/not-found-state";

export default function NotFound() {
  return (
    <main className="flex min-h-screen items-center justify-center p-4">
      <NotFoundState className="w-full max-w-lg" />
    </main>
  );
}
