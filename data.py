from typing import List, Dict, Any, Union
from enum import Enum


class OpcoesDeStatus(str, Enum):
    todo = "Todo"
    doing = "Doing"
    done = "Done"


Item = Dict[str, Union[int, str, OpcoesDeStatus]]


class TodoList:
    todo: List[Item] = [
        {"id": 1, "title": "Aprender VueJS", "status": OpcoesDeStatus.todo},
        {"id": 2, "title": "Dominar Docker", "status": OpcoesDeStatus.todo},
        {"id": 3, "title": "Aprender Go", "status": OpcoesDeStatus.todo},
    ]
    id_atual = 3

    def get_all(self):
        return self.todo
    
    def add(self, item: Item) -> Item:
        self.id_atual += 1
        item["id"] = self.id_atual
        self.todo.append(item)
        return item
    
    def get_unique_item(self, item_id: int) -> Item:
        item = filter(lambda x: x["id"] == item_id, self.todo)
        return list(item)[0]

    def filter_status(self, status: OpcoesDeStatus) -> List[Item]:
        return list(filter(lambda x: x["status"] == status, self.todo))
