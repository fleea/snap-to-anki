import os
import uuid

from fastapi import Request, UploadFile, File, APIRouter
from fastapi.responses import JSONResponse

from api.src.main import main

router = APIRouter()


@router.post("/up")
async def upload_files(request: Request, files: list[UploadFile] = File(...)):
    try:
        session_id = request.headers.get("sessionId", str(uuid.uuid4()))
        temporary_dir = os.path.join("data", "input", session_id)

        os.makedirs(temporary_dir, exist_ok=True)

        uploaded_files = []

        for file in files:
            if file.filename:
                file_path = os.path.join(temporary_dir, file.filename)
                content = await file.read()
                with open(file_path, 'wb') as out_file:
                    out_file.write(content)

                uploaded_files.append({
                    "name": file.filename,
                    "path": file_path
                })

        # Process file
        main(session_id)

        return JSONResponse({
            "status": "success",
            "id": session_id,
            "files": uploaded_files,
        })

    except Exception as e:
        print(f"Error: {str(e)}")
        return JSONResponse({"status": "fail", "error": str(e)}, status_code=500)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
