// API Base URL - supports both development and production
// Set VITE_API_URL environment variable for production, or use relative path for development
export const API_BASE_URL = import.meta.env.VITE_API_URL || "/api"