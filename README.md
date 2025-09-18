# FastAPI Backend

A minimal FastAPI backend with a Makefile for common dev tasks.

Quick start
- Create venv: make venv  (or: python3 -m venv venv)
- Activate venv: source venv/bin/activate  (or: make shell for a subshell)
- Install deps: make install
- Run dev server: make dev
- Run on port 8080: make dev-port
- Show help: make help

URLs
- API: http://127.0.0.1:8000
- Docs: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

Project structure
- app/ (application code)
- requirements.txt
- makefile
- README.md
- venv/ (local, not committed)
- app.db (SQLite; auto-created; safe to delete to reset)

Notes
- The Makefile assumes your virtual environment is at ./venv.
- Uvicorn entrypoint: app.main:app.