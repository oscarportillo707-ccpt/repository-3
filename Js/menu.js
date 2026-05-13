const hamburguesa = document.getElementById("hamburguesa");
const menu = document.getElementById("menu");

if (hamburguesa) {

    hamburguesa.addEventListener("click", () => {

        menu.classList.toggle("oculto");

    });

}

const elementosAnimados =
    document.querySelectorAll(".animada-derecha, .animada-izquierda");

function mostrarScroll() {

    elementosAnimados.forEach((elemento) => {

        const posicion =
            elemento.getBoundingClientRect().top;

        const tamañoPantalla =
            window.innerHeight;

        if (posicion < tamañoPantalla - 100) {

            elemento.classList.add("mostrar");

        }

        else {

            elemento.classList.remove("mostrar");

        }

    });

}

window.addEventListener("scroll", mostrarScroll);

mostrarScroll();