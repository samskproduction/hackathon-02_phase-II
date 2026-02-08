// frontend/lib/better-auth-client.ts
import { createAuthClient } from 'better-auth/client';

export const betterAuthClient = createAuthClient({
  baseURL: process.env.NEXT_PUBLIC_BETTER_AUTH_URL || 'https://alishba51-sameer-todo-backend.hf.space', // This should match your backend URL
});