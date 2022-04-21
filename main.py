
import uvicorn
from typing import List
############## DB & CRUD ###############################


from fastapi import Depends, FastAPI, Request, Response, Form

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()



templates = Jinja2Templates(directory="templates")



@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("home.html", {"request": request, "id": id})



@app.get("/rechner/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/mul", response_class=HTMLResponse)
async def login_template_frontend(request: Request):
    msg = "aa"
    return templates.TemplateResponse("home.html", {"request": request, "msg": msg})






if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
