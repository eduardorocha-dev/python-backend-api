# 🐉 Cryptid Tracking API

A production-oriented FastAPI backend built as a portfolio project.

------------------------------------------------------------------------

## 📌 Overview

The **Cryptid Tracking API** is a backend service that allows users
("Chasers") to:

-   Register and authenticate
-   Create and manage cryptid entries (mythical creatures)
-   Log sightings of cryptids
-   Manage their own sightings securely

This project is inspired by examples from the O'Reilly FastAPI book, but
its primary purpose is to demonstrate professional backend engineering
practices.

A separate frontend/client application will be developed later to
consume this API and provide a complete end-to-end experience.

------------------------------------------------------------------------

## 🎯 Purpose

This project demonstrates:

-   Clean architecture principles
-   FastAPI best practices
-   JWT authentication & password hashing
-   SQLAlchemy ORM modeling
-   Ownership-based authorization
-   Layered design (API → Services → Repositories → DB)
-   Alembic migrations
-   Automated testing
-   Dockerized development environment

------------------------------------------------------------------------

## 🧱 Architecture

app/ api/ \# FastAPI routers (thin controllers) core/ \# config,
security, logging db/ \# session & base models/ \# SQLAlchemy ORM models
schemas/ \# Pydantic request/response schemas repositories/ \# Data
access layer services/ \# Business logic & ownership rules main.py \#
FastAPI application entrypoint

------------------------------------------------------------------------

## 🗂 Domain Model

### User (Chaser)

-   id
-   username
-   email
-   hashed_password
-   created_at

### Cryptid

-   id
-   name
-   classification
-   description
-   rarity
-   last_seen_location
-   created_by
-   created_at

### Sighting

-   id
-   cryptid_id
-   user_id
-   location
-   date
-   notes
-   created_at

------------------------------------------------------------------------

## 🔐 Authentication & Authorization

-   JWT-based authentication
-   Password hashing using bcrypt
-   Protected routes using FastAPI dependencies
-   Ownership enforcement:
    -   Users can only modify/delete their own sightings
    -   Cryptids are globally visible
    -   Only the creator can update/delete their cryptids

------------------------------------------------------------------------

## 🚀 Features (MVP)

### Auth

-   Register
-   Login
-   JWT token issuance

### Cryptids

-   Create cryptid
-   List cryptids
-   Retrieve cryptid
-   Update (creator only)
-   Delete (creator only)

### Sightings

-   Create sighting
-   List current user's sightings
-   Filter by cryptid/date/location
-   Update (owner only)
-   Delete (owner only)

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python 3.10+
-   FastAPI
-   SQLAlchemy
-   PostgreSQL
-   Alembic
-   Pydantic
-   python-jose (JWT)
-   passlib (bcrypt)
-   Pytest
-   Docker / Docker Compose

------------------------------------------------------------------------

## 🐳 Running Locally (Docker)

docker-compose up --build

API will be available at:

http://localhost:8000

Swagger documentation:

http://localhost:8000/docs

------------------------------------------------------------------------

## 🧪 Testing

Run tests:

pytest

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Role-based access control (admin users)
-   Pagination & advanced filtering
-   CI pipeline with coverage enforcement
-   Production deployment
-   Separate frontend application
-   API versioning (/api/v1)

------------------------------------------------------------------------

## 📚 Portfolio Context

This project demonstrates backend engineering capability using FastAPI
and modern Python tooling.

It is intentionally structured to reflect real-world production systems
rather than tutorial-level CRUD examples.

------------------------------------------------------------------------

## License

MIT
