import { BadgeDollarSign, FileText, ShieldAlert, TriangleAlert, Lightbulb, BriefcaseBusiness } from "lucide-react";
import { formatCurrency, formatNumber, formatPercent } from "../utils/formatters";
export default function ExecutiveSummary({ data }: { data: unknown }) {
 const d=(data??{}) as Record<string,unknown>;
 return <div className="executive">
  <div className="summary-stats">
   <div><FileText/><span>Total Claims</span><strong>{formatNumber(d.total_claims)}</strong></div>
   <div><ShieldAlert/><span>Fraud Claims</span><strong>{formatNumber(d.fraud_claims)}</strong></div>
   <div><TriangleAlert/><span>Fraud Rate</span><strong>{formatPercent(d.fraud_rate)}</strong></div>
   <div><BadgeDollarSign/><span>Fraud Amount</span><strong>{formatCurrency(d.fraud_amount)}</strong></div>
  </div>
  <div className="summary-message finding"><Lightbulb/><div><span>Key Finding</span><p>{String(d.key_finding ?? "—")}</p></div></div>
  <div className="summary-message action"><BriefcaseBusiness/><div><span>Business Action</span><p>{String(d.business_action ?? "—")}</p></div></div>
 </div>;
}