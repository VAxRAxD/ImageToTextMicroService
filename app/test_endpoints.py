import shutil,io
from fastapi.testclient import TestClient
from . main import app,BASE_DIR,UPLOAD_DIR
from PIL import Image,ImageChops

client=TestClient(app)

def test_home():
    response=client.get("/")
    assert response.status_code==200
    assert  "text/html" in response.headers['content-type']

def test_imgEcho():
    for path in (BASE_DIR/"images").glob("*"):
        try:
            img=Image.open(path)
        except:
            img=None
        response=client.post("/img-echo/",files={"file":open(path,'rb')})
        if img is not None:
            assert response.status_code==200
            assert response.status_code == 200
            r_stream = io.BytesIO(response.content)
            echo_img = Image.open(r_stream)
            difference = ImageChops.difference(echo_img, img).getbbox()
            assert difference is None
        else:
            assert response.status_code==400
    shutil.rmtree(UPLOAD_DIR)
    
