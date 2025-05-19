import pandas as pd
from datetime import datetime, timedelta

start_date = datetime.strptime('2025-05-19', '%Y-%m-%d')  # Primer lunes disponible (ajustado al verdadero lunes)
days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Lista de tareas semanales
weekly_plan = [
    [
        "JS: Variables, funciones flecha, DOM básico",
        "Python: Archivos .txt y .json, uso de with",
        "JS: Eventos, manipulación de DOM",
        "Python: List comprehensions, lambda, zip",
        "Proyecto: To-do list JS / Gestor de notas PY",
        "Libre o repaso",
        "JS: Desafíos DOM (teclado, color hover)"
    ],
    [
        "JS: map, filter, reduce, forEach",
        "Python: Módulos y manejo de errores",
        "JS: Funciones como parámetros, módulos",
        "Python: Decoradores",
        "Proyecto: Filtro de productos JS / Calculadora modular PY",
        "Libre o repaso",
        "JS: Mini desafíos"
    ],
    [
        "JS: setTimeout, Promesas",
        "Python: Web scraping con requests y BeautifulSoup",
        "JS: fetch, async/await, API pública",
        "Python: Guardar scraping en Excel",
        "Proyecto: Clima con JS / Scraper de precios PY",
        "Libre o repaso",
        "JS: Repaso Promesas"
    ],
    [
        "Python: Flask básico, servidor y rutas",
        "JS: fetch desde Flask",
        "Python: Rutas con JSON, lista de tareas",
        "JS: Mostrar JSON en DOM",
        "Proyecto: API de tareas + Frontend",
        "Libre o repaso",
        "CSS: Estilos para la app"
    ],
    [
        "Python: Métodos PUT, DELETE en Flask",
        "JS: Validación de formularios",
        "Python: Persistencia con JSON o SQLite",
        "JS: Animaciones visuales",
        "Proyecto: CRUD full stack (Flask + JS)",
        "Libre o repaso",
        "Desafíos opcionales"
    ],
    [
        "JS: Renderizado dinámico y templates",
        "Python: Modularización con Blueprints",
        "JS: Animaciones con CSS y JS",
        "Python: Organización y .env",
        "Proyecto: Mini CRM / Inventario",
        "Libre o repaso",
        "Debugging y revisión"
    ],
    [
        "JS: Estructura frontend/backend",
        "Python: CORS y seguridad básica",
        "JS: Estilizado con Tailwind o Bootstrap",
        "Python: Pruebas con Postman",
        "Proyecto: Finaliza app conectada a DB",
        "Libre o repaso",
        "Preparar README y capturas"
    ],
    [
        "Git: init, push, GitHub",
        "Deploy: Render.com o Vercel",
        "Portafolio web: diseño y contenido",
        "Sube tus proyectos y enlaces",
        "Feedback: muestra tu trabajo",
        "Libre o repaso",
        "Plan futuro y mantenimiento"
    ]
]

# Crear estructura de datos
data = []
for week_num, week_tasks in enumerate(weekly_plan, start=1):
    for day_offset, task in enumerate(week_tasks):
        date = start_date + timedelta(days=((week_num - 1)* 7) + day_offset)
        data.append({
            "Semana": f"Semana {week_num}",
            "Fecha": date.strftime("%Y-%m-%d"),
            "Día": days[day_offset],
            "Tarea": task
        })
        
# Crear DataFrame y exportar CSV
df = pd.DataFrame(data)
csv_path = "./Plan_8_Semanas_JS_Python_Notion.csv"
df.to_csv(csv_path, index=False)

df.to_csv(csv_path, index=False)

csv_path