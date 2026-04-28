from fastapi import (
    FastAPI,
)
from fastapi.middleware.cors import CORSMiddleware

from router.user_router import UserRouter
from database import DatabaseInterface
from config import Config


class Backend:
    """
    A class to represent the backend.

    ...

    """
    def __init__(self,
                 db: DatabaseInterface,
                 config: Config):
        """
        Constructs all necessary attributes for the backend object.

        Parameters
        ----------
            db : object of DatabaseInterface class
            config : object of Config class
        """
        self.db = db
        self.config = config
        self.app = FastAPI(
            title="FastAPI example backend",
            description="backend functionalities for webserver",
            swagger_ui_parameters={"persistAuthorization": True}
        )

        # allowing cors
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=config.allowed_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # set up routers
        user_router = UserRouter(db)
        self.app.include_router(user_router.get_router())

    def get_app(self):
        return self.app
