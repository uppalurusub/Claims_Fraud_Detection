import { titleCase } from "../utils/formatters";
const fmt = (v: unknown) => typeof v === "number" ? new Intl.NumberFormat("en-IN", { maximumFractionDigits: 4 }).format(v) : String(v ?? "—");
export default function MetricGrid({ data }: { data: unknown }) {
  if (!data || typeof data !== "object" || Array.isArray(data)) return null;
  const entries = Object.entries(data as Record<string, unknown>).filter(([,v]) => typeof v !== "object");
  return <div className="metric-grid">{entries.map(([k,v]) =>
    <div className="mini-metric" key={k}><span>{titleCase(k)}</span><strong>{fmt(v)}</strong></div>
  )}</div>;
}