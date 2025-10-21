import uvicorn

from PY.apis import app

if __name__ == "__main__":
    uvicorn(app, host ="127.0.0.1", port = 8000)