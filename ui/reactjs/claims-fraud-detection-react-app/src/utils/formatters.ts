export const formatNumber = (value: unknown) =>
  typeof value === "number" ? new Intl.NumberFormat("en-IN").format(value) : "—";
export const formatCurrency = (value: unknown) =>
  typeof value === "number" ? new Intl.NumberFormat("en-IN", { style: "currency", currency: "USD", maximumFractionDigits: 0 }).format(value) : "—";
export const formatPercent = (value: unknown) =>
  typeof value === "number" ? `${value.toFixed(2)}%` : "—";
export const titleCase = (value: string) =>
  value.replace(/_/g, " ").replace(/\b\w/g, c => c.toUpperCase());