import { useCallback, useState } from "react";
import { AlertTriangle, BadgeDollarSign, BrainCircuit, FileWarning, RefreshCw, ShieldAlert } from "lucide-react";
import { fraudApi } from "../api/fraudApi";
import { useApi } from "../hooks/useApi";
import KpiCard from "../components/KpiCard";
import AnalyticsChart from "../components/AnalyticsChart";
import SectionCard from "../components/SectionCard";
import DataTable from "../components/common/DataTable";
import AnomalyCards from "../components/AnomalyCards";
import RootCauseCards from "../components/RootCauseCards";
import ModelMetricsCards from "../components/ModelMetricsCards";
import ExecutiveSummary from "../components/ExecutiveSummary";
import Loading from "../components/common/Loading";
import ErrorMessage from "../components/common/ErrorMessage";
import { formatCurrency, formatNumber, formatPercent } from "../utils/formatters";

export default function FraudDashboard() {
  const kpis = useApi(useCallback(() => fraudApi.kpis(), []));
  const states = useApi(useCallback(() => fraudApi.fraudByState(), []));
  const providers = useApi(useCallback(() => fraudApi.fraudByProvider(), []));
  const procedures = useApi(useCallback(() => fraudApi.fraudByProcedure(), []));
  const trend = useApi(useCallback(() => fraudApi.fraudTrend(), []));
  const risk = useApi(useCallback(() => fraudApi.riskDistribution(), []));
  const anomalies = useApi(useCallback(() => fraudApi.anomalyDetection(), []));
  const rootCauses = useApi(useCallback(() => fraudApi.rootCauseAnalysis(), []));
  const metrics = useApi(useCallback(() => fraudApi.modelMetrics(), []));
  const features = useApi(useCallback(() => fraudApi.featureImportance(), []));
  const summary = useApi(useCallback(() => fraudApi.executiveSummary(), []));
  const [training, setTraining] = useState(false);
  const [trainMessage, setTrainMessage] = useState("");

  const train = async () => {
    setTraining(true); setTrainMessage("");
    try { const result = await fraudApi.trainModel(); setTrainMessage(typeof result === "string" ? result : JSON.stringify(result)); await metrics.execute(); await features.execute(); }
    catch (e) { setTrainMessage(e instanceof Error ? e.message : "Training failed"); }
    finally { setTraining(false); }
  };

  const panel = (state: { loading: boolean; error: string | null; data: unknown }, chart?: "bar" | "line" | "doughnut") =>
    state.loading ? <Loading /> : state.error ? <ErrorMessage message={state.error} /> : chart ? <AnalyticsChart data={state.data as never} type={chart} /> : <DataTable data={state.data} />;

  return <main className="app-shell">
    <header className="hero"><div><p className="eyebrow">Healthcare Claims Analytics</p><h1>Fraud Detection Command Center</h1><p>Descriptive, diagnostic, predictive and anomaly analytics powered by the FastAPI fraud router.</p></div>
      <button onClick={train} disabled={training}><BrainCircuit size={18}/>{training ? "Training…" : "Train Model"}</button></header>

    {kpis.error && <ErrorMessage message={kpis.error} />}
    <div className="kpi-grid">
      <KpiCard label="Total Claims" value={formatNumber(kpis.data?.total_claims)} icon={<FileWarning/>}/>
      <KpiCard label="Fraud Claims" value={formatNumber(kpis.data?.fraud_claims)} icon={<ShieldAlert/>}/>
      <KpiCard label="Fraud Rate" value={formatPercent(kpis.data?.fraud_rate_pct)} icon={<AlertTriangle/>}/>
      <KpiCard label="Fraud Amount" value={formatCurrency(kpis.data?.fraud_amount)} icon={<BadgeDollarSign/>}/>
    </div>
    {trainMessage && <div className="notice">{trainMessage}</div>}

    <div className="dashboard-grid">
      <SectionCard title="Fraud Trend">{panel(trend, "line")}</SectionCard>
      <SectionCard title="Risk Distribution">{panel(risk, "doughnut")}</SectionCard>
      <SectionCard title="Fraud by State">{panel(states, "bar")}</SectionCard>
      <SectionCard title="Fraud by Provider">{panel(providers, "bar")}</SectionCard>
      <SectionCard title="Fraud by Procedure">{panel(procedures, "bar")}</SectionCard>
      <SectionCard title="Feature Importance">{panel(features, "bar")}</SectionCard>
    </div>

    <div className="detail-grid">
      <SectionCard title="Anomaly Detection">{anomalies.loading ? <Loading/> : anomalies.error ? <ErrorMessage message={anomalies.error}/> : <AnomalyCards data={anomalies.data}/>}</SectionCard>
      <SectionCard title="Root Cause Analysis">{rootCauses.loading ? <Loading/> : rootCauses.error ? <ErrorMessage message={rootCauses.error}/> : <RootCauseCards data={rootCauses.data}/>}</SectionCard>
      <SectionCard title="Model Metrics">{metrics.loading ? <Loading/> : metrics.error ? <ErrorMessage message={metrics.error}/> : <ModelMetricsCards data={metrics.data}/>}</SectionCard>
      <SectionCard title="Executive Summary">{summary.loading ? <Loading/> : summary.error ? <ErrorMessage message={summary.error}/> : <ExecutiveSummary data={summary.data}/>}</SectionCard>
    </div>
    <footer><RefreshCw size={14}/> API base URL: {import.meta.env.VITE_API_BASE_URL ?? "http://127.0.0.1:8000"}</footer>
  </main>;
}