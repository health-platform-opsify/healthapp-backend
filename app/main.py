from fastapi import FastAPI

app = FastAPI(title="HealthApp Backend",
              version="0.1.0",
              docs_url="/docs",
              redoc_url="/redoc",
              )





@app.get("/healthz")
def healthz():
    return {"status": "ok"}

