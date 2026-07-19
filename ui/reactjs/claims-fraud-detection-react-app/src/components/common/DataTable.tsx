import { titleCase } from "../../utils/formatters";
export default function DataTable({ data }: { data: unknown }) {
  if (!Array.isArray(data) || !data.length || typeof data[0] !== "object" || data[0] === null) return <pre>{JSON.stringify(data, null, 2)}</pre>;
  const rows = data as Record<string, unknown>[];
  const columns = Object.keys(rows[0]);
  return <div className="table-wrap"><table><thead><tr>{columns.map(c => <th key={c}>{titleCase(c)}</th>)}</tr></thead>
    <tbody>{rows.map((row, i) => <tr key={i}>{columns.map(c => <td key={c}>{typeof row[c] === "object" ? JSON.stringify(row[c]) : String(row[c] ?? "—")}</td>)}</tr>)}</tbody></table></div>;
}