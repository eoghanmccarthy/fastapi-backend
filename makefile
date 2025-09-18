# Variables
PYTHON = python3
VENV = venv
ACTIVATE = source $(VENV)/bin/activate

# Default target
.DEFAULT_GOAL := dev

# Create virtual environment if missing (run once)
$(VENV):
	@test -d $(VENV) || $(PYTHON) -m venv $(VENV)

# Install dependencies (ensures venv exists)
install: $(VENV)
	$(ACTIVATE) && pip install -r requirements.txt

# Start development server (your main daily command)
dev: $(VENV)
	$(ACTIVATE) && uvicorn app.main:app --reload

# Run on different port if needed
dev-port: $(VENV)
	$(ACTIVATE) && uvicorn app.main:app --reload --port 8080

# Open an interactive shell with the venv activated (child shell only)
shell: $(VENV)
	$(ACTIVATE) && exec bash -i

# Show available commands
help:
	@echo "Daily FastAPI Development Commands:"
	@echo "  make venv       Create virtual environment (if missing)"
	@echo "  make install    Install/update dependencies"
	@echo "  make dev        Start development server (default)"
	@echo "  make dev-port   Start server on port 8080"
	@echo "  make shell      Open subshell with venv activated"
	@echo "  make help       Show this help"

.PHONY: install dev dev-port shell help