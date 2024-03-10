$(document).ready(function() { 
    //$('#mostrarPlan').on('click', function() {
        
    function dropdown(e) { // Función para controlar el desplegable del menú  
        var $el = e.data.el;
        $this = $(this),
        $next = $this.next();

        $next.slideToggle();
        $this.parent().toggleClass('open');

        if (!e.data.multiple) {
            $el.find('.submenu').not($next).slideUp().parent().removeClass('open');
        }
    }

    var $accordion = $('#accordion');
    var $links = $accordion.find('.link');

    $links.on('click', { el: $accordion, multiple: false }, dropdown);

    const plan2023Div = document.querySelector('.plan2023Struct');
    const mostrarPlanButton = document.getElementById('mostrarPlan'); // Obtengo el boton mostrarPlan
    mostrarPlanButton.addEventListener('click', function() { 
        const materias = [];
        const radioButtons = document.querySelectorAll("input[type='radio']:checked");

        radioButtons.forEach(function(radioButton) {
            const estado = parseInt(radioButton.value); // Convertir el valor a entero
            materias.push(estado); // Agregar el estado al vector
        });

        if (plan2023Div.classList.contains('hidden')) {
            plan2023Div.classList.remove('hidden');
        }
        const url = 'http://3.18.181.47/api2/consultaMaterias';
        // Envio al back end el vector de materias con la información de estados.
        $.ajax({
            type: 'POST',
            url: url,
            contentType: 'application/json', 
            data: JSON.stringify({estados: materias}),  // Enviar el array como JSON 
            success: function(response) {
                console.log(response);
                const materiaDivs = document.querySelectorAll(".plan2023 .child");
                materiaDivs.forEach(function(materiaDiv, index) {
                    const estado = response[index];
                    materiaDiv.classList.remove("pendiente", "aprobada", "examen", "tutoria");
                    
                    if (estado === 0) {
                        materiaDiv.classList.add("pendiente");
                    } else if (estado === 1) {
                        materiaDiv.classList.add("aprobada");
                    } else if (estado === 2) {
                        materiaDiv.classList.add("examen");
                    } else if (estado === 3) {
                        materiaDiv.classList.add("tutoria");
                    }
                });
            },
            
            error: function(error) {
                console.error('Error al enviar los estados al servidor:', error);
            }
        });    
    });

    $('input[type="radio"]').prop('checked', false); // Desmarcar todos los radios
    $('input[value="0"]').prop('checked', true); // Marcar los radios con valor 0 (Pendiente)
});

    /*
    if (topic === topicToSubscribe) {
        const receivedMessage = JSON.parse(message.toString());

        // Crea un DOM virtual con jsdom para cambiar los colores/estados de cada materia 2023
        const dom = new JSDOM(`<!DOCTYPE html><html><body></body></html>`);
        const document = dom.window.document;
        const materiaDivs = document.querySelectorAll(".plan2023 .child");


        // Seleccionar y modificar los elementos del DOM virtual
        for (let i = 0; i < receivedMessage.length; i++) {
            const estado = receivedMessage[i];

            if (estado === 0) {
                materiaDivs[i].classList.add("pendiente");
            } else if (estado === 1) {
                materiaDivs[i].classList.add("aprobada");
            } else if (estado === 2) {
                materiaDivs[i].classList.add("examen");
            } else if (estado === 3) {
                materiaDivs[i].classList.add("tutoria");
            }
        }

        // Convertir el DOM virtual a una cadena HTML modificada
        const modifiedHtml = dom.serialize();

        // Aquí puedes enviar o utilizar modifiedHtml según tus necesidades
        console.log(modifiedHtml);
    }*/