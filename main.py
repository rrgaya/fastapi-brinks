from fastapi import FastAPI
from todo import router as todo_router

app = FastAPI()


@app.get("/")
def index():
    """ Return simple object 
    """
    return {"status_code": "200"}

app.include_router(todo_router, prefix="/todo", tags=["TODO"])