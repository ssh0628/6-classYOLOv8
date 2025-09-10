# app.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config import config
from controller import predict_skin, predict_eye

app = FastAPI()
templates = Jinja2Templates(directory="templates")

skin_model_path = config.SKIN_MODEL_PATH

app.include_router(predict_skin.router)
app.include_router(predict_eye.router)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    context = {
        "request" : request, 
        "title" : "My Pet Health System", 
        "description" : "Check my pet's health using a Picture", 
    }
    return templates.TemplateResponse(
        name="home.html", 
        context=context
    )
