from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.src.routers.content import router as content_router
from api.src.routers.upload import router as upload_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows the Next.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(content_router)

# @app.get("/convert/{session_id}")
# def read_item(session_id: str):
#     return main(session_id)
