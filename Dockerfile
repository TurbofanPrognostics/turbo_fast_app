FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /app

WORKDIR /app

EXPOSE 80
CMD ["python3", "main.py"]
