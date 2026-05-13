// BOTÓN Y ELEMENTOS DEL HTML
const btnConsultar = document.getElementById("btnConsultar");
const departamento = document.getElementById("departamento");

const temperatura = document.getElementById("temperatura");
const estado = document.getElementById("estado");
const precipitacion = document.getElementById("precipitacion");
const recomendacion = document.getElementById("recomendacion");
const contenedorPronostico = document.getElementById("contenedorPronostico");
const aqi = document.getElementById("aqi");
const estadoAire = document.getElementById("estadoAire");
const recomendacionAire = document.getElementById("recomendacionAire");
const iconoClima = document.getElementById("iconoClima");

const fechaActual = document.getElementById("fechaActual");
const horaActual = document.getElementById("horaActual");

const velocidadViento = document.getElementById("velocidadViento");
const direccionViento = document.getElementById("direccionViento");


// COORDENADAS DE LOS 14 DEPARTAMENTOS
const coordenadasDepartamentos = {
    "Ahuachapán": { lat: 13.9214, lon: -89.8450 },
    "Cabañas": { lat: 13.8648, lon: -88.7494 },
    "Chalatenango": { lat: 14.0333, lon: -88.9333 },
    "Cuscatlán": { lat: 13.7167, lon: -89.1167 },
    "La Libertad": { lat: 13.4883, lon: -89.3222 },
    "La Paz": { lat: 13.4833, lon: -88.9667 },
    "La Unión": { lat: 13.3369, lon: -87.8439 },
    "Morazán": { lat: 13.7681, lon: -88.1291 },
    "San Miguel": { lat: 13.4833, lon: -88.1833 },
    "San Salvador": { lat: 13.6929, lon: -89.2182 },
    "San Vicente": { lat: 13.6333, lon: -88.8000 },
    "Santa Ana": { lat: 13.9942, lon: -89.5597 },
    "Sonsonate": { lat: 13.7189, lon: -89.7242 },
    "Usulután": { lat: 13.3500, lon: -88.4500 }
};


// EVENTO DEL BOTÓN CON API REAL
btnConsultar.addEventListener("click", async () => {

    const deptoSeleccionado = departamento.value;

    const { lat, lon } = coordenadasDepartamentos[deptoSeleccionado];

    const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current=temperature_2m,precipitation_probability,weather_code,wind_speed_10m,wind_direction_10m&daily=temperature_2m_max,weather_code,precipitation_probability_max&timezone=auto`;

    try {

        const respuesta = await fetch(url);
        const data = await respuesta.json();

        const tempC = data.current.temperature_2m;
        const tempF = (tempC * 9 / 5) + 32;
        const lluvia = data.current.precipitation_probability;
        const codigoClima = data.current.weather_code;

        const velocidad = data.current.wind_speed_10m;
        const direccion = data.current.wind_direction_10m;

        const clima = traducirClima(codigoClima);

        if (clima === "Despejado") {
            iconoClima.src = "assets/soleado.png";
        }
        else if (clima === "Parcialmente Nublado") {
            iconoClima.src = "assets/nublado.png";
        }
        else if (clima === "Lluvia") {
            iconoClima.src = "assets/lluvia.png";
        }
        else if (clima === "Tormenta") {
            iconoClima.src = "assets/lluvia.png";
        }
        else if (clima === "Niebla") {
            iconoClima.src = "assets/nublado.png";
        }
        else {
            iconoClima.src = "assets/nublado.png";
        }

        temperatura.textContent = `Temperatura: ${tempC}°C / ${tempF.toFixed(1)}°F`;
        estado.textContent = `Estado: ${clima}`;
        precipitacion.textContent = `Precipitación: ${lluvia}%`;
        velocidadViento.textContent = `Velocidad del viento: ${velocidad} km/h`;
        direccionViento.textContent = `Dirección del viento: ${obtenerDireccionViento(direccion)}`;

        if (clima === "Tormenta") {

            recomendacion.textContent =
                "Recomendación: Evitar actividades al aire libre por tormentas ⛈️.";

        }
        else if (clima === "Lluvia") {

            recomendacion.textContent =
                "Recomendación: Llevar paraguas y tomar precauciones 🌧️.";

        }
        else if (clima === "Neblina") {

            recomendacion.textContent =
                "Recomendación: Conduzca con precaución 🌫️.";

        }
        else if (
            clima === "Nublado" &&
            lluvia > 40
        ) {

            recomendacion.textContent =
                "Recomendación: Con precaución ante posible lluvias 🌧️.";

        }
        else if (
            clima === "Nublado" &&
            lluvia <= 40
        ) {

            recomendacion.textContent =
                "Recomendación: Clima favorable para actividades exteriores.";

        }

        else {

            recomendacion.textContent =
                "Recomendación: Clima favorable para actividades exteriores ☀️.";

        }

        const urlAire = `https://air-quality-api.open-meteo.com/v1/air-quality?latitude=${lat}&longitude=${lon}&current=us_aqi`;

        const respuestaAire = await fetch(urlAire);
        const dataAire = await respuestaAire.json();

        const valorAQI = dataAire.current.us_aqi;

        aqi.textContent = `AQI: ${valorAQI}`;

        if (valorAQI <= 50) {
            estadoAire.textContent = "Estado: Buena";
            recomendacionAire.textContent = "Recomendación: Aire limpio, ideal para actividades al aire libre.";
        }
        else if (valorAQI <= 100) {
            estadoAire.textContent = "Estado: Moderada";
            recomendacionAire.textContent = "Recomendación: Calidad aceptable, personas sensibles con precaución.";
        }
        else if (valorAQI <= 150) {
            estadoAire.textContent = "Estado: Dañina para grupos sensibles";
            recomendacionAire.textContent = "Recomendación: Personas sensibles deben limitar actividad exterior.";
        }
        else {
            estadoAire.textContent = "Estado: Mala";
            recomendacionAire.textContent = "Recomendación: Reducir actividades al aire libre.";
        }

        contenedorPronostico.innerHTML = "";

        for (let i = 0; i < 6; i++) {
            const tempDia = data.daily.temperature_2m_max[i];
            const climaDia = traducirClima(data.daily.weather_code[i]);
            const lluviaDia = data.daily.precipitation_probability_max[i];

            contenedorPronostico.innerHTML += `
                <div class="dia-pronostico">
                    <span>${obtenerNombreDia(i)}</span>
                    <span>${tempDia}°C - ${climaDia} ${obtenerEmojiClima(climaDia)}</span>
                    <span>Precipitación: ${lluviaDia}%</span>
                </div>
            `;
        }

    } catch (error) {
        console.error("Error al obtener clima:", error);

        temperatura.textContent = "Error al cargar datos.";
        estado.textContent = "--";
        precipitacion.textContent = "--";
        recomendacion.textContent = "--";
    }

});

function obtenerEmojiClima(clima) {

    if (clima === "Despejado") {
        return "☀️";
    }
    else if (clima === "Parcialmente Nublado") {
        return "⛅";
    }
    else if (clima === "Nublado") {
        return "☁️";
    }
    else if (clima === "Lluvia") {
        return "🌧️";
    }
    else if (clima === "Tormenta") {
        return "⛈️";
    }
    else if (clima === "Neblina") {
        return "🌫️";
    }
    else {
        return "❓";
    }

}

function obtenerNombreDia(offset) {
    const dias = [
        "Domingo",
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado"
    ];

    const hoy = new Date().getDay();

    return dias[(hoy + offset + 1) % 7];
}

function actualizarFechaHora() {
    const ahora = new Date();

    const opcionesFecha = {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric"
    };

    fechaActual.textContent = "Fecha: " + ahora.toLocaleDateString("es-ES", opcionesFecha);
    horaActual.textContent = "Hora: " + ahora.toLocaleTimeString();
}

function obtenerDireccionViento(grados) {

    if (grados >= 337 || grados < 22) {
        return "Norte";
    }
    else if (grados < 67) {
        return "Noreste";
    }
    else if (grados < 112) {
        return "Este";
    }
    else if (grados < 157) {
        return "Sureste";
    }
    else if (grados < 202) {
        return "Sur";
    }
    else if (grados < 247) {
        return "Suroeste";
    }
    else if (grados < 292) {
        return "Oeste";
    }
    else {
        return "Noroeste";
    }

}


// FUNCIÓN PARA TRADUCIR CÓDIGOS DEL CLIMA
function traducirClima(codigo) {

    if (codigo === 0) {
        return "Despejado";
    }

    else if (codigo >= 1 && codigo <= 3) {
        return "Parcialmente Nublado";
    }

    else if (codigo >= 45 && codigo <= 48) {
        return "Neblina";
    }

    else if (codigo >= 51 && codigo <= 57) {
        return "Nublado";
    }

    else if (codigo >= 61 && codigo <= 82) {
        return "Lluvia";
    }

    else if (codigo >= 95 && codigo <= 99) {
        return "Tormenta";
    }

    else {
        return "Clima desconocido";
    }

}

actualizarFechaHora();
setInterval(actualizarFechaHora, 1000);
