import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import product, reserve, comment, newpost, disabled
from db import models
from db.database import engine


app = FastAPI(
    title="FML's API",
    description="This API was developed for teaching Fast API",
    version="0.0.1",
    docs_url='/api/docs',
    redoc_url='/api/redoc',
    openapi_url='/api/openapi.json'
)


app.include_router(product.router)
app.include_router(reserve.router)
app.include_router(comment.router)
app.include_router(newpost.router)
app.include_router(disabled.router)

@app.get("/")
def root():
    return {"title": 'HELLO'}


if __name__ == "__main__":
    uvicorn.run("app:app", port= 5000, reload=True)


origins = [
    'http://localhost:3000',
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

models.Base.metadata.create_all(engine)