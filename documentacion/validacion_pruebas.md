# Validación y pruebas del Detector Inteligente de SPAM

## 1. Introducción

La validación de una solución basada en Inteligencia Artificial constituye una etapa fundamental para comprobar su funcionamiento, identificar posibles errores y determinar si cumple con los objetivos establecidos.

En este proyecto realizamos pruebas sobre el modelo de clasificación Naive Bayes y sobre la API REST desarrollada mediante FastAPI. Nuestro propósito fue evaluar tanto la capacidad predictiva del modelo como el comportamiento de la aplicación ante diferentes condiciones de entrada.

Las pruebas se realizaron utilizando Google Colab durante el entrenamiento y Swagger UI durante la ejecución local de la aplicación contenerizada mediante Docker.

## 2. Objetivo de las pruebas

El objetivo principal fue verificar que nuestra aplicación pudiera recibir mensajes de texto, procesarlos mediante TF-IDF y clasificarlos correctamente como SPAM o NO SPAM.

Asimismo, buscamos comprobar que la API gestionara adecuadamente las entradas inválidas y mantuviera su funcionamiento ante mensajes extensos, caracteres especiales y contenido ambiguo.

## 3. Evaluación del modelo de Inteligencia Artificial

Para evaluar el modelo utilizamos un conjunto de prueba independiente equivalente al 20 % de los datos disponibles.

Las métricas obtenidas fueron:

| Métrica | Resultado |
|---|---:|
| Exactitud (Accuracy) | 97.40 % |
| Precisión (Precision) | 100.00 % |
| Sensibilidad (Recall) | 80.54 % |
| F1-Score | 89.22 % |

Los resultados muestran que nuestro modelo alcanza una exactitud del 97.40 %, lo que representa un desempeño general favorable. La precisión del 100 % indica que, dentro del conjunto evaluado, los mensajes identificados como SPAM realmente pertenecían a esa categoría.

Sin embargo, la sensibilidad del 80.54 % evidencia que aproximadamente el 19.46 % de los mensajes SPAM no fueron detectados correctamente.

Esto nos permite identificar una oportunidad de mejora relacionada con la reducción de falsos negativos.

## 4. Análisis de la matriz de confusión

La matriz de confusión permitió identificar los siguientes resultados:

| Clasificación real | Predicción NO SPAM | Predicción SPAM |
|---|---:|---:|
| NO SPAM | 966 | 0 |
| SPAM | 29 | 120 |

Observamos que el modelo clasificó correctamente 966 mensajes legítimos y 120 mensajes SPAM. No se registraron falsos positivos, mientras que 29 mensajes SPAM fueron clasificados incorrectamente como NO SPAM.

Estos resultados confirman que el algoritmo presenta una capacidad favorable para evitar falsas alarmas, aunque todavía puede mejorar su sensibilidad para detectar mensajes no deseados.

[Imagen 1. Matriz de confusión generada durante la evaluación del modelo en Google Colab.]

## 5. Pruebas funcionales de la API REST

Para validar el funcionamiento de nuestra API utilizamos Swagger UI, disponible mediante el endpoint `/docs`.

Las pruebas consistieron en enviar solicitudes HTTP POST al endpoint `/predecir`, utilizando mensajes en formato JSON.

El backend recibió las solicitudes, validó su contenido y devolvió las clasificaciones generadas por nuestro modelo.

Los resultados fueron:

| Caso | Código HTTP | Clasificación | Confianza |
|---|---:|---|---:|
| Mensaje SPAM | 200 | SPAM | 96.70 % |
| Mensaje NO SPAM | 200 | NO SPAM | 98.40 % |
| Mensaje vacío | 422 | Rechazado | No aplica |
| Mensaje superior a 5,000 caracteres | 422 | Rechazado | No aplica |
| Caracteres especiales | 200 | SPAM | 94.73 % |
| Mensaje ambiguo | 200 | NO SPAM | 96.06 % |

Estas pruebas permitieron comprobar la comunicación entre la API y el modelo, así como el comportamiento del sistema ante diferentes tipos de información.

## 6. Evaluación de casos extremos

### 6.1. Mensaje vacío

Enviamos una solicitud con el campo `mensaje` vacío.

```json
{
  "mensaje": ""
}
```

La API respondió con el código HTTP 422, indicando que el texto no cumplía con la longitud mínima establecida.

Esto demuestra que el mecanismo de validación impide procesar mensajes sin contenido.

### 6.2. Mensaje excesivamente largo

Enviamos un mensaje que superaba los 5,000 caracteres permitidos.

La API respondió con HTTP 422 y un mensaje indicando que la cadena excedía la longitud máxima.

Esta validación permite establecer límites sobre el tamaño de las solicitudes recibidas.

### 6.3. Mensaje con caracteres especiales

Evaluamos el siguiente mensaje:

```text
FREE $$$ PRIZE!!! 🎉🎁 Claim NOW!!! @#$% 12345
```

El modelo clasificó el mensaje como SPAM con una confianza estimada del 94.73 %.

Esto demuestra que la aplicación puede procesar mensajes que contienen símbolos, números y caracteres especiales sin generar errores durante la solicitud.

### 6.4. Mensaje ambiguo

Evaluamos un mensaje que combinaba expresiones promocionales con lenguaje cotidiano:

```text
Hi, I have a free gift for you. Can we meet tomorrow to discuss it?
```

El modelo clasificó el mensaje como NO SPAM con una confianza estimada del 96.06 %.

Este resultado evidencia que el algoritmo puede generar predicciones ante mensajes con características mixtas. Sin embargo, la clasificación debe interpretarse con precaución, ya que una probabilidad elevada no garantiza que el mensaje sea legítimo.

## 7. Validación de la integración técnica

Además de las pruebas del modelo, verificamos la comunicación entre los componentes de nuestra aplicación.

El frontend permitió introducir mensajes desde el navegador y enviarlos al backend mediante solicitudes HTTP POST.

FastAPI procesó las solicitudes utilizando el vectorizador TF-IDF y el modelo Naive Bayes, devolviendo respuestas JSON con la clasificación y el porcentaje de confianza.

Posteriormente, JavaScript presentó los resultados mediante cuadros de colores: rojo para SPAM y verde para NO SPAM.

También comprobamos que la aplicación podía ejecutarse dentro de un contenedor Docker y accederse localmente desde:

http://localhost:8080/aplicacion

Estas pruebas proporcionan evidencia de la integración funcional entre la interfaz web, la API REST y el modelo de Inteligencia Artificial.

[Imagen 2. Aplicación web ejecutándose dentro de Docker y mostrando la clasificación de un mensaje.]

[Imagen 3. Swagger UI mostrando una solicitud POST /predecir con respuesta HTTP 200.]

## 8. Limitaciones identificadas

Durante las pruebas identificamos algunas limitaciones relevantes.

En primer lugar, el modelo fue entrenado principalmente con mensajes en inglés, por lo que su rendimiento con textos en español no ha sido evaluado suficientemente.

Asimismo, la sensibilidad del 80.54 % indica que algunos mensajes SPAM pueden clasificarse incorrectamente como legítimos.

Finalmente, las probabilidades generadas por el clasificador representan estimaciones estadísticas y no deben interpretarse como garantías absolutas de clasificación correcta.

Estas consideraciones son importantes para comprender el alcance de nuestra solución y establecer posibles mejoras futuras.

## 9. Conclusiones

Las pruebas realizadas permitieron comprobar el funcionamiento de nuestro Detector Inteligente de SPAM desde dos perspectivas: el desempeño predictivo del modelo y la integración técnica de la aplicación.

El modelo Naive Bayes alcanzó una exactitud del 97.40 % y una puntuación F1 del 89.22 % para la categoría SPAM, demostrando un comportamiento favorable dentro del conjunto de evaluación.

Por otra parte, las pruebas funcionales confirmaron que FastAPI recibe y procesa solicitudes válidas, mientras que las entradas que incumplen las restricciones de longitud son rechazadas mediante respuestas HTTP 422.

También verificamos la comunicación entre frontend y backend y la ejecución de la aplicación dentro de Docker.

En conjunto, estos resultados demuestran que nuestra solución cumple con los objetivos académicos de integración técnica, contenerización y validación funcional. No obstante, identificamos oportunidades de mejora relacionadas con la sensibilidad del modelo, la evaluación de otros idiomas y la ampliación de las pruebas ante condiciones más diversas.# Validación y pruebas del Detector Inteligente de SPAM
