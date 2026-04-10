#checklist:
#post new user: 
#get all users: 
#post new post: 
#get all posts from specific user: 
#delete user and its posts: 
#delete specific post: 
#get specific user: 
#get specific post:
#get all posts: 
#put user:
#put post:

from fastapi import FastAPI, HTTPException, status
from contextlib import asynccontextmanager
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
from bson.objectid import ObjectId
from mongodb_database import DatabaseManager
from dotenv import load_dotenv
# from typing import Optional
import os

load_dotenv()

app = FastAPI(title="MongoDB Database API", version ="1.0.0")

#pydantic models for request/response

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None

class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    age: int
    created_at: datetime

class PostCreate(BaseModel):
    user_id: str
    title: str
    content: str

class PostUpdate(BaseModel):
    # user_id: Optional[int] = None
    title: Optional[str] = None
    content: Optional[str] = None

class PostResponse(BaseModel):
    id: str
    user_id: str
    title: str
    content: str
    created_at: datetime

class PostResponseForUser(BaseModel):
    id: int
    title: str
    content: str
    created_at: str

#Initialize database
try:
    db = DatabaseManager()
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    db = None

#event handler
@app.on_event("startup")
async def startup_event():
    if db is None:
        raise Exception("Failed to connect to MongoDB")
    
@app.on_event("shutdown")
async def shutdown_event():
    if db:
        db.close_connection()


@app.get("/")
async def root():
    return {"message": "MongoDB Database API", "version": "1.0.0"}

@app.post("/users/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """Create a new user"""
    try:
        user_id = db.create_user(user.name, user.email, user.age)
        if user_id:
            return {"message": "User created successfully", "user_id": user_id}
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to create user. Email might already exist."
            )
    except Exception as e:
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Internal server error: {str(e)}"
        )

# @app.get("/users/", response_model=List[UserResponse])
# async def get_all_users():
#     """Get all users"""
#     try:
#         users = db.get_all_users()
#         return [
#             UserResponse(
#                 id=user[0],
#                 name=user[1],
#                 email=user[2],
#                 age=user[3],
#                 created_at=user[4],
#             )
#             for user in users
#         ]
#     except Exception as e:
#         raise HTTPException(
#                 status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 detail=f"Internal server error: {str(e)}"
#         )
    
# @app.get("/users/{user_id}", response_model=UserResponse)
# async def get_user(user_id: int):
#     """Get specific user by ID"""
#     try:
#         with sqlite3.connect(db.db_name) as conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
#             user = cursor.fetchone()

#             if not user:
#                 raise HTTPException(
#                     status_code=status.HTTP_404_NOT_FOUND,
#                     detail="User not found"
#                 )
            
#         return UserResponse(
#                 id=user[0],
#                 name=user[1],
#                 email=user[2],
#                 age=user[3],
#                 created_at=user[4],
#             )
#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(
#                 status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 detail=f"Internal server error: {str(e)}"
#         )
    
# @app.post("/posts/", response_model=dict, status_code=status.HTTP_201_CREATED)
# async def create_post(post: PostCreate):
#     """Create a new post"""
#     try:
#         #check if user exists
#         with sqlite3.connect(db.db_name) as conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT id FROM users WHERE id = ?", (post.user_id,))
#             if not cursor.fetchone():
#                 raise HTTPException(
#                     status_code=status.HTTP_404_NOT_FOUND,
#                     detail="User not found"
#                 )

#         post_id = db.create_post(post.user_id, post.title, post.content)
#         if post_id:
#             return {"message": "Post created successfully", "post_id": post_id}
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="Failed to create post"
#             )
#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(
#                 status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 detail=f"Internal server error: {str(e)}"
#         )
    
# @app.get("/posts/", response_model=List[PostResponse])
# async def get_all_posts():
#     """Get all posts"""
#     try:

#         with sqlite3.connect(db.db_name) as conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT * FROM posts ORDER BY created_at DESC")
#             posts = cursor.fetchall()

#         return [
#             PostResponse(
#                 id=post[0],
#                 user_id=post[1],
#                 title=post[2],
#                 content=post[3],
#                 created_at=post[4]
#             )
#             for post in posts
#         ]
#     except Exception as e:
#         raise HTTPException(
#                 status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 detail=f"Internal server error: {str(e)}"
#         )


# @app.get("/users/{user_id}/posts", response_model=List[PostResponseForUser])
# async def get_user_posts(user_id: int):
#     """Get all posts by specific user"""
#     try:
#         #check if user exists
#         with sqlite3.connect(db.db_name) as conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
#             if not cursor.fetchone():
#                 raise HTTPException(
#                     status_code=status.HTTP_404_NOT_FOUND,
#                     detail="User not found"
#                 )

#         posts = db.get_user_posts(user_id)
#         return [
#             PostResponseForUser(
#                 id=post[0],
#                 title=post[1],
#                 content=post[2],
#                 created_at=post[3],
#             )
#             for post in posts
#         ]
#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(
#                 status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 detail=f"Internal server error: {str(e)}"
#         )

# @app.delete("/users/{user_id}", response_model=dict)
# async def delete_user(user_id: int):
#     """Delete user and all their posts"""
#     try:
#         #check if user exists
#         with sqlite3.connect(db.db_name) as conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
#             if not cursor.fetchone():
#                 raise HTTPException(
#                     status_code=status.HTTP_404_NOT_FOUND,
#                     detail="User not found"
#                 )

#         success = db.delete_user(user_id)
#         if success:
#             return {"message": "User deleted successfully"}
#         else:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="Failed to delete user"
#             )
#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(
#                 status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 detail=f"Internal server error: {str(e)}"
#         )

# @app.delete("/posts/{post_id}", response_model=dict)
# async def delete_post(post_id: int):
#     """Delete specific post"""
#     try:
#         with sqlite3.connect(db.db_name) as conn:
#             cursor = conn.cursor()
#             cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
            
#             if cursor.rowcount == 0:
#                 raise HTTPException(
#                     status_code=status.HTTP_404_NOT_FOUND,
#                     detail="Post not found"
#                 )
            
#         return {"message": "Post deleted successfully"}

#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(
#                 status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 detail=f"Internal server error: {str(e)}"
#         )
    
# @app.put("/users/{user_id}", response_model=dict)
# async def put_user(user_id: int, user: UserUpdate):
#     """Update user by ID"""
#     try:
#         #check if user exists
#         with sqlite3.connect(db.db_name) as conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
#             if not cursor.fetchone():
#                 raise HTTPException(
#                     status_code=status.HTTP_404_NOT_FOUND,
#                     detail="User not found"
#                 )
            
#         update_user = db.update_user(user_id, user.name, user.email, user.age)
#         if update_user:
#             return {"message": "User updated successfully", "user_id": user_id}

#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(
#                 status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 detail=f"Internal server error: {str(e)}"
#         )
    
# @app.put("/posts/{user_id}", response_model=dict)
# async def put_post(user_id: int, post: PostUpdate):
#     """Update post by user ID"""
#     try:
#         #check if user exists
#         with sqlite3.connect(db.db_name) as conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT * FROM posts WHERE user_id = ?", (user_id,))
#             if not cursor.fetchone():
#                 raise HTTPException(
#                     status_code=status.HTTP_404_NOT_FOUND,
#                     detail="Post not found"
#                 )
            
#         update_post = db.update_post(user_id, post.title, post.content)
#         if update_post:
#             return {"message": "Post updated successfully", "user_id": user_id}

#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(
#                 status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 detail=f"Internal server error: {str(e)}"
#         )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 8001)