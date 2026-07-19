import axios from "axios";
export const httpClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL ?? "http://127.0.0.1:8000",
  timeout: 60000,
  headers: { "Content-Type": "application/json" }
});
httpClient.interceptors.response.use(
  response => response,
  error => Promise.reject(new Error(error.response?.data?.detail ?? error.message ?? "API request failed"))
);