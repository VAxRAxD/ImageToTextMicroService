FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y \
        tesseract-ocr \
    && python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.src.main:app", "--host", "0.0.0.0", "--port", "8000"]