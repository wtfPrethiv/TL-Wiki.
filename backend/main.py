from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import routes 

app = FastAPI(
    title="TL;Wiki API",
    description="Backend service for scraping, translating, and summarizing wiki topics.",
    version="1.2.0"
)

 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],           
    allow_credentials=True,
    allow_methods=["*"],           
    allow_headers=["*"],         
)

app.include_router(routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to TL;Wiki API. Use /docs to explore the endpoints."}
