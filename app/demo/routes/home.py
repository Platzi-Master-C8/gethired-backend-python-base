
# FastAPI
from fastapi import APIRouter, Body

# Project
from app.demo.schemas import HomeInput

router: APIRouter = APIRouter()


@router.get(
    "/",
    summary="Home route",
)
def home():
    """
    Home
    home router.
    :return: dict -> base response.
    """
    return dict(var="foo")


@router.post(
    '/',
    summary="Say hi"
)
def say_hi(data: HomeInput = Body(...)):
    """
    Say hi
    This functions says hi to you.
    :param data: BodyParameter
        - name: str -> Your name
    :return:
    """
    return f'Hi {data.name}'
