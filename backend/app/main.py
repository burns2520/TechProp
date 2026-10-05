from fastapi import FastAPI

app = FastAPI(
    title="TechProp API",
    version="0.1.0",
    description="Backend API for TechProp property-rental marketplace"
)

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "techprop-api"}
