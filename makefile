# Variables
VENV = venv
ACTIVATE = source $(VENV)/bin/activate

# Default target
.DEFAULT_GOAL := dev

# Install dependencies (handles activation automatically)
install:
	$(ACTIVATE) && pip install -r requirements.txt

# Start development server (your main daily command)
dev:
	$(ACTIVATE) && uvicorn app.main:app --reload

# Run on different port if needed
dev-port:
	$(ACTIVATE) && uvicorn app.main:app --reload --port 8080

# Show available commands
help:
	@echo "Daily FastAPI Development Commands:"
	@echo "  make install    Install/update dependencies"
	@echo "  make dev        Start development server (default)"
	@echo "  make dev-port   Start server on port 8080"
	@echo "  make help       Show this help"

.PHONY: install dev dev-port help