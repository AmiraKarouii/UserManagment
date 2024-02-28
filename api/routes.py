from fastapi import APIRouter
from exceptions.custom_exceptions import UserCreationException, UserNotFoundException, UserNotFoundExceptionId
from schemas.schemas import Response, RequestUser
import services.crud as crud

router = APIRouter()

@router.post("/create")
async def create_user_service(request: RequestUser):
    try:
        user_created = crud.create_user_service(request.parameter)
        return user_created
    except Exception as e:
        raise UserCreationException from e

@router.get("/allusers")
async def get_users_service():
    users = crud.get_users_service()
    return {"users": users}

@router.patch("/update/{user_id}")
async def update_user(user_id: int, request: RequestUser):
    try:
        updated_user = crud.update_user_service(user_id, **request.parameter.dict())
        return updated_user
    except Exception as e:
        raise UserNotFoundException(user_id) from e

@router.delete("/delete/{user_id}")
async def delete_user(user_id: int):
    try:
        if crud.delete_user_service(user_id):
            return Response(status="Ok", code="200", message="User deleted successfully", result=None).dict(exclude_none=True)
    except Exception as e:
        raise UserNotFoundExceptionId(user_id) from e

@router.get("/users/{nationality}")
async def get_users_by_nationality_endpoint(nationality: str):
    try:
        users = crud.get_users_by_nationality_service(nationality)
        return users
    except Exception as e:
        raise UserNotFoundException(nationality) from e
