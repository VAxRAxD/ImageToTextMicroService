import shutil,time
from fastapi.testclient import TestClient
from . main import app,BASE_DIR,UPLOAD_DIR

client=TestClient(app)

def test_home():
    response=client.get("/")
    assert response.status_code==200
    assert  "text/html" in response.headers['content-type']

def test_imgEcho():
    for path in (BASE_DIR/"images").glob("*"):
        response=client.post("/img-echo/",files={"file":open(path,'rb')})
        assert response.status_code==200
        fext=path.suffix.replace('.','')
        assert fext in response.headers['content-type']
    shutil.rmtree(UPLOAD_DIR)
    
