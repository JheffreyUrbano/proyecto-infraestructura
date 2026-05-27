# Sistema de Gestión de Ferretería

## Descripción
Sistema de gestión de inventario para ferretería con arquitectura de microservicios, contenedores Docker, orquestación con Swarm y procesamiento de datos con PySpark.

## Tecnologías
- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Node.js, Express
- **Base de datos**: PostgreSQL
- **Procesamiento**: PySpark, Apache Spark
- **Orquestación**: Docker, Docker Swarm

## Arquitectura
[Cliente] → [Nginx] → [Node.js API] → [PostgreSQL]  
          ↓°  
[PySpark Analytics]

## Requisitos
- Docker 20.10+
- Docker Compose 2.0+
- 8GB RAM mínimo
- 20GB espacio en disco

# Instalación Rápida
### Clonar repositorio
git clone <repo-url>
cd ferreteria-proyecto

### Inicializar Swarm
docker swarm init --advertise-addr <IP>

### Desplegar stack
docker stack deploy -c swarm/stack.yml ferreteria

### Acceder a la aplicación
http://localhost:3000

Credenciales
- Usuario: admin
- Contraseña: admin123

Datos del Sistema
Tipo	Cantidad
Productos	100,000
Proveedores	5,000
Ventas	50,000
Valor inventario	$1.24 B
Comandos Útiles
bash
### Ver servicios
docker service ls

### Escalar backend
docker service scale ferreteria_backend=10

### Ver logs
docker service logs ferreteria_backend -f

### Ejecutar PySpark
docker run --rm --network ferreteria_net ferreteria-pyspark spark-submit --master local[*] /opt/spark/jobs/analytics.py

### Estructura del Proyecto
```
ferreteria-proyecto/
├── docker-compose.yml
├── Dockerfile
├── Dockerfile.pyspark
├── server.js
├── public/
│   ├── index.html
│   ├── inventario.html
│   └── css/
├── pyspark_jobs/
│   └── analytics_masivo.py
├── swarm/
│   └── stack.yml
└── postgres/
    └── init.sql
```
