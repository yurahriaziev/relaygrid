from fastapi import FastAPI

app = FastAPI()

@app.get("/health", tags=['Health'])
def health():
    return {
        'status': 'ok'
    }