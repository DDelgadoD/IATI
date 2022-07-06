<div id="top"></div>
<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div style="text-align:center;">
  <a href="http://daviddelgadoduenas.pythonanywhere.com">
    <img src="https://raw.githubusercontent.com/DDelgadoD/IATI/master/media/Screenshot.png" alt="Logo" width="1600" height="400">
  </a>

<h3 style="text-align:center;">IATI</h3>

  <p style="text-align:center;">Test Técnico IATI</p>
</div>



<!-- TABLE OF CONTENTS -->
## Tabla de Contenidos
1. [Introducción](#Intro)
2. [Pruébalo en vivo](#Try)
3. [Archivos Incluidos](#Archivos)
4. [Petición Original](#Peti)
5. [Hecho con...](#hecho)
6. [Licencia](#licencia)
7. [Contacto](#contacto)

<!-- INTRODUCTION -->

## <a name="Intro"></a> Introducción

---

<!-- TRY IT -->

## <a name="Try"></a> Pruébalo en vivo

---

<!-- ARCHIVE LIST -->

## <a name="Archivos"></a> Archivos Incluidos 
- __IATI Localhost.postman_collection.json__ -> export de los endpoints para usar Postman con un localhost
- __IATI PythonAnywhere.postman_collection.json__ -> export de los endpoints para usar Postman con la web "PythonAnywhere".
- __manage.py__ -> no modificado
- __README.md__ -> este archivo
- __requirements.txt__ -> requerimientos del proyecto generado por venv.

### api  

- __apps.py__ -> no modificado.
- __serializers.py__ -> Aquí se incluyen todos los serializadores para la API.
- __test.py__
- __urls.py__ -> Aquí se incluyen todos los endpoints de la API.
- __views.py__ -> Aquí se incluyen las vistas para los endpoints de la API.

### config 

Este es el directorio base del proyecto. Por costumbre lo nombro como config.
- __asgi.py__ -> no modificado.
- __settings__ -> Aquí se han realizado los cambios necesarios para que el proyecto funcione. 
- __urls__ -> Aquí se incluyen las direcciones url globales de todo el proyecto.
- __wsgi.py__ -> no modificado

### media

Este directorio aloja todas las imágenes del proyecto. Como las imagenes se usan globalmente he decidido poner la carpeta en el directorio raíz

### shop
- __admin.py__ -> en este archivo se han añadido "Caps" y "Shirts" para poder poblar la base de datos.
- __apps.py__ -> no modificado
- __models__ -> en este archivo se han creado los modelos de "shop". "Product" que es polimórfico con las subclasses "Cap" y "Shirt", "Item" que es una línea del carrito de la compra, "Cart" que es el carrito de la compra. 
#### [DIR] automatic migration
- __002_load_initial_data.py__ -> Archivo que permite poblar la base de datos con "migrate" añadiéndolo la carpeta migrations de shop después de hacer "makemigrations" para que se cree "0001_inital.py"
#### [DIR] fixtures
- __initial_data.json__ -> JSON que contiene la información para poblar la base de datos con 10 productos.
#### [DIR] management
#### - [SUBDIR] commands
- __loaddata.py__ -> Archivo que sobreescribe el loaddata de django para hacer lo que pide el enunciado y no cargar de nuevo los datos de fixture si ya existen.
 
### static

En este directorio se incluyen los archivos para carga de web estática. No se ha realizado "collectstatic", así que solo están los que se han añadido manualmente.

### templates

En este directorio se incluyen los archivos para la página principal que muestra los endpoints disponibles.

---

<!-- ORIGINAL PETITION -->
## <a name="Peti"></a>Petición Original
## Carrito de compra  
La idea es crear una aplicación muy sencilla para que la use un frontal. Esta aplicación tendrá cuatro acciones (endpoints) principales:

### Listado de productos
La aplicación utiliza dos productos distintos: gorras y camisetas. De las gorras se necesita tener su color principal, color secundario, color del logo y la marca. En cuanto a las camisetas se necesita su color principal, color secundario, talla, marca, tipo de tejido, tallaje (hombre, mujer o unisex) y si tiene mangas o no. De ambos tipos de producto se necesita además la fecha de inclusión en el catálogo, la URL a la foto del mismo, el precio por unidad y un campo de descripción (ejemplo: “Gorra Nike azul/negro 2022”). 
Este primer endpoint solamente devolverá un listado de todos los productos de ambos tipos que haya en la BBDD ordenados por tipo de producto (primero gorras y después camisetas) y dentro de cada uno por fecha de inclusión en el catálogo (más recientes primero). Se debe devolver toda la información de cada tipo de producto.

### Añadir producto al carrito  
Una vez obtenido el listado de productos, el front debe tener la posibilidad de añadir uno de ellos al carrito de la compra.
Este segundo endpoint recibirá el producto a añadir y lo añadirá al carrito junto con la cantidad de dicho producto que se quiere añadir (por defecto la cantidad es una unidad). Hay que tener en cuenta que el carrito no existirá antes de añadirse el primer producto, por lo que habrá que crearlo. Como no se va a implementar ningún modelo de usuario, asociaremos el carrito al día actual, es decir, solo podrá existir un carrito por día. Si en el día de hoy ya existe, usamos ese; si no existe, lo creamos. 

### Ver el carrito
El front en cualquier momento podrá ver el contenido del carrito (incluso antes de añadir un producto, en cuyo caso deberá verlo vacío).
Este endpoint simplemente devolverá una lista de los productos que hayan sido añadidos y el sumatorio del total de los productos añadidos. En esta ocasión, para los productos, solo hace falta que se devuelva su ID, descripción, URL de la foto, cantidad y precio por unidad.

### Comprar
Vamos a simular esta compra de modo que este endpoint solamente enviará al cliente un email con el resumen de su compra.

### Puntos a tener en cuenta
- Sube la app a tu cuenta de GitHub.
- Tendrás que hacer una carga inicial de productos (5 gorras y 5 camisetas). Las propiedades de cada uno rellénalas a tu gusto. Como recomendación, créate una
fixture que se importe en la BBDD al levantar la app controlando que no se dupliquen los productos la sucesivas veces que la levantes
- Para el envío de email, ya que no vamos a implementar un modelo de usuario para esta prueba ni te pedimos que configures un servidor de envío de emails, utiliza
como EMAIL_BACKEND la escritura de emails por consola 
- El contenido o formato de dicho email es libre y no afecta a hacer mejor o peor la prueba. Créalo como más te guste
- No te preocupes si no has tocado alguna cosa que se pide. La idea de esta prueba es ver cómo te desenvuelves y resuelves problemas nuevos.
- No se pide que la prueba sea perfecta aunque sí que sea funcional. La app deberá poder levantarse en local y ser usada desde navegador o Postman.

<!--BUILT WITH-->
## <a name="Hecho"></a> Hecho con ...

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)

<p style="text-align:right;">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## <a name="Licencia"></a>Licencia

Distributed under the MIT License. See [`LICENSE.md`](https://raw.githubusercontent.com/DDelgadoD/DDelgadoD/main/LICENSE.md) for more information.

<p style="text-align:right;">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## <a name="Contacto"></a>Contacto

David Delgado-Dueñas

[![GitHub][github-shield]][github-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![ResearchGate][researchgate-shield]][researchgate-url]
[![Gmail][gmail-shield]][gmail-url]

Link del proyecto: [https://github.com/DDelgadoD/IATI](https://github.com/DDelgadoD/IATI)

<p style="text-align:right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[researchgate-shield]:https://img.shields.io/badge/-researchgate-white.svg?style=for-the-badge&logo=researchgate&colorB=33b864&logoColor=white
[researchgate-url]: https://www.researchgate.net/profile/David-Delgado-Duenas
[gmail-shield]: https://img.shields.io/badge/-Gmail-black.svg?style=for-the-badge&logo=gmail&colorB=red&logoColor=white
[gmail-url]:mailto:david.delgado82@gmail.com
[github-shield]: https://img.shields.io/badge/-Github-black.svg?style=for-the-badge&logo=github&colorB=black
[github-url]: https://github.com/DDelgadoD/
[license-shield]: https://img.shields.io/github/license/DDelgadoD/DDelgadoD.svg?style=for-the-badge
[license-url]: https://raw.githubusercontent.com/DDelgadoD/DDelgadoD/main/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=0072B1
[linkedin-url]: https://www.linkedin.com/in/david-delgado-duenas/
[contributors-shield]: https://img.shields.io/github/contributors/DDelgadoD/IATI.svg?style=for-the-badge
[contributors-url]: https://github.com/DDelgadoD/IATI/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DDelgadoD/IATI.svg?style=for-the-badge
[forks-url]: https://github.com/DDelgadoD/IATI/network/members
[stars-shield]: https://img.shields.io/github/stars/DDelgadoD/IATI.svg?style=for-the-badge
[stars-url]: https://github.com/DDelgadoD/IATI/stargazers
[issues-shield]: https://img.shields.io/github/issues/DDelgadoD/IATI.svg?style=for-the-badge
[issues-url]: https://github.com/DDelgadoD/IATI/issues
[license-shield]: https://img.shields.io/github/license/DDelgadoD/IATI.svg?style=for-the-badge
[license-url]: https://github.com/DDelgadoD/IATI/blob/master/LICENSE.txt
[product-screenshot]: media/screenshot.png
 
