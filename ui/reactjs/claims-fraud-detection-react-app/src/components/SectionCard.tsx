import type { ReactNode } from "react";
export default function SectionCard({ title, children }: { title: string; children: ReactNode }) {
  return <section className="section-card"><h2>{title}</h2>{children}</section>;
}