import { Bar, Line, Doughnut } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, BarElement, CategoryScale, Legend, LinearScale, LineElement, PointElement, Tooltip } from "chart.js";
import { toChartData } from "../utils/chartAdapters";
import type { AnalyticsData } from "../types/fraud";
ChartJS.register(ArcElement, BarElement, CategoryScale, Legend, LinearScale, LineElement, PointElement, Tooltip);
const palette = ["#2563eb","#f97316","#10b981","#8b5cf6","#ef4444","#06b6d4","#eab308","#ec4899","#14b8a6","#6366f1"];
export default function AnalyticsChart({ data, type = "bar" }: { data: AnalyticsData; type?: "bar" | "line" | "doughnut" }) {
  const chartData = toChartData(data);
  if (!chartData) return <div className="state">Chart data is not in row-based label/value format.</div>;
  const colored = { ...chartData, datasets: chartData.datasets.map((ds, i) => ({...ds,
    backgroundColor: type === "doughnut" ? palette : type === "line" ? "rgba(37,99,235,.15)" : chartData.labels.map((_,j)=>palette[j%palette.length]),
    borderColor: type === "line" ? "#2563eb" : type === "doughnut" ? "#ffffff" : chartData.labels.map((_,j)=>palette[j%palette.length]),
    borderWidth: type === "line" ? 3 : 1, tension: .35, fill: type === "line", pointBackgroundColor: "#2563eb", pointRadius: 4
  }))};
  const options = { responsive: true, maintainAspectRatio: false, plugins:{legend:{display:type==="doughnut",position:"bottom" as const}}, scales:type==="doughnut"?{}:{y:{beginAtZero:true,grid:{color:"#eef2f7"}},x:{grid:{display:false}}} };
  return <div className="chart">{type === "line" ? <Line data={colored} options={options} /> : type === "doughnut" ? <Doughnut data={colored} options={options} /> : <Bar data={colored} options={options} />}</div>;
}