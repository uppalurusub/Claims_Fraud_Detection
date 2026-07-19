import type { ReactNode } from "react";
export default function KpiCard({ label, value, icon }: { label: string; value: string; icon: ReactNode }) {
  return <article className="kpi-card"><div className="kpi-icon">{icon}</div><div><span>{label}</span><strong>{value}</strong></div></article>;
}