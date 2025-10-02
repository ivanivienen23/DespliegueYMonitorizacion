docker info
# Construye imágenes y levanta contenedores
docker compose up -d --build

# Contenedores activos
docker compose ps

# Ver info json
Invoke-RestMethod http://localhost:5000/api/citas

# Parar y eliminar contenedores (manteniendo volúmenes)
docker compose down

# Levantar de nuevo
docker compose up -d