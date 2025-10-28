from fastapi import FastAPI
from app.api.v1.routes.organization import router as org_router
from app.api.v1.routes.patients import router as patients_router

app = FastAPI(title="HealthApp Backend",
              version="0.1.0",
              docs_url="/docs",
              redoc_url="/redoc",
              )


# Include versioned routes
app.include_router(org_router, prefix="/api/v1", tags=["organizations"])
app.include_router(patients_router, prefix="/api/v1", tags=["patients"])

@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}

