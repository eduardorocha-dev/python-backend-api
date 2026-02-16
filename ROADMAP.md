# Portfolio Roadmap — Cryptid Tracking API

This roadmap outlines a full build from scratch, with learning goals and expected project contents.

## 0) Define the product
- Write a 1–2 paragraph product brief: who uses it, what problem it solves, and key flows.
- Define core entities: `User` (chaser), `Cryptid`, `Sighting`.
- List non‑functional goals: auth, security, tests, docs, deploy.

Deliverables:
- Updated `CONTEXT.md`
- Initial ERD (even a simple diagram or text list)

## 1) Project setup
Learning goals:
- Python environment management, dependency pinning, project structure

Steps:
- Create virtual environment
- Add dependencies (`fastapi`, `uvicorn`, `sqlalchemy`, `psycopg2`, `pydantic`, `python-jose`, `passlib`)
- Create `app/` package and `main.py`
- Add `README.md` with quickstart

Deliverables:
- `app/main.py`
- `README.md` with install/run commands

## 2) Database foundation
Learning goals:
- SQLAlchemy ORM, sessions, migrations

Steps:
- Configure DB settings and session (`app/core/config.py`, `app/db/session.py`)
- Create base model (`app/db/base.py`)
- Add Alembic or choose a simple `Base.metadata.create_all` approach

Deliverables:
- DB connection config
- Migration tool configured

## 3) Domain models
Learning goals:
- Model design, relationships, constraints

Steps:
- Implement SQLAlchemy models (`User`, `Cryptid`, `Sighting`)
- Add constraints and indexes
- Add timestamps and ownership rules

Deliverables:
- `app/models/`
- ERD updated

## 4) Pydantic schemas
Learning goals:
- Request/response models, validation

Steps:
- Create `Create`, `Update`, `Out` schemas per model
- Add auth schemas (`Token`, `UserLogin`)
- Ensure `orm_mode` (or `from_attributes`) for outputs

Deliverables:
- `app/schemas/`

## 5) Repositories (data access)
Learning goals:
- Clean architecture, separation of concerns

Steps:
- Implement CRUD repository classes for each model
- Add basic list/filter methods

Deliverables:
- `app/repositories/`

## 6) Services (business logic)
Learning goals:
- Domain rules, validation, error handling

Steps:
- Create service layer functions/classes
- Enforce ownership and access rules
- Create domain exceptions

Deliverables:
- `app/services/`

## 7) API endpoints
Learning goals:
- FastAPI routing, dependency injection

Steps:
- Build auth endpoints (register/login/token)
- Add CRUD routes for `Cryptid` and `Sighting`
- Add pagination and filtering

Deliverables:
- `app/api/`
- OpenAPI docs working at `/docs`

## 8) Auth and security
Learning goals:
- JWT, hashing, protected routes

Steps:
- Implement password hashing
- JWT generation and validation
- Protect routes with dependencies

Deliverables:
- Secure auth flow
- Protected endpoints

## 9) Testing
Learning goals:
- Automated testing, fixtures

Steps:
- Add unit tests for services
- Add integration tests for API
- Use a test DB

Deliverables:
- `tests/` with coverage targets

## 10) Observability and quality
Learning goals:
- Logging, error monitoring, formatting

Steps:
- Add structured logging
- Add linting/formatting tools
- Add pre-commit hooks

Deliverables:
- `pyproject.toml` or tool configs

## 11) Deployment
Learning goals:
- Docker, environments, secrets

Steps:
- Create `Dockerfile` and `docker-compose.yml`
- Add environment variable config
- Deploy to a platform (Render, Fly.io, Railway)

Deliverables:
- Deployed API URL
- Deployment instructions in `README.md`

## 12) Portfolio polish
Learning goals:
- Communication, presentation

Steps:
- Add project screenshots/diagrams
- Write a short case study
- List features, tradeoffs, and future work

Deliverables:
- `README.md` polished with screenshots and links

## Suggested project contents (final)
- `app/` with API, services, repositories, models, schemas
- `tests/`
- `README.md`
- `CONTEXT.md`
- `Dockerfile`, `docker-compose.yml`
- `alembic/` and migration config
- `.env.example`
- `ROADMAP.md`
