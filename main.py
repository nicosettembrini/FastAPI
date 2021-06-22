from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published posts
    if published:
        return {'data': f'{limit} published blog list'}
    else:
        return {'data': f'{limit} all blog list'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished'}


@app.get('/blog/{id}')
def show(id: int):
    #fetch blog with id = id 
    return {'data': id}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] 
    pass

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title as {blog.title}'}




@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}