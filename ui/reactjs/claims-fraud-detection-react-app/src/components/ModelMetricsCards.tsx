import { Activity, Crosshair, Gauge, Radar } from "lucide-react";
const pct = (v: unknown) => typeof v === "number" ? `${(v * 100).toFixed(2)}%` : "—";
export default function ModelMetricsCards({ data }: { data: unknown }) {
  const d = (data ?? {}) as Record<string, unknown>;
  const cards = [
    ["Accuracy", d.accuracy, <Gauge/>], ["Precision", d.precision, <Crosshair/>],
    ["Recall", d.recall, <Radar/>], ["F1 Score", d.f1_score, <Activity/>], ["ROC AUC", d.roc_auc, <Activity/>]
  ] as const;
  const matrix = Array.isArray(d.confusion_matrix) ? d.confusion_matrix as number[][] : [];
  return <div>
    <div className="model-metrics">{cards.map(([label,value,icon]) => <div className="model-card" key={label}>{icon}<span>{label}</span><strong>{pct(value)}</strong><div className="progress"><i style={{width: pct(value)}}/></div></div>)}</div>
    {matrix.length >= 2 && <div className="matrix-wrap"><h3>Confusion Matrix</h3><div className="matrix">
      <div><span>True Negative</span><strong>{matrix[0]?.[0] ?? "—"}</strong></div><div><span>False Positive</span><strong>{matrix[0]?.[1] ?? "—"}</strong></div>
      <div><span>False Negative</span><strong>{matrix[1]?.[0] ?? "—"}</strong></div><div><span>True Positive</span><strong>{matrix[1]?.[1] ?? "—"}</strong></div>
    </div></div>}
  </div>;
}