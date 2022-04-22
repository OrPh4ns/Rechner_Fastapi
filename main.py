import uvicorn
from typing import List
############## DB & CRUD ###############################


from fastapi import Depends, FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/rechner/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/rechnen/", response_class=HTMLResponse)
async def login(request:Request, n1: str = Form(...), n2: str = Form(...), operator: str = Form(...)):
    erg = int(n1) * int(n2)
    return templates.TemplateResponse("home.html", {"request": request, "erg": erg, "operator":operator})


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
