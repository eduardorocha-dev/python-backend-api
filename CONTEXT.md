# Project Context — FastAPI Portfolio Backend

## Purpose
Build a professional, production-oriented FastAPI backend API as a portfolio project.

The domain theme (Cryptid Tracking) is inspired by an O’Reilly FastAPI book example,
but the real objective is to demonstrate backend engineering skills:

- Clean architecture
- Authentication & authorization
- Database modeling
- Layered design (API → Services → Repositories → DB)
- Testing
- Dockerized deployment
- Production-oriented structure

A separate frontend/client application will be developed later in a different project
to consume this API and make the system fully functional end-to-end.

---

## Product Overview

The Cryptid Tracking API allows users ("Chasers") to:

- Register and authenticate
- Create and manage cryptid entries
- Log sightings of cryptids
- View and manage their own sightings

Each authenticated user acts as a **Cryptid Chaser**.

The system enforces ownership rules:
- Users can only modify or delete their own sightings.
- Cryptids are globally visible.
- Any authenticated user can create cryptids.

---

## Core Entities

### User (Chaser)
Represents an authenticated account.

Fields:
- id
- username
- email
- hashed_password
- created_at

---

### Cryptid
Catalog entry for a mythical creature.

Fields:
- id
- name
- classification
- description
- rarity
- last_seen_location
- created_by (User ID)
- created_at

---

### Sighting
Record of a user observing a cryptid.

Fields:
- id
- cryptid_id (FK)
- user_id (FK)
- location
- date
- notes
- created_at

---

## Core Features (MVP)

### Authentication & Security
- User registration
- Login
- JWT authentication
- Password hashing
- Protected routes

### Cryptids
- Create cryptid
- List cryptids (public)
- Retrieve cryptid
- Update cryptid (optional: only creator or open editing)
- Delete cryptid (optional: only creator)

### Sightings
- Create sighting
- List current user's sightings
- Filter by cryptid/date/location
- Update sighting (owner only)
- Delete sighting (owner only)

---

## Non-Functional Goals (Portfolio Signals)

- Clear separation of concerns
- No business logic in endpoints
- Service layer enforces ownership
- Repository layer encapsulates DB access
- SQLAlchemy ORM with PostgreSQL
- Alembic migrations
- Automated tests (services + API)
- Structured logging
- Dockerized setup
- Clean OpenAPI documentation

---

## Stack

- Python 3.10+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- python-jose (JWT)
- passlib (bcrypt)
- Pytest
- Docker / Docker Compose

---

## Architecture

app/
  api/           # FastAPI routers
  core/          # settings, security, config
  db/            # session and base
  models/        # SQLAlchemy models
  schemas/       # Pydantic schemas
  repositories/  # data access layer
  services/      # business logic
  main.py        # application entrypoint

tests/
Dockerfile
docker-compose.yml
.env.example
README.md
ROADMAP.md

---

## Engineering Rules

- Endpoints remain thin.
- All business rules live in services.
- Repositories perform only DB access.
- Ownership checks are explicit.
- API contracts are stable and documented.
