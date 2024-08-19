import asyncio
import json
import os

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

router = APIRouter()

# BASE_DIR = "data/output"
BASE_DIR = os.path.join('data', "output")


def ensure_dir_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")


# Ensure the BASE_DIR exists
ensure_dir_exists(BASE_DIR)
print(os.path.abspath(BASE_DIR))


class FolderHandler(FileSystemEventHandler):
    def __init__(self):
        self.changes = []

    def on_any_event(self, event):
        if event.is_directory:
            what = 'directory'
        else:
            what = 'file'
        self.changes.append({
            'event_type': event.event_type,
            'path': event.src_path,
            'is_directory': event.is_directory,
            'what': what
        })


def get_initial_content():
    content = []
    for root, dirs, files in os.walk(BASE_DIR):
        for name in dirs + files:
            path = os.path.join(root, name)
            content.append({
                'path': path,
                'is_directory': os.path.isdir(path)
            })
    print(content)
    return content


@router.get("/content")
async def get_content():
    async def event_stream():
        initial_content = get_initial_content()
        yield f"data: {json.dumps(initial_content)}\n\n"
        print(f"Initial content {initial_content}")

        handler = FolderHandler()
        observer = Observer()
        observer.schedule(handler, BASE_DIR, recursive=True)
        observer.start()

        try:
            while True:
                if handler.changes:
                    print(f"Changes detected: {handler.changes}")
                    yield f"data: {json.dumps(handler.changes)}\n\n"
                    handler.changes = []
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            observer.stop()
        observer.join()

    return StreamingResponse(event_stream(), media_type="text/event-stream")
