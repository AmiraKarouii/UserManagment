from fastapi import FastAPI
from api.routes import router
import models.User as User
from helper.engine import engine

User.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/user", tags=["user"])

