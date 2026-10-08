from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from typing import List


router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)


class Todo(BaseModel):
    title: str
    completed: bool = False


class TodoResponse(Todo):
    id: int


todos_db = []
todo_id = 1


# =========================
# GET /todos
# =========================

@router.get(
    "/",
    response_model=List[TodoResponse]
)
def get_todos(
    skip: int = 0,
    limit: int = 10
):
    return todos_db[skip: skip + limit]


# =========================
# POST /todos
# =========================

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=TodoResponse
)
def create_todo(todo: Todo):
    global todo_id

    todo_dict = todo.model_dump()
    todo_dict["id"] = todo_id

    todo_id += 1
    todos_db.append(todo_dict)

    return todo_dict


# =========================
# PUT /todos/{id}
# =========================

@router.put(
    "/{todo_id}",
    response_model=TodoResponse
)
def update_todo(todo_id: int, todo: Todo):
    for index, old_todo in enumerate(todos_db):

        if old_todo["id"] == todo_id:

            todo_dict = todo.model_dump()
            todo_dict["id"] = todo_id

            todos_db[index] = todo_dict

            return todo_dict

    raise HTTPException(
        status_code=404,
        detail="Todo topilmadi"
    )


# =========================
# DELETE /todos/{id}
# =========================

@router.delete(
    "/{todo_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos_db):

        if todo["id"] == todo_id:

            todos_db.pop(index)

            return None

    raise HTTPException(
        status_code=404,
        detail="Todo topilmadi"
    )
