FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y \
        build-essential \
        python3-setuptools \
        python3-dev \
        tesseract-ocr \
    && python3 -m pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]