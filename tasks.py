from invoke import task, run

# Tarea de limpieza de ficheros
@task 
def clean(c):
	print("Borrando caché de python.")
	run("find . -maxdepth 5 -type d -name  .pytest_cache -exec rm -r {} +")
	run("find . -maxdepth 5 -type d -name __pycache__ -exec rm -r {} +")

# Tarea de ejecución del modelo
@task
def execute(c):
	print("Ejecución de MedAuth\n")
	run("python3 src/kivy_gui.py")