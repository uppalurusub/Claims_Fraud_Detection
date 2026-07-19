import { CircleCheckBig, Siren } from "lucide-react";
import { formatNumber } from "../utils/formatters";
export default function AnomalyCards({ data }: { data: unknown }) {
  const d = (data ?? {}) as Record<string, unknown>;
  return <div className="split-cards">
    <div className="status-card success"><CircleCheckBig/><span>Normal Claims</span><strong>{formatNumber(d.normal_claims)}</strong></div>
    <div className="status-card danger"><Siren/><span>Anomalies Detected</span><strong>{formatNumber(d.anomalies)}</strong></div>
  </div>;
}