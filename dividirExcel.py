import pandas as pd
import os

# Cargar el archivo CSV
archivo = "delitos_bucaramanga_202501202158.csv"  # Cambia esto por la ruta a tu archivo original
# Cargar archivo Excel asegurando que se lean todas las columnas
df = pd.read_csv('delitos_bucaramanga_202501202158.csv', usecols=None, header=0)  # Usa la primera fila como encabezado

# Mostrar las primeras filas para verificar si todas las columnas fueron cargadas
print(df.head())
df = pd.read_csv(archivo)

# Seleccionar 20 filas aleatorias
muestra = df.sample(n=15)

# Definir la ruta a la carpeta donde quieres guardar el archivo
directorio_destino = r"C:\Users\Hewlett Packard\Desktop\Nueva carpeta\Modelo-simulacion-delitos-"  # Ruta deseada
os.makedirs(directorio_destino, exist_ok=True)  # Crear la carpeta si no existe

# Guardar el archivo CSV en esa ubicación
ruta_destino = os.path.join(directorio_destino, "muestra_aleatoria.csv")
muestra.to_csv(ruta_destino, index=False)

print(f"Muestra guardada en: {ruta_destino}")
