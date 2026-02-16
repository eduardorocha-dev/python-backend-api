# Project Context — Python Backend API

## Goal
Build a professional Python backend API for portfolio and curriculum purposes.

## Stack
- Python 3.10+
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication
- Docker

## Domain
Task and Project Management API

## Models Context
- Cryptids: catalog of mythical creatures (name, classification, description, rarity, last_seen_location).
- Cryptid Chasers: users who track cryptids and log sightings.
- Sightings: records linking chasers to cryptids with location, date, and notes.

## Core Features
- User registration and authentication (JWT)
- Project CRUD
- Task CRUD associated with projects
- User can only access own data

## Architecture
- app/
  - api/
  - models/
  - schemas/
  - services/
  - repositories/
  - core/
  - db/

## Rules
- No business logic in endpoints
- Use SQLAlchemy ORM
- Clean architecture
- Production-oriented code
