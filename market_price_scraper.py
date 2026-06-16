import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    
    print("Extrayendo el catálogo completo de la página 1...")
    print("=" * 60)
    
    # Buscamos TODOS los artículos de libros en la página (devuelve una lista de 20 libros)
    todos_los_libros = soup.find_all('article', class_='product_pod')
    
    # Creamos un contador para listar los libros del 1 al 20
    contador = 1
    
    # Recorremos cada libro uno por uno con un ciclo for
    for libro in todos_los_libros:
        # Extraemos el título y el precio de ese libro en específico
        titulo = libro.h3.a['title']
        precio = libro.find('p', class_='price_color').text
        
        # Lo imprimimos con un formato limpio en la terminal
        print(f"{contador}. 📖 {titulo}")
        print(f"   💰 Precio: {precio}")
        print("-" * 40)
        
        contador += 1
        
    print("=" * 60)
    print("COMPLETADO CON ÉXITO!")
    print("Logramos conectar, entender el HTML y extraer los 20 productos en crudo.")

else:
    print("Error al conectar con la tienda.")