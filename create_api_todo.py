from fastapi import FastAPI, HTTPException
import uvicorn
from typing import Optional 
from pydantic import BaseModel


app = FastAPI(title= "TODO API", version= "v1")

class Todo(BaseModel): 
    name:str
    due_date: str
    description: str
    
## Create a list 
store_todo = []
print(store_todo)
# crud : create, read, update, delete 
## the get method 
@app.get("/")
async def home(): 
    return {"hello": "world"}

## Get all to dos
@app.get("/todo/", response_model= list[Todo])
async def get_all_todo(): 
    return store_todo

@app.get("/todo/{id}")
async def get_todo (id : int):
    try: 
        return store_todo[id]
    except: 
        raise HTTPException(status_code=404, detail="Todo not found in database")

@app.post("/todo/")
async def create_todo(todo:Todo):
    store_todo.append(todo)
    return todo

# Put method 

@app.put("/todo/{id}")
async def update_todo(id: int, new_todo:Todo): 
    try: 
        store_todo[id] = new_todo
        return store_todo[id]
    except: 
        raise HTTPException (status_code= 404, detail= "Todo not found in database")
    
## delete method
@app.delete("/todo/id")
async def delete_todo(id:int): 
    try: 
        obj = store_todo[id]
        store_todo.pop(id)
        return obj
    except: 
        raise HTTPException (status_code=404, detail="Todo not found in database")


if __name__ =="__main__": 
    uvicorn.run(app, host = "127.0.0.1", port = 8000)