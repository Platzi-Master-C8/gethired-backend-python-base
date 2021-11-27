

# Fast API
from fastapi import FastAPI


def get_application():
    """
    Get Application
    Get application build our ASGI interface using FastAPI
    :return app: FastAPI -> Fast api application
    """
    app: FastAPI = FastAPI()
    return app


application = get_application()
