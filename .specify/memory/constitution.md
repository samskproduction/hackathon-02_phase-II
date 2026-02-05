# Project Constitution: Hackathon Phase 2 – Todo Full-Stack Web Application

## Core Principles

### I. Spec-Driven Development
All implementation must follow specifications defined in the `/specs` folder with zero manual coding - all code generated via Claude Code using Spec-Kit references. Every feature and requirement must be traceable to specifications, ensuring consistent and predictable development outcomes.

### II. Technology Stack Adherence
Adhere strictly to the defined technology stack: Next.js 16+ (App Router) for frontend, FastAPI and SQLModel for backend, Neon Serverless PostgreSQL for database, and Better Auth with JWT plugin for authentication. The architecture follows a monorepo structure with modular agents to ensure consistency and maintainability.

### III. Security & Data Isolation
Implement complete user data isolation where users can only access their own tasks. All API endpoints require valid JWT tokens, database queries must be filtered by authenticated user_id, and maintain stateless authentication with no server-side session storage to prevent data leakage between users.

### IV. Quality Standards
Maintain clean, responsive UI using Tailwind CSS with proper error handling and validation. Ensure comprehensive API documentation and create testable, modular code structure that follows industry best practices for maintainability and scalability.

### V. Agentic Development Process
Follow a fully agentic development approach using modular agents (Main Agent, Task Agent, Auth Agent, UI Agent) with defined responsibilities. Leverage server components by default in Next.js and implement proper middleware for JWT verification to ensure secure and efficient operation.

### VI. Architecture Requirements

Enforce modular architecture through agents and skills with clear separation of concerns. Maintain server components by default in Next.js, implement proper middleware for JWT verification, and ensure all CRUD operations enforce task ownership to maintain data integrity.

## Technical Constraints

Non-negotiable requirements include Better Auth configured with JWT plugin and shared BETTER_AUTH_SECRET, database schema that matches specifications exactly, and all CRUD operations that enforce task ownership. The frontend must communicate with backend only through protected API endpoints, with no external libraries beyond the specified stack, no direct database access from frontend, and no session storage on backend. The monorepo structure must match the documented layout.

## Success Criteria

Functional requirements include complete implementation of 5 basic task CRUD operations with toggle completion, successful user signup and login with Better Auth, JWT tokens issued on login and automatically attached to API requests, FastAPI middleware correctly verifying JWT and extracting user_id, and all database queries filtered by authenticated user_id with zero data leakage.

Non-functional requirements encompass responsive frontend with task list, create/edit forms, and authentication pages, application running locally with docker-compose up, entire implementation traceable to specs via Claude Code prompts, and full agentic structure with properly defined agents and skills.

Delivery requirements demand a fully structured monorepo with all specs and configuration, working full-stack application meeting all acceptance criteria, clear history of spec-driven Claude Code prompts, and zero manual coding with all implementation generated via Claude Code.

## Governance
This constitution supersedes all other development practices. All implementation must adhere to these principles, and any deviations require formal documentation and approval. Code reviews must verify compliance with all constitutional requirements, and complexity must be justified against these foundational principles. Use the defined spec-kit tools for runtime development guidance.

**Version**: 1.0.0 | **Ratified**: 2026-02-05 | **Last Amended**: 2026-02-05
