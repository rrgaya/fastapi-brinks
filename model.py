from pydantic import BaseModel
from typing import Optional
from data import OpcoesDeStatus


class ModeloDoItem(BaseModel):
    title: str
    status: Optional[OpcoesDeStatus]


class ModeloDoItemResposta(ModeloDoItem):
    id: int