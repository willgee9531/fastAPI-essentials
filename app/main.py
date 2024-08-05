import uvicorn
from fastapi import FastAPI
from fastapi.params import Body
# from random import randrange
# import psycopg2
# import time
# from psycopg2.extras import RealDictCursor
from . import models
from .database import engine
from .routes import posts, users, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# while True:
#     try:
#         conn = psycopg2.connect(host="localhost", database='fastapi', user='postgres', password='password', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as e:
#         print(f"connecting to database failed")
#         print(f"Error: {e}")
#         time.sleep(2)

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "fav food", "content": "content of favorite food", "id": 2}]

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/", tags=["Home"])
def root():
    return {"message": "Hello, i love FastAPI!"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, log_level="debug", debug=True)