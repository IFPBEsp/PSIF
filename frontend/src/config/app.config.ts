export const appConfig = {
  environment: process.env.APP_ENV,
  appUrl: process.env.NEXT_PUBLIC_APP_URL,
  apiInternalUrl: process.env.API_INTERNAL_URL,
} as const;
