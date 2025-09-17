# FastAPI Backend

## Project Setup

### Initial Setup
```bash
# Create project directory
mkdir fastapi-backend
cd fastapi-backend

# Create virtual environment
python3 -m venv venv

# Create project structure
mkdir app
touch app/__init__.py
touch app/main.py
touch requirements.txt
```

### Daily Development Workflow
```bash
# 1. Navigate to project
cd my-fastapi-project

# 2. Activate virtual environment (ALWAYS DO THIS FIRST)
source venv/bin/activate
# You should see (venv) in your terminal prompt

# 3. Install/update dependencies (if needed)
pip install -r requirements.txt

# 4. Run the development server
uvicorn app.main:app --reload

# 5. When done working, deactivate environment
deactivate
```

## Important URLs
- **API**: http://127.0.0.1:8000
- **Interactive Docs**: http://127.0.0.1:8000/docs
- **Alternative Docs**: http://127.0.0.1:8000/redoc

## Useful Commands

### Virtual Environment
```bash
# Activate (do this every time you work on the project)
source venv/bin/activate

# Deactivate (when you're done)
deactivate

# Check if virtual environment is active
echo $VIRTUAL_ENV
# Should show path to your venv folder if active
```

### Server Commands
```bash
# Run with auto-reload (development)
uvicorn app.main:app --reload

# Run without auto-reload (production-like)
uvicorn app.main:app

# Run on different port
uvicorn app.main:app --reload --port 8080

# Stop server
# Press Ctrl+C in terminal
```

### Package Management
```bash
# Install new package
pip install package-name

# Install from requirements.txt
pip install -r requirements.txt

# Update requirements.txt with current packages
pip freeze > requirements.txt

# See what's installed
pip list
```

### Database Commands
```bash
# Database file location
./app.db

# To reset database (delete the file)
rm app.db
# Server will recreate it on next startup
```

## Project Structure
```
my-fastapi-project/
├── app/
│   ├── __init__.py          # Makes app a Python package
│   ├── main.py              # FastAPI app and routes
│   ├── database.py          # Database connection setup
│   ├── models.py            # Database table definitions
│   └── schemas.py           # API request/response models (future)
├── venv/                    # Virtual environment (don't commit)
├── app.db                   # SQLite database file (don't commit)
├── requirements.txt         # Python dependencies
├── .gitignore              # Files to ignore in git
└── README.md               # This file
```

## Troubleshooting

### "command not found: pip"
- Your virtual environment isn't activated
- Run: `source venv/bin/activate`
- Look for `(venv)` in your prompt

### "Module not found" errors
- Virtual environment might not be activated
- Or you need to install dependencies: `pip install -r requirements.txt`

### Server won't start
- Check if another server is running on port 8000
- Try a different port: `uvicorn app.main:app --reload --port 8080`

### Database changes not showing
- Make sure you're using `--reload` flag
- Check terminal for "Detected file change" messages

## Development Notes
- Always activate virtual environment before working
- Use `--reload` flag during development for auto-refresh
- Visit `/docs` for interactive API testing
- Database file `app.db` is created automatically
- Delete `app.db` to reset all data

## Git Setup (Optional)
```bash
# Initialize git repository
git init

# Add .gitignore to exclude sensitive files
echo "venv/" >> .gitignore
echo "*.db" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore

# First commit
git add .
git commit -m "Initial FastAPI setup"
```