from fastapi import FastAPI
from todo import router as todo_router

app = FastAPI()


@app.get("/")
def ola_mundo():
    """
    Retorna meu ojeto  
    """
    return {"ola": "mundo"}

app.include_router(todo_router, prefix="/todo", tags=["TODO"])