

# Fast API
from fastapi import FastAPI

# Application
from app.demo.routes import home_router


def get_application():
    """
    Get Application
    Get application build our ASGI interface using FastAPI
    :return app: FastAPI -> Fast api application
    """
    app: FastAPI = FastAPI()
    app.include_router(home_router)
    return app


application = get_application()
