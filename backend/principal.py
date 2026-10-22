
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

aplicacion = FastAPI(
    title="Detector Inteligente de SPAM",
    description="API para clasificar mensajes mediante IA",
    version="1.0.0"
)

aplicacion.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_credentials=False,
    allow_methods=["POST", "GET"],
    allow_headers=["Content-Type"]
)


class MensajeEntrada(BaseModel):
    mensaje: str = Field(min_length=1, max_length=5000)


@aplicacion.get("/")
def inicio():
    return {
        "estado": "activo",
        "mensaje": "API del Detector Inteligente de SPAM"
    }


@aplicacion.post("/predecir")
def predecir(datos: MensajeEntrada):

    mensaje = datos.mensaje.strip()

    if not mensaje:
        return {
            "clasificacion": "Mensaje vacío"
        }

    return {
        "clasificacion": "Pendiente de modelo IA"
    }
