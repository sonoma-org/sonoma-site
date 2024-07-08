from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi import FastAPI, HTTPException, Request
import os
from pathlib import Path
from fastapi.responses import FileResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from repos import get_reps, get_json_names, get_rep
from refresh import thread

port = 80
addr = "0.0.0.0"
app = FastAPI()
templates = Jinja2Templates(directory="www")


class Server:
    def __init__(self):
        self.port = port
        self.addr = addr
        thread.start()
        app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "www"),
    name="static",)

    @app.get("/")
    def index(self: Request):
        return templates.TemplateResponse(
            "index.html", {"request": self}
        )
    
    @app.get("/projects")
    def projects(self: Request):
        return templates.TemplateResponse(
            "pages/projects.html", {"request": self}
        )
    
    @app.get("/contact")
    def contact(self: Request):
        return templates.TemplateResponse(
            "pages/contact.html", {"request": self}
        )
    
    @app.get("/images/sonoma.png")
    def contact(self: Request):
        return FileResponse(Path('www/images/sonoma.png'))
    
    @app.get("/favicon.ico")
    def contact(self: Request):
        return FileResponse(Path('www/icons/favicon.ico'))
    
    @app.get("/api/projects")
    def all(self: Request):
        repos = get_json_names()

        return JSONResponse(content=repos)
    
    @app.get("/projects/{name}")
    def rep(self: Request, name):
        rep = get_rep(name)

        if rep is not None:
            return templates.TemplateResponse(
                "html/repos.html", {"request": self, "rep": rep}
            )
        else:
            raise HTTPException(status_code=404)
    

    def start_server(self):
        uvicorn.run(app, port=self.port, proxy_headers=True, host=self.addr)


if __name__ == '__main__':
    Server().start_server()
