from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
import models.User as User
from helper.engine import engine, origins
from fastapi import FastAPI

app = FastAPI(debug=True)
User.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/user", tags=["user"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "PATCH","POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

