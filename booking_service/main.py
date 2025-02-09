from fastapi import FastAPI
from app.api.routers import api_router
import uvicorn

# Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8001,
        reload=True
    )