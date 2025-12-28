# CICD NINJA 
## fastapi-hello-world

Simple FastAPI backend with a hello world endpoint.

## Setup

### Create Virtual Environment

**Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run

Start the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## Endpoints

- `GET /` - Returns a hello world message

## Testing

Run tests with pytest:
```bash
pytest
```

Or with verbose output:
```bash
pytest -v
```


