
const botonAnalizar = document.getElementById("botonAnalizar");
const campoMensaje = document.getElementById("mensaje");
const contenedorResultado = document.getElementById("resultado");

botonAnalizar.addEventListener("click", async () => {
    const mensaje = campoMensaje.value.trim();

    if (mensaje === "") {
        contenedorResultado.textContent =
            "Por favor, escribe un mensaje.";
        return;
    }

    contenedorResultado.textContent = "Analizando mensaje...";
    botonAnalizar.disabled = true;

    try {
        const respuesta = await fetch(
            "http://localhost:8000/predecir",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ mensaje: mensaje })
            }
        );

        if (!respuesta.ok) {
            throw new Error("Error al analizar el mensaje");
        }

        const datos = await respuesta.json();

        contenedorResultado.textContent =
            "Clasificación: " + datos.clasificacion;

    } catch (error) {
        contenedorResultado.textContent =
            "No fue posible conectar con el servidor.";
        console.error(error);
    } finally {
        botonAnalizar.disabled = false;
    }
});

