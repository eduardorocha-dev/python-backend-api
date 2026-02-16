# ROADMAP — FastAPI Portfolio Backend (Cryptid Tracking API)

Goal: build a professional FastAPI backend (portfolio-grade) with clean architecture, auth, ownership rules, tests, docs, and Docker. A separate frontend/client will be built later in another project to consume this API.

---

## 0) Define the product (Project framing)
**Outcome:** the repo immediately explains *what it is* and *why it exists*.

- [ ] Update `CONTEXT.md` (purpose, domain, rules, MVP scope)
- [ ] Write a 1–2 paragraph product brief in `README.md` (who uses it, what it solves, key flows)
- [ ] Define MVP vs “Later” scope explicitly
- [ ] Draft a simple ERD (markdown diagram is fine)

**Deliverables**
- `CONTEXT.md`
- `README.md` (brief + scope)
- `docs/erd.md` (or add ERD to README)

---

## 1) Project setup & tooling
**Outcome:** consistent environment and a clean baseline.

- [ ] Create repo structure (`app/`, `tests/`)
- [ ] Create `pyproject.toml` (preferred) or `requirements.txt`
- [ ] Add dependencies:
  - `fastapi`, `uvicorn`
  - `sqlalchemy`, `psycopg`/`psycopg2`
  - `pydantic`
  - `python-jose` (JWT)
  - `passlib[bcrypt]`
  - `alembic`
  - `pytest`, `httpx`
- [ ] Add code quality tools:
  - `ruff` (lint)
  - `black` (format)
  - `mypy` (optional, but good)
- [ ] Add `.gitignore`

**Deliverables**
- `app/main.py` (basic FastAPI app)
- `pyproject.toml`
- `README.md` quickstart (run locally)

---

## 2) Configuration & app bootstrap
**Outcome:** 12-factor style config with env vars.

- [ ] Implement settings (`app/core/config.py`) using environment variables
- [ ] Add `.env.example` (no secrets)
- [ ] Add centralized error response format (optional but recommended)
- [ ] Add basic logging config (`app/core/logging.py`)

**Deliverables**
- `app/core/config.py`
- `.env.example`

---

## 3) Database foundation (SQLAlchemy + Alembic)
**Outcome:** DB sessions work; migrations are supported.

- [ ] Create DB session management (`app/db/session.py`)
- [ ] Create Base + model registry (`app/db/base.py`)
- [ ] Initialize Alembic and wire it to your app models
- [ ] Add `docker-compose.yml` with PostgreSQL for local dev

**Deliverables**
- `alembic/` + `alembic.ini`
- `app/db/session.py`, `app/db/base.py`
- `docker-compose.yml`

---

## 4) Domain models (SQLAlchemy)
**Outcome:** core entities modeled with relationships + constraints.

- [ ] Implement `User` (Chaser) model
- [ ] Implement `Cryptid` model with `created_by`
- [ ] Implement `Sighting` model with FKs to `User` and `Cryptid`
- [ ] Add constraints/indexes:
  - Unique: `User.email` (and/or username)
  - Useful indexes: `Sighting.user_id`, `Sighting.cryptid_id`, `Sighting.date`
- [ ] Generate and apply first migration

**Deliverables**
- `app/models/user.py`
- `app/models/cryptid.py`
- `app/models/sighting.py`
- Alembic migration `001_initial.py`

---

## 5) Schemas (Pydantic)
**Outcome:** stable API contracts (Create/Update/Out).

- [ ] Create `UserCreate`, `UserOut`, `Token`, `Login` schemas
- [ ] Create `CryptidCreate`, `CryptidUpdate`, `CryptidOut`
- [ ] Create `SightingCreate`, `SightingUpdate`, `SightingOut`
- [ ] Ensure Pydantic v2 style (`from_attributes=True`) where needed

**Deliverables**
- `app/schemas/`

---

## 6) Security layer (hashing + JWT)
**Outcome:** secure auth flow that protects routes.

- [ ] Password hashing utilities (`app/core/security.py`)
- [ ] JWT encode/decode utilities (`app/core/jwt.py`)
- [ ] Auth dependency `get_current_user` (`app/api/deps.py`)
- [ ] Standard auth exceptions and responses

**Deliverables**
- `app/core/security.py`
- `app/core/jwt.py`
- `app/api/deps.py`

---

## 7) Repository layer (data access)
**Outcome:** DB operations are isolated and testable.

- [ ] `UserRepository`: get by email, create
- [ ] `CryptidRepository`: create, get, list, update, delete
- [ ] `SightingRepository`: create, get, list by user, update, delete, filters

**Deliverables**
- `app/repositories/`

---

## 8) Service layer (business rules + ownership)
**Outcome:** domain rules live here; endpoints stay thin.

- [ ] `AuthService`: register, authenticate (verify password), issue token
- [ ] `CryptidService`:
  - create cryptid (any authenticated user)
  - (recommended) update/delete only creator
- [ ] `SightingService`:
  - create sighting (user-owned)
  - update/delete only owner
  - list only current user’s sightings + filters

**Deliverables**
- `app/services/`
- `app/core/exceptions.py` (domain exceptions)

---

## 9) API layer (routers)
**Outcome:** usable API with docs at `/docs`.

- [ ] Add routers:
  - `/auth/register`, `/auth/login`
  - `/cryptids` (CRUD)
  - `/sightings` (CRUD, user-owned)
- [ ] Add pagination on list endpoints
- [ ] Add filtering:
  - cryptids: name/classification/rarity (optional)
  - sightings: cryptid_id, date range, location
- [ ] Verify OpenAPI schemas are clean

**Deliverables**
- `app/api/routers/auth.py`
- `app/api/routers/cryptids.py`
- `app/api/routers/sightings.py`
- `app/api/router.py` (include all routers)

---

## 10) Testing (unit + integration)
**Outcome:** portfolio-grade proof of correctness.

- [ ] Set up test database strategy:
  - Option A: ephemeral Postgres via docker-compose
  - Option B: SQLite for unit tests + Postgres integration tests
- [ ] Unit tests for services (ownership checks, auth logic)
- [ ] Integration tests for API routes using `httpx` + FastAPI `TestClient`
- [ ] Add coverage target (e.g., 70%+ initially)

**Deliverables**
- `tests/unit/`
- `tests/integration/`
- `tests/conftest.py`

---

## 11) Observability & quality gates
**Outcome:** clean logs, consistent errors, automated checks.

- [ ] Structured logging (request id optional)
- [ ] Central exception handlers (domain errors → HTTP responses)
- [ ] Add `pre-commit` hooks (ruff/black)
- [ ] Add CI (GitHub Actions):
  - lint
  - tests
  - (optional) type-check

**Deliverables**
- `.github/workflows/ci.yml`
- `.pre-commit-config.yaml` (optional)

---

## 12) Dockerization (production-like)
**Outcome:** one-command local run and deploy readiness.

- [ ] Create `Dockerfile` for FastAPI app
- [ ] Update `docker-compose.yml` to run API + DB
- [ ] Add healthcheck endpoint `/health`
- [ ] Confirm env-based config works in containers

**Deliverables**
- `Dockerfile`
- `docker-compose.yml` (API + Postgres)
- `GET /health`

---

## 13) Documentation polish (portfolio mode)
**Outcome:** the repo “sells itself” to reviewers.

- [ ] Update `README.md`:
  - project story (portfolio + book-inspired domain)
  - features list
  - architecture diagram (simple)
  - local run instructions (docker + non-docker)
  - test instructions
  - API docs link (`/docs`)
- [ ] Add screenshots (Swagger UI, ERD)
- [ ] Add “Tradeoffs & Future Work” section

**Deliverables**
- Polished `README.md`
- `docs/` (optional)

---

## 14) Frontend/client plan (separate project)
**Outcome:** clear next step without mixing concerns.

- [ ] Create a separate repo (recommended) for frontend/client
- [ ] Define the API contract usage (auth flow, endpoints)
- [ ] Build minimal UI:
  - login/register
  - cryptid list/create
  - sightings list/create

**Deliverables**
- Separate frontend repo
- Link it from backend README

---

## Milestone checkpoints (recommended)
- **M1:** Auth + DB + migrations working
- **M2:** Cryptids CRUD working
- **M3:** Sightings CRUD + ownership rules working
- **M4:** Tests + Docker + CI
- **M5:** README polish + frontend repo link
