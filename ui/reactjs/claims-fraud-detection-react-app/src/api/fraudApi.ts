import { httpClient } from "./httpClient";
import type { AnalyticsData, FraudKpis } from "../types/fraud";

const prefix = "/fraud";
const get = async <T>(path: string): Promise<T> => (await httpClient.get<T>(`${prefix}${path}`)).data;

export const fraudApi = {
  dashboard: () => get<AnalyticsData>("/dashboard"),
  kpis: () => get<FraudKpis>("/kpis"),
  totalClaims: () => get<{ total_claims: number }>("/total-claims"),
  fraudClaims: () => get<{ fraud_claims: number }>("/fraud-claims"),
  fraudRate: () => get<{ fraud_rate_pct: number }>("/fraud-rate"),
  fraudAmount: () => get<{ fraud_amount: number }>("/fraud-amount"),
  fraudByState: () => get<AnalyticsData>("/fraud-by-state"),
  fraudByProvider: () => get<AnalyticsData>("/fraud-by-provider"),
  fraudByProcedure: () => get<AnalyticsData>("/fraud-by-procedure"),
  fraudTrend: () => get<AnalyticsData>("/fraud-trend"),
  rootCauseAnalysis: () => get<AnalyticsData>("/root-cause-analysis"),
  trainModel: async () => (await httpClient.post<AnalyticsData>(`${prefix}/train-model`)).data,
  modelMetrics: () => get<AnalyticsData>("/model-metrics"),
  featureImportance: () => get<AnalyticsData>("/feature-importance"),
  anomalyDetection: () => get<AnalyticsData>("/anomaly-detection"),
  riskDistribution: () => get<AnalyticsData>("/risk-distribution"),
  charts: () => get<AnalyticsData>("/charts"),
  executiveSummary: () => get<AnalyticsData>("/executive-summary"),
  fraudReport: () => get<AnalyticsData>("/fraud-report"),
  modelReport: () => get<AnalyticsData>("/model-report")
};