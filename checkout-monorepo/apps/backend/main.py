from fastapi import FastAPI, APIRouter
from api.products import router as products_router

app = FastAPI(
    title="Web Checkout Backend",
    description="API to allow for purchasing of products via a web checkout flow",
    version="1.0.0",
)

app.include_router(products_router, prefix="/api")

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Web Checkout Backend API!",  # Corrected message
        "docs": "/docs",  # Swagger UI
        "health_check": "/health",  # Health check endpoint
        "version": "1.0.0",
    }

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}
