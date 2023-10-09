from fastapi import FastAPI, Request
from routers.users import user_router


app = FastAPI(title="Simple Banking System", description="Building a simple banking system API with so far my knowledge learning FastAPI")

app.include_router(user_router, prefix="/users", tags=["Users"])



@app.get("/")
async def home():
    return {"message": "Welcome to my Simple Banking System API, check out docs at localhost:8000/docs"}



# @app.middleware("http")
# async def check_account_type(request: Request, call_next):
#     # write some code before sending request
#     response = await call_next(request)
#     # do something woth response from server
#     return response