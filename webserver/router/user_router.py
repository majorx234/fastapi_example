from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from database import DatabaseInterface
#from models.user import User


class UserRouter:
    def __init__(self, db: DatabaseInterface):
        self._router = APIRouter(
            prefix="/user",
            tags=['user'],
        )
        self._router.add_api_route(
            "/get_users",
            self.get_users,
            methods=["GET"]
        )

    def get_router(self):
        return self._router

    def get_users(self, request: Request):
        return JSONResponse(
                content={"users": ["Torben", "Michel", "Tommy", "Annika"]},
                status_code=200)
