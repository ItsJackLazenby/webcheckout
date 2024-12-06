from fastapi import APIRouter

router = APIRouter()

@router.get("/products")
def get_products():
    return {"message": "Returning all products"}

@router.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    return {"message": f"Returning product with ID {product_id}"}
