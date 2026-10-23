
document.addEventListener("DOMContentLoaded", () => {

    const botonAnalizar = document.getElementById("botonAnalizar");
    const campoMensaje = document.getElementById("mensaje");
    const contenedorResultado = document.getElementById("resultado");

    if (!botonAnalizar || !campoMensaje || !contenedorResultado) {
        console.error("No se encontraron los elementos del formulario.");
        return;
    }

    botonAnalizar.addEventListener("click", async () => {

        const mensaje = campoMensaje.value.trim();

        if (!mensaje) {
            contenedorResultado.textContent =
                "Por favor, escribe un mensaje.";
            return;
        }

        contenedorResultado.textContent = "Analizando mensaje...";
        botonAnalizar.disabled = true;

        try {
            const respuesta = await fetch("/predecir", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ mensaje: mensaje })
            });

            if (!respuesta.ok) {
                throw new Error("Error HTTP: " + respuesta.status);
            }

            const datos = await respuesta.json();

            const esSpam = datos.clasificacion === "SPAM";

            contenedorResultado.className = esSpam
                ? "resultado-spam"
                : "resultado-seguro";

            contenedorResultado.textContent = esSpam
                ? "⚠️ Posible mensaje SPAM | Confianza: " + datos.confianza + "%"
                : "✅ Mensaje NO SPAM | Confianza: " + datos.confianza + "%";

        } catch (error) {
            contenedorResultado.textContent =
                "Error al conectar con la API.";
            console.error(error);

        } finally {
            botonAnalizar.disabled = false;
        }
    });

    console.log("Detector de SPAM inicializado correctamente.");
});
