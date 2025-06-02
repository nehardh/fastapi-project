from fastapi import FastAPI

app = FastAPI()

#All static paths are written before the dynamic paths.


#Here index function is called as path operation function
# get is an operation
# @app... is called path operation decorator
# "/" is the path
#Decorator is defined with an "@" symbol as a prefix
@app.get("/blog")
def index(limit):
    return {
        "data": {
            f'{limit} Blog list from the db'
        }
    }

@app.get('/blog/unpublished')
def unpublished():
    return {
        "data": "All unpublished blogs"
    }

@app.get('/blog/{id}')
def show(id: int):
    return {
        "data": id
    }