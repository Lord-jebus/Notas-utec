$(document).ready(function() {    
    function dropdown(e) { // Función para controlar el desplegable del menú
        var $el = e.data.el;
        $this = $(this),
        $next = $this.next();
        
        $next.slideToggle(); // Si estaba oculto, se desplegará; si estaba desplegado, se ocultará
        $this.parent().toggleClass('open');
        
        if (!e.data.multiple) {
            $el.find('.submenu').not($next).slideUp().parent().removeClass('open');
        }
    }
    
    var $accordion = $('#accordion');
    var $desplegables = $accordion.find('.desplegable');
    
    $desplegables.on('click', { el: $accordion, multiple: false }, dropdown);
    
    const plan2023Div = document.querySelector('.plan2023Struct');
    const mostrarPlanButton = document.getElementById('mostrarPlan'); // Obtengo el boton mostrarPlan
    mostrarPlanButton.addEventListener('click', function() {
        const materias = [];
        const radioButtons = document.querySelectorAll("input[type='radio']:checked");
        var btn_titulo_intermedio = document.getElementById('btn_contenedor');
        var isPresionado = btn_titulo_intermedio.classList.contains('seleccionado'); // Verificar si el botón está activado o desactivado
        var i=0;
        
        radioButtons.forEach(function(radioButton) {
            const estado = parseInt(radioButton.value); // Convertir el valor a entero
            i++;
            if(isPresionado && i<=36){ // Las primeras 36 materias son correspondientes al título intermedio
                console.log("prueba");
                materias.push(1);
            }else{
                materias.push(estado); // Agregar el estado al vector
            }
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
                materiaDivs.forEach(function(materiaDiv, index_materia) {
                    const estado = response[index_materia];
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

                    if(isPresionado && ((index_materia == 17) || (index_materia == 20) || 
                    (index_materia == 30) || (index_materia == 34) || (index_materia == 35))){ // Si se presionó que tiene el título, debe también exonerar las materias..
                        // Dinámica y estática = 17 , P3 = 20, Pocesos de fabricación = 30, HYN = 34, Automatización de procesos industriales = 35. 
                        materiaDiv.classList.add("aprobada");
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

function toggleEgresoIntermedio() {
    var btn_titulo_intermedio = document.getElementById('btn_contenedor');
    var isPresionado = btn_titulo_intermedio.classList.contains('seleccionado'); // Verificar si el botón está activado o desactivado
    btn_titulo_intermedio.classList.toggle('seleccionado'); // Alternar la clase 'seleccionado' 
    egresoIntermiedio(isPresionado);
}

function egresoIntermiedio(isPresionado) { 
    const desplegables = document.querySelectorAll(".desplegable");
    
    desplegables.forEach(function(desplegable, index_semestre){
        if(index_semestre<6){ // Los primeros 6 semestres son respectivos al titulo intermedio.
            var flecha_abajo = desplegable.querySelector('.fa-chevron-down');
            var guion = desplegable.querySelector('.fa-minus');
            var numero = desplegable.querySelector('.fa-solid');
            
            if (isPresionado) {
                flecha_abajo.classList.remove('inhabilitado');
                guion.classList.remove('inhabilitado');
                numero.classList.remove('inhabilitado');
                desplegable.classList.remove('inhabilitado');
            } else {
                flecha_abajo.classList.add('inhabilitado');
                guion.classList.add('inhabilitado');
                numero.classList.add('inhabilitado');
                desplegable.classList.add('inhabilitado');
            }        
        }
    }); 
}