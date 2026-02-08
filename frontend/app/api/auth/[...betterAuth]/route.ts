import { drizzleAdapter } from '@better-auth/drizzle-adapter';
import { db } from '@/lib/db';
import { betterAuth } from 'better-auth';
import { toNextJsHandler } from 'better-auth/next-js';

const auth = betterAuth({
  database: drizzleAdapter(db, {
    provider: 'pg',
  }),
  secret: process.env.BETTER_AUTH_SECRET || 'fallback-secret-for-development',
  emailAndPassword: {
    enabled: true,
  },
});

export const { GET, POST } = toNextJsHandler(auth);