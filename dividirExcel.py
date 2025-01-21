import pandas as pd
import os

# Cargar el archivo CSV
archivo = "delitos_bucaramanga_202501202158.csv"  # Cambia esto por la ruta a tu archivo original
df = pd.read_csv(archivo)

# Seleccionar 20 filas aleatorias
muestra = df.sample(n=20)

# Definir la ruta a la carpeta donde quieres guardar el archivo
directorio_destino = r"C:\Users\Hewlett Packard\Desktop\Nueva carpeta\Modelo-simulacion-delitos-"  # Ruta deseada
os.makedirs(directorio_destino, exist_ok=True)  # Crear la carpeta si no existe

# Guardar el archivo CSV en esa ubicación
ruta_destino = os.path.join(directorio_destino, "muestra_aleatoria.csv")
muestra.to_csv(ruta_destino, index=False)

print(f"Muestra guardada en: {ruta_destino}")
