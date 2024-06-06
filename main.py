import uvicorn
from fastapi import FastAPI, Request
import os
from fastapi.responses import HTMLResponse

port = 80
addr = "0.0.0.0"
app = FastAPI()


class Server:
    def __init__(self):
        self.port = port
        self.addr = addr

    @app.get("/")
    def doc(self: Request):
        with open(os.path.join('www/images/index.html')) as fh:
            data = fh.read()
        return HTMLResponse(content=data)

    def start_server(self):
        uvicorn.run(app, port=self.port, proxy_headers=True, host=self.addr)


if __name__ == '__main__':
    Server().start_server()
