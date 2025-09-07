# app.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config import config
from controller import predict

app = FastAPI()
templates = Jinja2Templates(directory="templates")

model_path = config.MODEL_PATH

app.include_router(predict.router)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    context = {
        "request" : request, 
        "model_name" : "Yolo_v8", 
        "description" : "6-class Classification model", 
    }
    return templates.TemplateResponse(
        name="home.html", 
        context=context
    )