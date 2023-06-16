import pathlib,io,pytesseract
from fastapi import FastAPI,Depends,HTTPException,File,UploadFile,Header
from pydantic import BaseSettings
from functools import lru_cache
from PIL import Image

class Settings(BaseSettings):
    app_auth_token: str
    debug: bool = False
    class Config:
        env_file=".env"

@lru_cache
def get_settings():
    return Settings()

DEBUG=get_settings().debug
BASE_DIR=pathlib.Path(__file__).parent

app=FastAPI()

def verify_auth(authorization=Header(None),settings:Settings=Depends(get_settings)):
    if settings.debug:
        return
    if authorization is None:
        raise HTTPException(detail="Unauthorized Response", status_code=401)
    if authorization != settings.app_auth_token:
        raise HTTPException(detail="Unauthorized Response", status_code=401)

@app.get("/")
def home():
    return {"Deployment":"Success"}

@app.post("/convert/")
async def imgToText(file:UploadFile=File(...), authorization=Header(None), settings:Settings=Depends(get_settings)):
    verify_auth(authorization, settings)
    bytes_str=io.BytesIO(await file.read())
    try:
        img=Image.open(bytes_str)
    except:
        raise HTTPException(detail="Invalid Image", status_code=400)
    text=str(pytesseract.image_to_string(img)).replace('\n',' ').replace('.','.\n')
    return {"text":text}