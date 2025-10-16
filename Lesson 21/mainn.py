from fastapi import FastAPI

# app = FastAPI()
# @app.get("/")
# def home():
#     return{"message":"HelloWorld"}

# @app.get("/user/{user_id}")
# def get_user(user_id:int):
#     return{"user_id":user_id,"name":"John Doe"}


app = FastAPI()

@app.get("/items/")
def readitems():
    return{"items":["item1","item2","item3"]}

@app.post("/items/")
def createitem(name:str,price:float):
    return{"item_name":name,"item_price":price}

@app.put("/item/{item_id}")
def updateitems(item_id:int,name:str,price:float):
    return{"item_id":item_id,"name":name,"price":price}


@app.delete("/items/{item_id}")
def deleteitems(item_id:int):
    return{"item_id":f"item {item_id} deleted"}