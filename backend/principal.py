
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from pathlib import Path

import joblib
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Configurar las rutas del proyecto
ruta_principal = Path(__file__).resolve().parent.parent
ruta_modelo = ruta_principal / "modelos" / "modelo_spam.joblib"
ruta_vectorizador = ruta_principal / "modelos" / "vectorizador_tfidf.joblib"

# Cargar el modelo y el vectorizador
modelo_principal = joblib.load(ruta_modelo)
vectorizador_principal = joblib.load(ruta_vectorizador)

# Crear la aplicación FastAPI
aplicacion = FastAPI(
    title="Detector Inteligente de SPAM",
    description="API de clasificación de mensajes mediante IA",
    version="1.0.0"
)

# Configurar la comunicación con el frontend
aplicacion.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"]
)

# Definir la estructura del mensaje
class MensajeEntrada(BaseModel):
    mensaje: str = Field(min_length=1, max_length=5000)


# Endpoint de estado
@aplicacion.get("/")
def inicio():
    return {
        "estado": "activo",
        "mensaje": "API del Detector Inteligente de SPAM"
    }


# Endpoint de clasificación
@aplicacion.post("/predecir")
def predecir(datos: MensajeEntrada):

    mensaje = datos.mensaje.strip()

    if not mensaje:
        raise HTTPException(
            status_code=400,
            detail="El mensaje no puede estar vacío"
        )

    # Transformar el mensaje mediante TF-IDF
    matriz_mensaje = vectorizador_principal.transform(
        [mensaje]
    )

    # Realizar la predicción
    prediccion = modelo_principal.predict(
        matriz_mensaje
    )[0]

    # Obtener la probabilidad de clasificación
    probabilidades = modelo_principal.predict_proba(
        matriz_mensaje
    )[0]

    confianza = round(
        float(max(probabilidades)) * 100,
        2
    )

    return {
        "clasificacion": str(prediccion),
        "confianza": confianza
    }


# Configuración de la interfaz web
ruta_frontend = ruta_principal / "frontend"

aplicacion.mount(
    "/archivos",
    StaticFiles(directory=str(ruta_frontend)),
    name="archivos"
)

@aplicacion.get("/aplicacion", include_in_schema=False)
def mostrar_aplicacion():
    return FileResponse(
        ruta_frontend / "index.html"
    )
