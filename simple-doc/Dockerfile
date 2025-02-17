FROM python:3.9-slim

WORKDIR /app

COPY requirements.py .

RUN pip install -no-cache-dir -r requirements.txt

COPY . .

EXPOSE 4000

CMD ["python", "app.py"]