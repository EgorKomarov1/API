from fastapi import APIRouter

from routers.flights import router as flights_router
from routers.airplanes import router as airplanes_router
from routers.segments import router as segments_router

router = APIRouter()

router.include_router(flights_router)
router.include_router(airplanes_router)
router.include_router(segments_router)

