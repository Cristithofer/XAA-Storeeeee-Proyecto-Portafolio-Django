# XAA Storeeee - E-Commerce Django

Aplicacion web de e-commerce desarrollada con Django 6.0.
Proyecto final de portafolio con flujo completo:
catalogo, carrito, confirmacion de compra y administracion.

Repositorio: https://github.com/Cristithofer/XAA-Storeeeee-Proyecto-Portafolio-Django

---

Requisitos

- Python 3.10 o superior
- pip
- virtualenv

---

Instalacion

1. Clonar el repositorio

git clone https://github.com/Cristithofer/XAA-Storeeeee-Proyecto-Portafolio-Django.git
cd ecommerce_Pro_final

2. Crear y activar entorno virtual

python -m venv venv
venv\Scripts\activate

3. Instalar dependencias

pip install -r requirements.txt

---

Como ejecutar en local

1. Aplicar migraciones

python manage.py migrate

2. Cargar datos de prueba (opcional)

python manage.py shell

Pegar en la consola:
from tienda.models import Categoria, Producto
c1, _ = Categoria.objects.get_or_create(nombre='Perifericos', slug='perifericos')
Producto.objects.get_or_create(nombre='Teclado Gamer RGB', defaults={'categoria':c1,'precio':29990,'stock':15})

3. Ejecutar servidor

python manage.py runserver

4. Abrir en navegador

http://127.0.0.1:8000

---

Rutas principales

#Publicas (sin login)
| Ruta | Descripcion |
|------|-------------|
| / | Catalogo de productos |
| /buscar/?q=nombre | Buscador de productos |
| /producto/pk/ | Detalle de producto |
| /usuarios/login/ | Iniciar sesion |
| /usuarios/registro/ | Crear cuenta |

#Cliente (requiere login)
| Ruta | Descripcion |
|------|-------------|
| /carrito/ | Ver carrito |
| /carrito/agregar/pk/ | Agregar producto |
| /carrito/actualizar/pk/ | Actualizar cantidad |
| /carrito/eliminar/pk/ | Quitar producto |
| /carrito/vaciar/ | Vaciar carrito |
| /ordenes/confirmar/ | Confirmar compra |
| /ordenes/historial/ | Historial de ordenes |

#Administrador (requiere is_staff)
| Ruta | Descripcion |
|------|-------------|
| /admin/ | Panel Django admin |
| /producto/agregar/ | Agregar producto (modal) |
| /producto/editar/pk/ | Editar producto |
| /producto/eliminar/pk/ | Eliminar producto |

---

Credenciales de prueba

#Administrador
- Usuario: admin
- Password: admin1234
- Acceso: panel admin + gestion de productos

#Cliente
- Usuario: cliente1
- Password: cliente1234
- Acceso: catalogo, carrito, ordenes

Para crear el usuario cliente ejecutar:

python manage.py shell

from django.contrib.auth.models import User
User.objects.create_user('cliente1', password='cliente1234')

---

Tecnologias

- Django 6.0
- Python 3.x
- SQLite
- Bootstrap 5.3
- Pillow

---

Funcionalidades principales

- Catalogo con filtro por categorias
- Buscador sin duplicados
- Carrito con sesion (agregar, actualizar, eliminar, vaciar)
- Confirmacion de orden asociada al usuario
- Historial de ordenes por usuario
- CRUD de productos solo para administrador
- Subida de imagenes por producto
- Precios formateados en CLP ($19.990)
- Control de stock automatico al comprar
- Mensajes de exito y error en cada accion
- Diseno responsivo morado + Bootstrap 5

---

Autor: [manfred]
