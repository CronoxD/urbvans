# Urbvans API
Microservicio para administración de VANS (CRUD).

## Requisitos.
1. Docker
2. Docker-compose
3. Git

## Iniciar servidor de desarrollo

1. Clonar repositorio
```bash
git clone https://github.com/CronoxD/urbvans.git && cd urbvans
```

2. Configurar las variables de entorno.
```bash
cp app/.env.dev.example app/.env.devurbvans
```

3. Compilar los contenedores. (El archivo por defecto docker-compose.yml es para desarrollo.)
```bash
docker-compose build
```

4. Correr contenedores.
```bash
docker-compose up
```

La documentación de la API está en http://localhost:8000/doc/

## Configuración para producción.
Se asume que el repositorio ya está clonado en el servidor.

1. Configurar variables de entorno.
```bash
cp app/.env.prod.example app/.env.produrbvans
```

2. Compilar y correr los contenedores
```bash
docker-compose -f docker-compose.prod.yml up -d --build
```

3. Ejecutar las migraciones (Genera el schema de la base de datos).
```bash
docker-compose -f docker-compose.prod.yml exec app python manage.py migrate --noinput
```

4. Genera los archivos estáticos. (Usados en la documentación).
```bash
docker-compose -f docker-compose.prod.yml exec app python manage.py collectstatic --no-input --clear
```

El servidor está en http://localhost
