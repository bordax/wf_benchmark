from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class NewUser(BaseModel):
    name: str
    age: int
    location: str


@app.get("/")
def hello_world():
    return {"Hello": "World"}


@app.post("/users")
def read_item(new_user: NewUser):
    return_value = f"{new_user.name},{new_user.age},{new_user.location},"
    return {"data": "".join([return_value for _ in range(0, 1024)])}
