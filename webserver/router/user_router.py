from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from database import DatabaseInterface
#from models.user import User
from sqlmodel import select
from sqlmodels.model import Users as SqlUsers
from backend_models.schema import User


class UserRouter:
    def __init__(self, db: DatabaseInterface):
        self.db = db
        self._router = APIRouter(
            prefix="/user",
            tags=['user'],
        )
        self._router.add_api_route(
            "/get_users",
            self.get_users,
            methods=["GET"]
        )
        self._router.add_api_route(
            "/get_users_db",
            self.get_users_db,
            methods=["GET"]
        )

    def get_router(self):
        return self._router

    def get_users(self, request: Request):
        return JSONResponse(
                content={"users": ["Torben", "Michel", "Tommy", "Annika"]},
                status_code=200)

    def get_users_db(self, request: Request):
        user_list = self.db.query(select(SqlUsers.name))
        return JSONResponse(
                content={"users": user_list},
                status_code=200)
