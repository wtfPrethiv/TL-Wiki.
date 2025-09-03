from fastapi import FastAPI
from backend.routers import routes 


app = FastAPI(
    title="TL;Wiki API",
    description="Backend service for scraping, translating, and summarizing wiki topics.",
    version="1.0.0"
)


app.include_router(routes.router)


@app.get("/")
def root():
    return {"message": "Welcome to TL;Wiki API. Use /docs to explore the endpoints."}


