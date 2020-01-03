from fastapi import FastAPI
from todo import router as todo_router

from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# END CORS

@app.get("/")
def index():
    """ Return simple object 
    """
    return {"status_code": "200"}

app.include_router(todo_router, prefix="/todo", tags=["TODO"])