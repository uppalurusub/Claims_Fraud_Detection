import type { AnalyticsData, UnknownRecord } from "../types/fraud";
const isRecord = (v: unknown): v is UnknownRecord => typeof v === "object" && v !== null && !Array.isArray(v);
export function toChartData(data: AnalyticsData) {
  const rows = Array.isArray(data) ? data.filter(isRecord) : [];
  if (!rows.length) return null;
  const keys = Object.keys(rows[0]);
  const labelKey = keys.find(k => typeof rows[0][k] === "string") ?? keys[0];
  const valueKey = keys.find(k => k !== labelKey && typeof rows[0][k] === "number");
  if (!valueKey) return null;
  return {
    labels: rows.map(r => String(r[labelKey] ?? "")),
    datasets: [{ label: valueKey.replace(/_/g, " "), data: rows.map(r => Number(r[valueKey] ?? 0)) }]
  };
}