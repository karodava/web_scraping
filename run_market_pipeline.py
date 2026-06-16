import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

print(f" Ejecutando pipeline automático de precios - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("-" * 60)

url = "https://books.toscrape.com/"

try:
    # Petición y captura
    respuesta = requests.get(url)
    respuesta.encoding = 'utf-8'
    
    if respuesta.status_code == 200:
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        todos_los_libros = soup.find_all('article', class_='product_pod')
        
        lista_libros = []
        for libro in todos_los_libros:
            titulo = libro.h3.a['title']
            precio_crudo = libro.find('p', class_='price_color').text
            
            lista_libros.append({
                "Titulo": titulo,
                "Precio_Crudo": precio_crudo
            })
            
        # Estructura y Limpieza
        df = pd.DataFrame(lista_libros)
        df['Precio'] = df['Precio_Crudo'].str.replace('£', '').astype(float)
        df = df.drop(columns=['Precio_Crudo'])
        
        # Agregamos una columna con la fecha exacta del monitoreo
        df['Fecha_Monitoreo'] = datetime.now().strftime('%Y-%m-%d')
        
        # Exportación definitiva
        nombre_archivo = "reporte_precios_libros.csv"
        df.to_csv(nombre_archivo, index=False, encoding='utf-8-sig')
        
        print(" Pipeline completado de forma exitosa.")
        print(f" Archivo '{nombre_archivo}' actualizado correctamente.")
    else:
        print(f" Error de conexión con el servidor: Código {respuesta.status_code}")

except Exception as e:
    print(f" Error inesperado durante la ejecución: {e}")

print("=" * 60)