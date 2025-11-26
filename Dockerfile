#Dockerfile for IP address finder.

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --n0-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]

