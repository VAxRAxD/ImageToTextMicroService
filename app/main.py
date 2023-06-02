import pathlib,io,uuid
from fastapi import FastAPI,Request,Depends,HTTPException,File,UploadFile,Header 
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,FileResponse
from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    debug: bool = False
    echo_active: bool = False
    class Config:
        env_file=".env"

@lru_cache
def get_settings():
    return Settings()

DEBUG=get_settings().debug

BASE_DIR=pathlib.Path(__file__).parent
UPLOAD_DIR=BASE_DIR/"uploaded"

app=FastAPI()
templates=Jinja2Templates(directory=str(BASE_DIR/"templates"))

@app.get("/", response_class=HTMLResponse)
def home(request:Request, settings:Settings=Depends(get_settings)):
    print(DEBUG)
    return templates.TemplateResponse("home.html",{"request":request})

@app.post("/img-echo/",response_class=FileResponse)
async def imgEcho(file:UploadFile=File(...), settings:Settings=Depends(get_settings)):
    if not settings.echo_active:
        raise HTTPException(detail="Invalid Endpoint", status_code=400)
    bytes=io.BytesIO(await file.read())
    filename=pathlib.Path(file.filename)
    fileext=filename.suffix
    dest=UPLOAD_DIR/f"{uuid.uuid1}{fileext}"
    with open(str(dest),'wb') as file:
        file.write(bytes)
    return dest
