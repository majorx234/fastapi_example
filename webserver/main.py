from os import path
import uvicorn

from config import Config
from database import DatabaseInterface
from backend import Backend


def main():
    """
    Main function, called first when program starts

    """
    config = Config()
    print(config)
    db = DatabaseInterface()
    backend = Backend(db, config)

    uvicorn.run(backend.get_app(), host=config.host, port=config.port)


if __name__ == '__main__':
    main()
