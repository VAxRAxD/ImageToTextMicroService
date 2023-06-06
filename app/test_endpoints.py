from fastapi.testclient import TestClient
from . main import app,BASE_DIR,get_settings
from PIL import Image

client=TestClient(app)

def test_imgToText():
    for path in (BASE_DIR/"test_images").glob("*"):
        try:
            img=Image.open(path)
        except:
            img=None
        response=client.post("/convert/",files={"file":open(path,'rb')},headers={"Authorization":get_settings().app_auth_token})
        if img is not None:
            assert response.status_code==200
        else:
            assert response.status_code==400