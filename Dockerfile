FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN sudo apt-get update && \
    sudo apt-get install -y \
        build-essential \
        python3-dev \
        python3-setuptools \
        tesseract-ocr \
        make \
        gcc \
    && python3 -m pip install --no-cache-dir --upgrade -r requirements.txt\
    && sudo apt-get remove -y --purge make gcc build-essential \
    && sudo apt-get autoremove -y \
    && sudo rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]