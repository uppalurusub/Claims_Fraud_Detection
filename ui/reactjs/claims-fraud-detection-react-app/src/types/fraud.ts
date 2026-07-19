export type UnknownRecord = Record<string, unknown>;
export interface FraudKpis {
  total_claims?: number;
  fraud_claims?: number;
  fraud_rate_pct?: number;
  fraud_amount?: number;
  [key: string]: unknown;
}
export interface ApiState<T> { data: T | null; loading: boolean; error: string | null; }
export type AnalyticsData = UnknownRecord | UnknownRecord[] | unknown[] | string | number | null;