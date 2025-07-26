
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router as app_router
from db.database import TORTOISE_ORM
from tortoise.contrib.fastapi import register_tortoise

app=FastAPI(
    title="Notes App API",
    description="API for managing notes",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Register Tortoise ORM with FastAPI
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)


app.include_router(app_router, tags=["notes"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Welcome to Notes App API"}
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "Notes App API"}
