""" 
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
        self.nombre = "Ramiro"
        self.apellido = "Vazquez"
        self.ci = 44207503
        self.materias_2023 = [Materia2023() for _ in range(61)]
        self.materias_2018 = [Materia2018() for _ in range(57)]
#unAlumno = Alumno()        

def plan2018(): # BD materias del plan 2018 
    plan2018 = [
            # S1 - 5 materias
            { 'nombre': "matematica_1" },
            { 'nombre': "electricidad_electronica_industrial" },
            { 'nombre': "introduccion_a_la_mecatronica" },
            { 'nombre': "fisica" },
            { 'nombre': "quimica" },
            # S2 - 6 materias
            { 'nombre': "matematica_2" },
            { 'nombre': "mecanica_aplicada_a_maquinas" },
            { 'nombre': "termodinamica" },
            { 'nombre': "ciencia_de_los_materiales" },
            { 'nombre': "teoria_de_circuitos" },
            { 'nombre': "proyecto_1" },
            # S3 - 7 materias
            { 'nombre': "matematica_3" },
            { 'nombre': "diseño_logico" },
            { 'nombre': "electromagnetismo" },
            { 'nombre': "electronica_aplicada" },
            { 'nombre': "cad" },
            { 'nombre': "programacion_1" },
            { 'nombre': "proyecto_2" },
            # S4 - 6 materias
            { 'nombre': "seguridad_laboral" },
            { 'nombre': "microcontroladores" },
            { 'nombre': "programacion_2" },
            { 'nombre': "intrumentacion" },
            { 'nombre': "costos" },
            { 'nombre': "proyecto_3" },
            # S5 - 6 materias
            { 'nombre': "introduccion_a_control" },
            { 'nombre': "maquinas_electricas" },
            { 'nombre': "mecatronica" },
            { 'nombre': "hidraulica_1" },
            { 'nombre': "gestion" },
            { 'nombre': "proyecto_4" },
            # S6 - 6 materias
            { 'nombre': "proyecto_tecnologo" },
            { 'nombre': "ppt" },
            { 'nombre': "tecnologia_de_control_y_robotica" },
            { 'nombre': "tecnicas_digitales" },
            { 'nombre': "legislacion_laboral" },
            { 'nombre': "comunicacion_profesional" },
            # S7 - 5 materias
            { 'nombre': "matematica_4" },
            { 'nombre': "metalurgica_fisica" },
            { 'nombre': "electronica_de_potencia" },
            { 'nombre': "mecanica" },
            { 'nombre': "programacion_3" },
            # S8 - 5 materias
            { 'nombre': "metodos_numericos" },
            { 'nombre': "dinamica_y_vibraciones" },
            { 'nombre': "sistemas_de_control_aplicados" },
            { 'nombre': "programacion_4" },
            { 'nombre': "hidraulica_2" },
            # S9 - 6 materias
            { 'nombre': "fenomenos_de_transporte" },
            { 'nombre': "manufactura_asistida" },
            { 'nombre': "procesos_de_fabricacion" },
            { 'nombre': "probabilidad_y_estadistica" },
            { 'nombre': "conversion_de_energia" },
            { 'nombre': "anteproyecto_de_ing" },
            # S10 - 5 materias
            { 'nombre': "gestion_de_calidad" },
            { 'nombre': "gestion_ambiental" },
            { 'nombre': "mecatronica_avanzada" },
            { 'nombre': "practicas_profesionales" },
            { 'nombre': "proyecto_final_ing" }
        ]
    return plan2018

def plan2023(): # BD materias del plan 2023 
    plan_2023 = [ 
        # S1 - 6 materias
        { # COES 
            'codigo': "COES", 
            'nombre': "Comunicacion oral y escrita", 
            'materiasEq2018': ["comunicacion_profesional"], 
            'semestre': 1
        },
        { # PRG1 
            'codigo': "PRG1", 
            'nombre': "Programacion 1", 
            'materiasEq2018': ["programacion_1"], 
            'semestre': 1
        },
        { # TDC1 
            'codigo': "TDC1", 
            'nombre': "Teoria de circuitos 1", 
            'materiasEq2018': ["electricidad_electronica_industrial", "teoria_de_circuitos"], 
            'semestre': 1
        },
        { # MAT1 
            'codigo': "MAT1", 
            'nombre': "Matematica 1", 
            'materiasEq2018': ["matematica_1"], 
            'semestre': 1
        },
        { # QMCA 
            'codigo': "QMCA", 
            'nombre': "Quimica", 
            'materiasEq2018': ["quimica"], 
            'semestre': 1
        },
        { # INTM 
            'codigo': "INTM", 
            'nombre': "Introducción a la mecatrónica", 
            'materiasEq2018': ["introduccion_a_la_mecatronica"], 
            'semestre': 1
        },
        #  S2 - 7 materias
        { # MAT2 
            'codigo': "MAT2", 
            'nombre': "Matematica 2", 
            'previasCursadas': ["MAT1"], 
            'materiasEq2018': ["matematica_2"], 
            'semestre': 2
        },
        { # FMIN 
            'codigo': "FMIN", 
            'nombre': "Fundamentos matematicos con informatica", 
            'previasCursadas': ["PRG1", "MAT1"], 
            'materiasEq2018': ["matematica_1", "matematica_2", "matematica_3", "programacion_1", "programacion_2"], 
            'semestre': 2
        },
        { # TDC2 
            'codigo': "TDC2", 
            'nombre': "Teorica de circuitos 2", 
            'previasCursadas': ["TDC1"], 
            'materiasEq2018': ["teoria_de_circuitos", "electronica_aplicada"], 
            'semestre': 2
        },
        { # FIS1 
            'codigo': "FIS1", 
            'nombre': "Fisica 1", 'previasCursadas': ["MAT1"], 
            'materiasEq2018': ["fisica"], 
            'semestre': 2
        },
        { # TDM1 
            'codigo': "TDM1", 
            'nombre': "Tecnologias de materiales 1", 
            'previasCursadas': ["QMCA"], 
            'materiasEq2018': ["ciencia_de_los_materiales"], 
            'semestre': 2
        },
        { # DCAD 
            'codigo': "DCAD", 
            'nombre': "Dibujo computarizado (CAD)", 
            'previasCursadas': ["INTM"], 
            'materiasEq2018': ["cad"], 
            'semestre': 2
        },
        { # PIC1 
            'codigo': "PIC1", 
            'nombre': "Proyecto integrador de competencias 1", 
            'previasCursadas': ["COES", "PRG1", "TDC1", "MAT1", "QMCA"], 
            'previasAprobadas': ["INTM"], 
            'materiasEq2018': ["proyecto_1", "proyecto_2"], 
            'semestre': 2
        },
        #  S3 - 6 materias
        { # MAT3 
            'codigo': "MAT3", 
            'nombre': "Matematica 3", 
            'previasCursadas': ["MAT2"], 
            'previasAprobadas': ["MAT1"], 
            'materiasEq2018': ["matematica_3"], 
            'semestre': 3
        },
        { # PRG2 
            'codigo': "PRG2", 
            'nombre': "Programacion 2", 
            'previasCursadas': ["PRG1"], 
            'previasAprobadas': ["MAT2"], 
            'materiasEq2018': ["programacion_2"], 
            'semestre': 3
        },
        { # EALG 
            'codigo': "EALG", 
            'nombre': "Electronica analogica aplicada", 
            'previasCursadas': ["TDC2","FIS1","MAT2"], 
            'previasAprobadas': ["MAT1","TDC1"], 
            'materiasEq2018': ["teoria_de_circuitos", "electronica_aplicada"], 
            'semestre': 3
        },
        { # SLSO 
            'codigo': "SLSO", 
            'nombre': "Seguridad laboral y salud ocupacional", 
            'previasAprobadas': ["COES","PRG1","TDC1","MAT1","QMCA","INTM"], 
            'materiasEq2018': ["seguridad_laboral"], 
            'semestre': 3
        },
        { # DIES 
            'codigo': "DIES", 
            'nombre': "Dinamica y estatica", 
            'previasCursadas': ["FIS1"], 
            'previasAprobadas': ["INTM"], 
            'materiasEq2018': ["mecanica_aplicada_a_maquinas", "mecanica"], 
            'semestre': 3
        },
        { # EDG1 
            'codigo': "EDG1", 
            'nombre': "Electronica digital 1", 
            'previasCursadas': ["FMIN"], 
            'previasAprobadas': ["TDC1"], 
            'materiasEq2018': ["diseño_logico"], 
            'semestre': 3
        },
        #  S4 - 6 materias
        { # TMPR 
            'codigo': "TMPR", 
            'nombre': "Tecnologias de microprocesamiento", 
            'previasCursadas': ["EDG1"], 
            'previasAprobadas': ["FMIN"], 
            'materiasEq2018': ["microcontroladores"], 
            'semestre': 4
        },
        { # PRG3 
            'codigo': "PRG3", 
            'nombre': "Programacion 3", 
            'previasCursadas': ["PRG1", "MAT1"], 
            'materiasEq2018': ["programacion_3"], 
            'semestre': 4
        },
        { # MEM1 
            'codigo': "MEM1", 
            'nombre': "Materiales y elementos de máquinas", 
            'previasCursadas': ["DIES"], 
            'previasAprobadas': ["FMIN"], 
            'materiasEq2018': ["mecanica_aplicada_a_maquinas", "cinecia_de_los_materiales"], 
            'semestre': 4
        },
        { # FIS2 
            'codigo': "FIS2", 
            'nombre': "Fisica 2 (Electromagnetismo)", 
            'previasAprobadas': ["MAT1", "FMIN", "FIS1"], 
            'materiasEq2018': ["electromagnetismo"], 
            'semestre': 4
        },
        { # AEIN 
            'codigo': "AEIN", 
            'nombre': "Aplicaciones electro industriales", 
            'previasCursadas': ["EALG"], 
            'previasAprobadas': ["TDC2", "FMIN"], 
            'materiasEq2018': ["electricidad_electronica_industrial", "intrumentacion"], 
            'semestre': 4
        },
        { # PIC2 
            'codigo': "PIC2", 
            'nombre': "Proyecto integrador de competencias 2", 
            'previasCursadas': ["MAT3", "PRG2", "EALG", "SLSO", "DIES", "EDG1"], 
            'previasAprobadas': ["PIC1"], 
            'materiasEq2018': ["proyecto_3", "proyecto_4"], 
            'semestre': 4
        },
        #  S5 - 8 materias
        { # MAEL 
            'codigo': "MAEL", 
            'nombre': "Maquinas electricas", 
            'previasCursadas': ["AEIN"], 
            'previasAprobadas': ["EALG"], 
            'materiasEq2018': ["mecanica_aplicada_a_maquinas", "maquinas_electricas"], 
            'semestre': 5
        },
        { # TIND 
            'codigo': "TIND", 
            'nombre': "Telematica industrial", 
            'previasCursadas': ["TMPR","PRG3"], 
            'previasAprobadas': ["EALG","PRG2"],  
            'semestre': 5
        },
        { # FIS3 
            'codigo': "FIS3", 
            'nombre': "Fisica 3 (Termica y fluidos)", 
            'previasCursadas': ["AEIN"], 
            'previasAprobadas': ["MAT3","PRG2","EALG","SLSO","DIES","EDG1"], 
            'materiasEq2018': ["termodinamica"], 
            'semestre': 5
        },
        { # INSC 
            'codigo': "INSC", 
            'nombre': "Introduccion a los sistemas de control", 
            'previasCursadas': ["AEIN"], 
            'previasAprobadas': ["MAT3","PRG2","EALG","SLSO","DIES","EDG1"], 
            'materiasEq2018': ["introduccion_a_control"], 
            'semestre': 5
        },
        { # LEGL 
            'codigo': "LEGL", 
            'nombre': "Legislacion laboral", 
            'previasAprobadas': ["MAT3","PRG2","EALG","SLSO","DIES","EDG1"], 
            'materiasEq2018': ["legislacion_laboral"], 
            'semestre': 5
        },
        { # PFAB 
            'codigo': "PFAB", 
            'nombre': "Procesos de fabricacion", 
            'previasAprobadas': ["MAT3","PRG2","EALG","SLSO","DIES","EDG1"], 
            'materiasEq2018': ["manufactura_asistida"], 
            'semestre': 5
        },
        { # APTM 
            'codigo': "APTM", 
            'nombre': "Anteproyecto de tecnologo", 
            'previasAprobadas': ["PIC2"], 
            'materiasEq2018': ["proyecto_4"], 
            'semestre': 5
        },
        { # PPCU 
            'codigo': "PPCU", 
            'nombre': "Practica profesional curricular", 
            'previasAprobadas': ["MAT3","PRG2","EALG","SLSO","DIES","EDG1"], 
            'materiasEq2018': ["ppt"], 
            'semestre': 5
        },
        # S6 - 7 materias
        { # EDG2 
            'codigo': "EDG2", 
            'nombre': "Electronica digital 2", 
            'previasAprobadas': ["EALG","EDG1"], 
            'materiasEq2018': ["tecnicas_digitales"], 
            'semestre': 6
        },
        { # HYNE 
            'codigo': "HYNE", 
            'nombre': "Hidraulica y neumatica", 
            'previasAprobadas': ["TMPR","PRG3","MEM1","FIS2","AEIN","PIC2"], 
            'materiasEq2018': ["hidraulica_1", "hidraulica_2"], 
            'semestre': 6
        },
        { # AUTM 
            'codigo': "AUTM", 
            'nombre': "Automatizacion", 
            'previasCursadas': ["TIND","INSC"], 
            'previasAprobadas': ["TMPR","PRG3","MEM1","FIS2","AEIN","PIC2"], 
            'materiasEq2018': ["mecatronica", "programacion_3"], 
            'semestre': 6
        },
        { # TDCR 
            'codigo': "TDCR", 
            'nombre': "Tecnologias de control y robotica", 
            'previasCursadas': ["INSC"], 
            'materiasEq2018': ["tecnologia_de_control_y_robotica"], 
            'semestre': 6
        },
        { # IMEL 
            'codigo': "IMEL", 
            'nombre': "Instrumentacion y medidas electricas", 
            'previasCursadas': ["MAEL","INSC"], 
            'previasAprobadas': ["TMPR","PRG3","MEM1","FIS2","AEIN","PIC2"], 
            'materiasEq2018': ["intrumentacion"], 
            'semestre': 6
        },
        { # PIND 
            'codigo': "PIND", 
            'nombre': "Procesos industriales", 
            'previasAprobadas': ["TMPR","PRG3","MEM1","FIS2","AEIN","PIC2"], 
            'materiasEq2018': ["procesos_de_fabricacion"], 
            'semestre': 6
        },
        { # PFTM 
            'codigo': "PFTM", 
            'nombre': "Proyecto final de tecnologo", 
            'previasAprobadas': ["APTM"], 
            'materiasEq2018': ["proyecto_tecnologo"], 
            'semestre': 6
        },
        # S7 - 6 materias
        { # MAT4 
            "codigo": "MAT4",
            "nombre": "Matematica 4",
            "previasAprobadas": ["MAEL", "TIND", "FIS3", "INSC", "LEGL", "PFAB", "APTM", "PPCU"],
            "materiasEq2018": ["matematica_4"],
            "semestre": 7
        },
        { # EPOT 
            "codigo": "EPOT",
            "nombre": "Electronica de potencia",
            "previasCursadas": ["TDCR", "IMEL"],
            "previasAprobadas": ["MAEL", "TIND", "FIS3", "INSC", "LEGL", "PFAB", "APTM", "PPCU"],
            "materiasEq2018": ["electronica_de_potencia"],
            "semestre": 7
        },
        { # MEM2 
            "codigo": "MEM2",
            "nombre": "Materiales y elementos de maquinas 2",
            "previasAprobadas": ["MAEL", "TIND", "FIS3", "INSC", "LEGL", "PFAB", "APTM", "PPCU"],
            "materiasEq2018": ["mecanica", "dinamica_y_vibraciones"],
            "semestre": 7
        },
        { # GPYE 
            "codigo": "GPYE",
            "nombre": "Gestion de proyectos y emprendimientos",
            "previasAprobadas": ["MAEL", "TIND", "FIS3", "INSC", "LEGL", "PFAB", "APTM", "PPCU"],
            "materiasEq2018": ["gestion"],
            "semestre": 7
        },
        { # SEMB 
            "codigo": "SEMB",
            "nombre": "Sistemas embebidos",
            "previasCursadas": ["TDCR"],
            "previasAprobadas": ["MAEL", "TIND", "FIS3", "INSC", "LEGL", "PFAB", "APTM", "PPCU"],
            "semestre": 7
        },
        { # TCYF 
            "codigo": "TCYF",
            "nombre": "Transferencia de calor y fluidos",
            "previasAprobadas": ["MAEL", "TIND", "FIS3", "INSC", "LEGL", "PFAB", "APTM", "PPCU"],
            "materiasEq2018": ["fenomenos_de_transporte"],
            "semestre": 7
        },
        # S8 - 6 materias
        { # PYES 
            "codigo": "PYES",
            "nombre": "Probabilidad y estadistica",
            "previasAprobadas": ["EDG2", "HYNE", "AUTM", "TDCR", "IMEL", "PIND", "PFTM"],
            "materiasEq2018": ["probabilidad_y_estadistica"],
            "semestre": 8
        },
        { # MNPI 
            "codigo": "MNPI",
            "nombre": "Metodos numericos para ingenieria",
            "previasCursadas": ["MAT4"],
            "previasAprobadas": ["EDG2", "HYNE", "AUTM", "TDCR", "IMEL", "PIND", "PFTM"],
            "materiasEq2018": ["metodos_numericos"],
            "semestre": 8
        },
        { # PRDS 
            "codigo": "PRDS",
            "nombre": "Procesamiento de señales (A/D)",
            "previasAprobadas": ["EDG2", "HYNE", "AUTM", "TDCR", "IMEL", "PIND", "PFTM"],
            "materiasEq2018": ["programacion_4"],
            "semestre": 8
        },
        { # MDSA 
            "codigo": "MDSA",
            "nombre": "Mantenimiento de sistemas automatizados",
            "previasCursadas": ["SEMB"],
            "previasAprobadas": ["EDG2", "HYNE", "AUTM", "TDCR", "IMEL", "PIND", "PFTM"],
            "semestre": 8
        },
        { # SCAP 
            "codigo": "SCAP",
            "nombre": "Sistemas de control aplicados",
            "previasCursadas": ["EPOT"],
            "previasAprobadas": ["EDG2", "HYNE", "AUTM", "TDCR", "IMEL", "PIND", "PFTM"],
            "materiasEq2018": ["sistemas_de_control_aplicados"],
            "semestre": 8
        },
        { # TMD2 
            "codigo": "TDM2",
            "nombre": "Tecnologia de materiales 2",
            "previasAprobadas": ["EDG2", "HYNE", "AUTM", "TDCR", "IMEL", "PIND", "PFTM"],
            "materiasEq2018": ["metalurgica_fisica"],
            "semestre": 8
        },
        # S9 - 5 materias
        { # DMEC
            'codigo': "DMEC", 
            'nombre': "Diseño mecatronica", 
            'materiasEq2018': ["diseño_mecatronico"], 
            'previasCursadas': ["SCAP", "MDSA"], 
            'previasAprobadas': ["MAT4", "EPOT", "MEM2", "GPYE", "SEMB", "TCYF"], 
            'semestre': 9
        },
        { # RBIN
            'codigo': "RBIN", 
            'nombre': "Robotica industrial", 
            'materiasEq2018': ["robotica_industrial"], 
            'previasCursadas': ["SCAP"], 
            'previasAprobadas': ["MAT4", "EPOT", "MEM2", "GPYE", "SEMB", "TCYF"], 
            'semestre': 9
        },
        { #MAIC
            'codigo': "MAIC", 
            'nombre': "Manufactura asistida por computador", 
            'materiasEq2018': ["manufactura_asistida"], 
            'previasAprobadas': ["MAT4", "EPOT", "MEM2", "GPYE", "SEMB", "TCYF"], 
            'semestre': 9
        },
        { #CPIN
            'codigo': "CPIN", 
            'nombre': "Costos para ingenieria", 
            'materiasEq2018': ["costos"], 
            'previasAprobadas': ["MAT4", "EPOT", "MEM2", "GPYE", "SEMB", "TCYF"], 
            'semestre': 9
        },
        { #PFG1
            'codigo': "PFG1", 
            'nombre': "Proyecto final de grado 1", 
            'materiasEq2018': ["anteproyecto_de_ing"], 
            'previasAprobadas': ["PYES", "MNPI", "PRDS", "MDSA", "SCAP", "TDM2"], 
            'semestre': 9
        },
        # S10 - 4 materias
        { #GCAL
            'codigo': "GCAL", 
            'nombre': "Gestion de calidad", 
            'materiasEq2018': ["gestion_de_calidad"], 
            'previasAprobadas': ["PYES", "MNPI", "PRDS", "MDSA", "SCAP", "TDM2"], 
            'semestre': 10
        },
        { #GIAM
            'codigo': "GIAM", 
            'nombre': "Gestion de impacto ambiental", 
            'materiasEq2018': ["gestion_ambiental"], 
            'previasAprobadas': ["PYES", "MNPI", "PRDS", "MDSA", "SCAP", "TDM2"], 
            'semestre': 10
        },
        { #SICF
                'codigo': "SICF", 
            'nombre': "Sistemas inteligentes y ciberfisicos", 
            'materiasEq2018': ["sistemas_inteligentes_y_ciberfisicos"], 
            'previasAprobadas': ["PYES", "MNPI", "PRDS", "MDSA", "SCAP", "TDM2"], 
            'semestre': 10
        },
        { #PFG2
            'codigo': "PFG2", 
            'nombre': "Proyecto final de grado 2", 
            'materiasEq2018': ["proyecto_final_ing"], 
            'previasAprobadas': ["DMEC", "RBIN", "MAIC"], 
            'semestre': 10
        }
    ]
    return plan_2023

def cargarBD(Alumno): # Instancia datos de los planes de estudio 
    global unAlumno
    unAlumno = Alumno
    if(not unAlumno.materias_2018[0].nombre):
        plan_2018 = plan2018()
        for i, materia in enumerate(plan_2018):
            unAlumno.materias_2018[i].nombre = materia['nombre']
    
    plan_2023 = plan2023()
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
            if materia_eq_2018 in materia_2018.nombre:
                encontreMateria = True
                if materia_eq_2018 == materia_2018.nombre:
                    if materia_2018.estado == EstadoMateria.EXAMEN:
                        # Cómo TUTORIA es el peor caso, hay que tomar esa excepción
                        # Si se tienen 1=APROBADA, 1=EXAMEN, 1=TUTORIA 
                        # -> estado de nueva materia = TOTURIA.
                        if estadoNuevo != EstadoMateria.TUTORIA:
                            estadoNuevo = EstadoMateria.EXAMEN
                    elif materia_2018.estado == EstadoMateria.TUTORIA:
                        estadoNuevo = EstadoMateria.TUTORIA
                    elif materia_2018.estado == EstadoMateria.PENDIENTE:
                        # Si alguna materia eq del plan 2018 se encuentra pendiente,
                        # la correspondiente al plan 2023 tendrá el mismo estado,
                        # sin importar el estado del resto de mateiras eq.
                        estadoNuevo = EstadoMateria.PENDIENTE
    
    # Verifica si la materia es nueva.
    if not encontreMateria:
        return EstadoMateria.PENDIENTE
    
    return estadoNuevo

def puedeCursarMateria(unaMateria: Materia2023): # Objetivo 3, comprobar si puede cursar X nueva materia 
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

def mostrarAlumno():
    print(f"Nombre: {unAlumno.nombre}")
    print(f"Apellido: {unAlumno.apellido}")
    print(f"CI: {unAlumno.ci}")
def mostrarEstados2018():
    print("###############################################")
    print("Materias 2018")
    for materia in unAlumno.materias_2018:
        print(f"    {materia.nombre}: {materia.estado}")
    print("###############################################")
def mostrarEstados2023():
    print("###############################################")
    print("Materias 2023")
    for materia in unAlumno.materias_2023:
        print(f"    {materia.nombre}: {materia.estado}")
    print("###############################################")
