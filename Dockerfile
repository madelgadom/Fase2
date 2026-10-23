
FROM python:3.11-slim

WORKDIR /aplicacion

COPY backend/requirements.txt ./backend/requirements.txt

RUN pip install --no-cache-dir -r backend/requirements.txt

COPY backend/ ./backend/
COPY frontend/ ./frontend/
COPY modelos/ ./modelos/

ENV PYTHONUNBUFFERED=1

EXPOSE 8080

CMD ["uvicorn", "backend.principal:aplicacion", "--host", "0.0.0.0", "--port", "8080"]
