import { useCallback, useEffect, useState } from "react";
import type { ApiState } from "../types/fraud";
export function useApi<T>(request: () => Promise<T>, immediate = true) {
  const [state, setState] = useState<ApiState<T>>({ data: null, loading: immediate, error: null });
  const execute = useCallback(async () => {
    setState(s => ({ ...s, loading: true, error: null }));
    try {
      const data = await request();
      setState({ data, loading: false, error: null });
      return data;
    } catch (error) {
      setState({ data: null, loading: false, error: error instanceof Error ? error.message : "Unknown error" });
      return null;
    }
  }, [request]);
  useEffect(() => { if (immediate) void execute(); }, [execute, immediate]);
  return { ...state, execute };
}