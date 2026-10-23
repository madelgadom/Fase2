# Detector Inteligente de SPAM mediante Inteligencia Artificial

## Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación web capaz de clasificar mensajes de texto como SPAM o NO SPAM mediante técnicas de Inteligencia Artificial y procesamiento de lenguaje natural (NLP).

La solución utiliza un modelo de aprendizaje supervisado basado en el algoritmo Multinomial Naive Bayes, entrenado con el conjunto de datos SMS Spam Collection. Para representar numéricamente los mensajes, se utiliza la técnica TF-IDF.

La aplicación integra una interfaz web desarrollada con HTML, CSS y JavaScript, un backend implementado mediante FastAPI y un modelo de clasificación entrenado con Scikit-learn.

## Tecnologías utilizadas

- Python 3.11
- Scikit-learn
- Pandas y NumPy
- TF-IDF
- Multinomial Naive Bayes
- FastAPI
- HTML, CSS y JavaScript
- Docker
- GitHub

## Arquitectura de la solución

El usuario introduce un mensaje mediante la interfaz web. JavaScript envía una solicitud HTTP POST al endpoint `/predecir` de FastAPI.

El backend recibe y valida el mensaje, lo transforma mediante el vectorizador TF-IDF y utiliza el modelo Naive Bayes para generar una clasificación.

Finalmente, la API devuelve una respuesta JSON con la categoría identificada y su porcentaje de confianza estimado, que se presenta visualmente en el frontend.

## Estructura del repositorio

```text
Fase2/
├── backend/
│   ├── principal.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── estilos.css
│   └── aplicacion.js
├── modelos/
│   ├── modelo_spam.joblib
│   └── vectorizador_tfidf.joblib
├── Dockerfile
├── .dockerignore
└── README.md
```

## Ejecución local mediante Docker

Para ejecutar la aplicación es necesario contar con Docker Desktop o un motor Docker compatible.

Clonar el repositorio:

```bash
git clone https://github.com/madelgadom/Fase2.git
cd Fase2
```

Construir la imagen:

```bash
docker build -t detector-spam-ia:1.0 .
```

Ejecutar el contenedor:

```bash
docker run -d --name detector-spam -p 8080:8080 detector-spam-ia:1.0
```

Abrir la aplicación:

http://localhost:8080/aplicacion

Consultar la documentación de la API:

http://localhost:8080/docs

## API REST

**GET /**

Permite consultar el estado del servicio.

**POST /predecir**

Recibe un mensaje en formato JSON y devuelve la clasificación realizada por el modelo.

Ejemplo de solicitud:

```json
{
  "mensaje": "Congratulations! You won a free prize!"
}
```

La respuesta contiene los campos `clasificacion` y `confianza`.

## Evaluación del modelo

El modelo fue evaluado utilizando un conjunto de prueba independiente, equivalente al 20 % de los registros disponibles.

| Métrica | Resultado |
|---|---:|
| Exactitud (Accuracy) | 97.40 % |
| Precisión (Precision) | 100.00 % |
| Sensibilidad (Recall) | 80.54 % |
| F1-Score | 89.22 % |

Los resultados indican un desempeño general favorable, aunque el modelo presenta oportunidades de mejora en la detección de algunos mensajes SPAM.

## Pruebas funcionales

Se realizaron pruebas mediante Swagger UI para verificar la clasificación de mensajes legítimos y no deseados, la validación de entradas vacías, el control de longitud, el procesamiento de caracteres especiales y el comportamiento ante mensajes ambiguos.

Las solicitudes válidas devolvieron respuestas HTTP 200, mientras que las entradas que incumplieron las restricciones de longitud fueron rechazadas con HTTP 422.

## Consideraciones

El modelo fue entrenado principalmente con mensajes en inglés, por lo que su desempeño con otros idiomas no ha sido validado.

El porcentaje de confianza corresponde a la probabilidad estimada por el clasificador y no debe interpretarse como una garantía de clasificación correcta.

## Contexto académico

Proyecto desarrollado como parte de la Fase II de la asignatura Gestión de Proyectos de Inteligencia Artificial de la Maestría en Inteligencia Artificial.

El objetivo es demostrar la integración de componentes de software, la contenerización mediante Docker, la validación funcional y la documentación de una solución basada en Inteligencia Artificial.
