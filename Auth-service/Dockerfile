FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary passlib python-jose

CMD ["uvicorn", "app1.main:app", "--host", "0.0.0.0", "--port", "8001"]