from fastapi import APIRouter, Depends, HTTPException
from app.schemas import TaskCreate, TaskUpdate
from app.database import task_collection
from app.auth import get_current_user
from bson import ObjectId

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/")
async def create_task(task: TaskCreate, user=Depends(get_current_user)):
    await task_collection.insert_one({
        "title": task.title,
        "description": task.description,
        "completed": False,
        "owner_id": user["_id"]
    })
    return {"message": "Task created"}

@router.get("/")
async def get_tasks(user=Depends(get_current_user)):
    tasks = await task_collection.find(
        {"owner_id": user["_id"]}
    ).to_list(100)
    for task in tasks:
        task["_id"] = str(task["_id"])
    return tasks

@router.put("/{task_id}")
async def update_task(task_id: str, task: TaskUpdate, user=Depends(get_current_user)):
    result = await task_collection.update_one(
        {"_id": ObjectId(task_id), "owner_id": user["_id"]},
        {"$set": task.dict(exclude_unset=True)}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task updated"}

@router.delete("/{task_id}")
async def delete_task(task_id: str, user=Depends(get_current_user)):
    result = await task_collection.delete_one(
        {"_id": ObjectId(task_id), "owner_id": user["_id"]}
    )
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
