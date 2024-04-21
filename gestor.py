""" 
Las materias que son o egreso serian 
    DINAMICA Y ESTATICA, 
    P3, 
    PROCESS DE FABRICACIPON, 
    HYN, 
    AUTOMATIZACION DE PROCESOS INDUSTRIALES
    
    QUITAR EN TEC DEMATERIALES 22 DINAICA Y MAQUINAS Y VIBRACIONES

    

Descripción
    El obj principal es actualizar el plan de estudios del año 2018 con 57 materias, a 61 materias correspondientes al plan del año 2023.
    Cada materia se encuentra en uno de los siguientes estados: pendiente, aprobada, exámen o tutoría.
    El nuevo plan tiene materias nuevas, suprime antiguas y cambian de nombre otras.
    Las materias que cambian de nombre, tienen una lista de las materias equivalentes del plan 2018.
        Ej: Teoria de circuitos 1 (TDC1) tiene como materias equivalentes a "electricidad_electronica_industrial" y "teoria_de_circuitos".
            1) Para revalidar TDC1 el alumno debe tener aprobadas las dos materias equivalentes.
            2) Si el alumno tiene materias aprobadas y al menos una a exámen, TDC1 toma el estado de Exámen.
            3) Si el alumno tiene materias aprobadas y exámen pero al menos una en estado de tutoría, TDC1 toma el estado de Tutoría.
            4) Si al menos una materia de las equivalentes se encuentra Pendiente, TDC1 toma el estado de Pendiente.

Objetivos 
    1)  Cargar el estado de las materias del plan 2018 (PENDIENTE, APROBADA, EXAMEN, TUTORIA),
        la página web envía una lista con el formato [1, 2, 3, 0.. para cada estado de cada materia.
    2)  Actualizar estado de materias del 2023, en base a materias equivalentes del plan 2018,
        tener en cuenta que nuevas materias pueden resultar en EXAMEN o TUTORIA, deben ser revisadas.
        En la página web se representa PENDIENTE≡GRIS, TUTORIA≡ROJO, EXAMEN≡AMARILLO y APROBADA≡VERDE
    3)  Función que compruebe si una materia del 2023 puede ser cursada en el próximo semestre.
"""

class EstadoMateria:
    PENDIENTE = 0
    APROBADA = 1
    EXAMEN = 2
    TUTORIA = 3
class Materia2023:
    def __init__(self):
        self.semestre = 0
        self.codigo = ""
        self.nombre = ""
        self.materiasEq2018 = [""]
        self.previas_cursadas = [""]
        self.previas_aprobadas = [""]
        self.estado = EstadoMateria.PENDIENTE
class Materia2018:
    def __init__(self):
        self.nombre = ""
        self.estado = EstadoMateria.PENDIENTE
class Alumno:
    def __init__(self):
        self.nombre = "Nombre"
        self.apellido = "Apellido"
        self.ci = 44207503
        self.materias_2023 = [Materia2023() for _ in range(61)]
        self.materias_2018 = [Materia2018() for _ in range(57)]

# Carga de BD
def cargarPlan(bd_txt): # Métodos de carga desde planes20xx.txt 
    plan_cargado = []
    if   bd_txt == 'plan2018.txt':
        with open(bd_txt, 'r') as archivo:
            materia_actual = {}
            
            for linea in archivo:
                linea = linea.strip()
                if linea: 
                    _, nombre_materia  = linea.split(': ', 1)
                    materia_actual['nombre'] = nombre_materia
                    plan_cargado.append(materia_actual)
                    materia_actual = {}
    elif bd_txt == 'plan2023.txt':
        with open(bd_txt, 'r') as archivo:
            materia_actual = {}
            for linea in archivo:
                linea = linea.strip()
                if linea:  # Ignorar saltos de linea
                    clave, valor = linea.split(': ', 1)
                    if clave == 'codigo':
                        materia_actual = {'codigo': valor}
                    elif clave == 'nombre':
                        materia_actual['nombre'] = valor
                    elif clave == 'materiasEq2018':
                        materia_actual['materiasEq2018'] = valor.split(', ')
                    elif clave == 'semestre':
                        materia_actual['semestre'] = int(valor)
                    elif clave == 'previasCursadas':
                        materia_actual['previasCursadas'] = valor.split(', ')
                    elif clave == 'previasAprobadas':
                        materia_actual['previasAprobadas'] = valor.split(', ')
                else:   # En el salto de línea carga la materia al plan y vacia la materia actual
                    plan_cargado.append(materia_actual)
                    materia_actual = {}
    return plan_cargado
def cargarBD(Alumno): # Carga datos de los planes de estudio 
    global unAlumno
    unAlumno = Alumno

    plan_2018 = cargarPlan("plan2018.txt") 
    plan_2023 = cargarPlan("plan2023.txt") 
    
    for i, materia in enumerate(plan_2018): 
        unAlumno.materias_2018[i].nombre = materia['nombre']
    
    for i, materia in enumerate(plan_2023):
        unAlumno.materias_2023[i].nombre = materia['nombre']
        unAlumno.materias_2023[i].codigo = materia['codigo']
        unAlumno.materias_2023[i].semestre = materia['semestre']
        if 'materiasEq2018' in materia:
            unAlumno.materias_2023[i].materiasEq2018 = materia['materiasEq2018']
        if 'previasCursadas' in materia:
            unAlumno.materias_2023[i].previas_cursadas = materia['previasCursadas']
        if 'previasAprobadas' in materia:
            unAlumno.materias_2023[i].previas_aprobadas = materia['previasAprobadas']

def cargarEstados2018(estados_2018): # Objetivo 1, carga los estados de las materias del plan 2018 mediante un POST de la web 
    # Aquí ingresa el formato [1, 2, 3, 0... y los actualiza en cada materia del alumno.
    for estado, materia_2018 in zip(estados_2018, unAlumno.materias_2018):
        materia_2018.estado = estado
def actualizarEstados2023(): #  Objetivo 2, actualiza los estados del plan 2023, en base a materias eq del plan 2018 
    nuevos_estados = []
    for i, unaMateria in enumerate(unAlumno.materias_2023):
        if (unaMateria.materiasEq2018[0]):  # Si la materia tiene equivalentes, controla su nuevo estado 
            nuevo_estado = nuevoEstado(unaMateria)
            unAlumno.materias_2023[i] = nuevo_estado
            nuevos_estados.append(nuevo_estado)
        else:
            unAlumno.materias_2023[i] = EstadoMateria.PENDIENTE
            nuevos_estados.append(EstadoMateria.PENDIENTE)
    return nuevos_estados

def nuevoEstado(unaMateria: Materia2023): # Función auxiliar al objetivo 2 
    estadoNuevo = EstadoMateria.APROBADA # Se presupone que la materia de nuevo plan si se puede revalidar.
    encontreMateria = False # Se presupone que no existe materia previa,
                            # por lo que la materia del plan 2023 es nueva y se debe cursar (PENDIENTE),
                            # por lo tanto encontreMateria = False, hasta que la encuentre.
    
    # Itero todas las materias eq al plan 2018.
    for materia_eq_2018 in unaMateria.materiasEq2018: 
        for materia_2018 in unAlumno.materias_2018: 
            if unaMateria.codigo == 'PFTM':
                print(f"Materia2023: {unaMateria.nombre}, {materia_2018.nombre} ={materia_2018.estado} ")
            
            if materia_eq_2018 in materia_2018.nombre:
                encontreMateria = True
                if materia_eq_2018 == materia_2018.nombre:
                    if materia_2018.estado == EstadoMateria.EXAMEN:
                        """ Cómo TUTORIA es el peor caso, hay que tomar esa excepción.. 
                            Si se tienen 1=APROBADA, 1=EXAMEN, 1=TUTORIA 
                            -> estado de nueva materia = TOTURIA. """
                        if estadoNuevo != EstadoMateria.TUTORIA:
                            estadoNuevo = EstadoMateria.EXAMEN
                    elif materia_2018.estado == EstadoMateria.TUTORIA:
                        estadoNuevo = EstadoMateria.TUTORIA
                    elif materia_2018.estado == EstadoMateria.PENDIENTE:
                        """ Si alguna materia eq del plan 2018 se encuentra pendiente.. 
                            la correspondiente al plan 2023 tendrá el mismo estado,
                            sin importar el estado del resto de mateiras eq. """
                        estadoNuevo = EstadoMateria.PENDIENTE
    # Verifica si la materia es nueva.
    if not encontreMateria:
        return EstadoMateria.PENDIENTE
    
    return estadoNuevo
def puedeCursarMateria(unaMateriaf: Materia2023): # Objetivo 3, comprobar si puede cursar X nueva materia 
    for previa_aprobada in unaMateria.previas_aprobadas:
        if previa_aprobada: # Verifica exista al menos una materia aprovada para luego confirmar
            for materia_2023 in unAlumno.materias_2023:
                if previa_aprobada == materia_2023.codigo and materia_2023.estado != EstadoMateria.APROBADA:
                    return False
    
    for previa_cursada in unaMateria.previas_cursadas:
        if previa_cursada: # Verifica exista al menos una materia cursada para luego confirmar
            for materia_2023 in unAlumno.materias_2023:
                # En caso de que la materia previa se encuentre en estado EXAMEN, se asume cómo cursada
                if previa_cursada == materia_2023.codigo and materia_2023.estado not in [EstadoMateria.EXAMEN, EstadoMateria.APROBADA]:
                    return False
    
    return True

# Auxiliares
def mostrarAlumno():
    print(f'Nombre: {unAlumno.nombre}')
    print(f'Apellido: {unAlumno.apellido}')
    print(f'CI: {unAlumno.ci}')
def mostrarEstados2018():
    print("###############################################")
    print("Materias 2018")
    for materia in unAlumno.materias_2018:
        print(f"{materia.nombre}: {materia.estado}")
    print("###############################################")
def mostrarEstados2023():
    print("###############################################")
    print("Materias 2023")
    for materia in unAlumno.materias_2023:
        print(f"    {materia.nombre}: {materia.estado}")
    print("###############################################")
