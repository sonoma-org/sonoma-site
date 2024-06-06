from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi import FastAPI, Request
import os
from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

port = 8096
addr = "127.0.0.1"
app = FastAPI()
templates = Jinja2Templates(directory="www")


class Server:
    def __init__(self):
        self.port = port
        self.addr = addr
        app.mount(
    "/www",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "www"),
    name="www",
)

    @app.get("/")
    def index(self: Request):
        return templates.TemplateResponse(
            "index.html", {"request": self}
        )
    
    @app.get("/projects")
    def projects(self: Request):
        return templates.TemplateResponse(
            "projects.html", {"request": self}
        )
    
    @app.get("/contact")
    def contact(self: Request):
        return templates.TemplateResponse(
            "contact.html", {"request": self}
        )
    
    @app.get("/images/sonoma.png")
    def contact(self: Request):
        return FileResponse(Path('www/images/sonoma.png'))
    

    def start_server(self):
        uvicorn.run(app, port=self.port, proxy_headers=True, host=self.addr)


if __name__ == '__main__':
    Server().start_server()
