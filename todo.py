from fastapi import APIRouter
from typing import List, Optional
from model import ModeloDoItem, ModeloDoItemResposta
from data import TodoList, OpcoesDeStatus


router = APIRouter()
todo = TodoList()

@router.get("/", response_model=List[ModeloDoItemResposta], tags=["TODO"])
def todo_list(status: Optional[OpcoesDeStatus] = None):
    """
    Return TodoList
    """
    if status is not None:
        return todo.filter_status(status=status)
    return todo.get_all()


@router.post("/", response_model=ModeloDoItemResposta, tags=["TODO"], status_code=201)
def todo_post(item_todo_list: ModeloDoItem):
    """
    POST new item TodoList
    """
    return todo.add(item_todo_list.dict())


@router.get("/{item_id}", response_model=ModeloDoItemResposta, tags=["TODO"])
def get_unique_item(item_id: int):
    """
    GET unique item TodoList
    """
    return todo.get_unique_item(item_id)
