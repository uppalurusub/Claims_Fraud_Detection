import { Building2, Stethoscope, Lightbulb } from "lucide-react";
export default function RootCauseCards({ data }: { data: unknown }) {
  const d = (data ?? {}) as Record<string, unknown>;
  return <div className="root-cause">
    <div className="cause-row"><Building2/><div><span>Highest Fraud Provider</span><strong>Provider {String(d.highest_fraud_provider ?? "—")}</strong></div></div>
    <div className="cause-row"><Stethoscope/><div><span>Highest Fraud Procedure</span><strong>Procedure {String(d.highest_fraud_procedure ?? "—")}</strong></div></div>
    <div className="recommendation"><Lightbulb/><div><span>Recommended Action</span><p>{String(d.recommendation ?? "No recommendation available")}</p></div></div>
  </div>;
}