# Documentación del diseño de la aplicación.

El código fuente de la aplicación está en [https://github.com/CronoxD/urbvans](https://github.com/CronoxD/urbvans)
## Estilo de arquitectura de Software
#### El estilo de nuesto microservicio es REST
Esto significa que se puede acceder a un recurso de la base de datos a travéz de su sustantivo en plural, en este caso **/v1/vans/**.

Y en caso de querer acceder a un elemento del recurso se pone el ID del elemento en el path de la siguiente manera **/v1/vans/ee8c4a2e-bbba-4bb9-aca7-01e1ad58c1a2/**

Según REST la API puede estar versionada con el primer elemento del path, en nuestro caso es la versión 1 **/v1/**.

El formato de salida que usamos es **JSON**.

Y para las operaciones de un CRUD utilizamos los métodos HTTP.

- **GET /v1/vans/**: Obtener una lista de las vans.
- **POST /v1/vans/**: Crea una van (es necesario mandarle todos la información en el cuerpo de la petición).
- **PUT /v1/vans/{uuid}**: Actualiza una van (es necesario mandarle todos la información).
- **PATCH /v1/vans/{uuid}**: Actualiza una van de forma parcial (Sólo actualiza los datos que se le mandan en el cuerpo de la petición).
- **DELETE /v1/vans/{uuid}** Elimina el elemento.

La documentación completa e interactiva de la API REST se puede consultar en la url del servidor [localhost/doc/](localhost/doc/)

## Arquitectura de Software

Esta aplicación está diseña para funcionar en una **arquitectura de microservicios**.
El microservicio cubre la administración de las vans en el negocio.
Para hacer el despliegue de la aplicación se usa **Docker** y **Docker compose**.

#### Docker

Hay 4 servicios de docker compose:
1. **app**: Ejecuta el código fuente de Python (Django).
2. **db**: Tiene la base de datos Postgresql.
3. **nginx**: Sirve como reverse proxy, manda los requests a **app** y **app** los procesa con WSGI con la librería gunicorn, también sirve para desplegar algunos archivos estáticos.
4. **cache**: Para evitar que se hagan muchas consultas a la base de datos se guarda en una cache la lista actualizada de vans, el servidor es con memcached.

#### Patrón de diseño Model, View, Template (Django)
Este patrón de diseño divide la aplicación en diferentes responsabilidades, el **model** es la capa que tiene acceso a la base de datos, el **template** es la capa de presentación, en nuestro caso se muestra con un archivo **json** y la **view** es la capa de la lógica de las reglas del negocio.

Para la capa **view** podemos usar **"Vistas basadas en clases"** lo cual nos permite ahorrar mucho código, ya que son clases que contienen la mayoría de las funcionalidades de un sistema, en nuestro caso de una API REST

#### Testing
El aplicativo tiene multiples **pruebas de integración** para brindar confianza al modificar el código en futuras ocaciones y para mitigar lo más posibles los bugs y fallos en producción.

#### Principios SOLID.
El desarrollo de esta aplicación se trató de basar en los principios **SOLID** para tratar de tener la mejor de la calidad en el código.

#### PEP8
También el código está basado en la guía de estilo del **PEP8**. Con la ayuda de la librería **flake8** se puede tener un código completamente basado en **PEP8**.


