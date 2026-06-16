import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
respuesta = requests.get(url)

# Forzamos a que interprete la web correctamente en UTF-8
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
        
    df = pd.DataFrame(lista_libros)
    print("Datos cargados en el DataFrame.")
    print("-" * 50)
    
    print("Limpiando la columna de precios...")
    
    # Ahora que no existe el carácter fantasma 'Â':
    df['Precio'] = df['Precio_Crudo'].str.replace('£', '').astype(float)
    
    df = df.drop(columns=['Precio_Crudo'])
    
    print("\nTabla limpia actualizada:")
    print(df.head())
    print("-" * 50)
    
    print("Corriendo validación técnica del tipo de dato:")
    print(df.dtypes)
    print("-" * 50)
    print("completado exitosamente y error solucionado!")

    # ---------------------------------------------------------
    # ANÁLISIS ESTADÍSTICO BÁSICO
    # ---------------------------------------------------------
    print("Calculando métricas de mercado...")
    print("-" * 50)
    
    # 1. Calculamos las métricas usando funciones nativas de Pandas
    precio_promedio = df['Precio'].mean()
    precio_maximo = df['Precio'].max()
    precio_minimo = df['Precio'].min()
    
    # Buscamos cuáles son los libros específicos más caro y más barato
    # Usamos idxmax() e idxmin() para encontrar la fila exacta
    libro_mas_caro = df.loc[df['Precio'].idxmax()]['Titulo']
    libro_mas_barato = df.loc[df['Precio'].idxmin()]['Titulo']
    
    # Mostramos los resultados con un diseño limpio
    print(f"REPORTES DEL MERCADO DE LIBROS:")
    print(f"   Precio Promedio: £{precio_promedio:.2f}")
    print(f"   Libro más Caro:   £{precio_maximo:.2f} -> ({libro_mas_caro})")
    print(f"   Libro más Barato: £{precio_minimo:.2f} -> ({libro_mas_barato})")
    print("-" * 50)
    print("Ya generas insights de valor desde los datos crudos.")

    # ---------------------------------------------------------
    # EXPORTACIÓN DE DATOS
    # ---------------------------------------------------------
    print("Guardando los datos en tu computadora...")
    
    # Definimos el nombre del archivo final
    nombre_archivo = "reporte_precios_libros.csv"
    
    # Exportamos el DataFrame usando la función nativa de Pandas
    # Usamos index=False para que no nos guarde la columna de números 0, 1, 2...
    df.to_csv(nombre_archivo, index=False, encoding='utf-8-sig')
    
    print("-" * 50)
    print(f"¡ÉXITO TOTAL! Archivo creado con el nombre: '{nombre_archivo}'")
    print("Revisa la misma carpeta donde tienes tu código, ¡ahí estará!")
    print("=" * 60)
    print("COMPLETADO CON BROCHE DE ORO! 🏆")
else:
    print("Error al conectar con la página.")