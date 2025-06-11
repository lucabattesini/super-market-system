from fastapi import APIRouter, status, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_all_inventory_info_route():
    return