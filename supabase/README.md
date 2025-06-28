# Documentación Técnica

## Portal y Observabilidad

![Diagrama 1](supabase_1.png)

En el diagrama mostramos la arquitectura de los componentes base de Supabase, plataforma de código abierto para desarrollar aplicaciones. A continuación, describo el propósito y la funcionalidad que aporta cada componente, basándome en el nombre y la versión indicada:

**Componentes resaltados en amarillo (core de Supabase o componentes clave):**

* **Supa Visor (supabase/supavisor [ 2.5.1 ])**
    * **Propósito:** Supavisor es un pooler de conexiones de PostgreSQL desarrollado por Supabase.
    * **Funcionalidad:** Permite gestionar y reutilizar conexiones a la base de datos PostgreSQL, lo que es crucial para la escalabilidad y eficiencia de las aplicaciones. Reduce la sobrecarga de establecer nuevas conexiones para cada solicitud, mejorando el rendimiento y la capacidad de la base de datos para manejar un gran número de clientes concurrentes.

* **db (supabase/postgres [ 15.8.1.060 ])**
    * **Propósito:** Este es el componente central de la base de datos relacional.
    * **Funcionalidad:** Proporciona la base de datos PostgreSQL donde se almacenan todos los datos de la aplicación, incluyendo tablas, vistas, funciones, etc. Es el motor de persistencia de datos para Supabase.

* **log flare analytics (supabase/logflare [ 1.14.2 ])**
    * **Propósito:** Logflare es una herramienta de agregación y análisis de logs.
    * **Funcionalidad:** Recopila, centraliza y permite analizar los logs generados por los diferentes componentes de la arquitectura. Esto es esencial para la depuración, monitoreo del rendimiento, auditoría y comprensión del comportamiento de la aplicación y la infraestructura.

* **vector observability (timberio/vector [ 0.28.1-alpine ])**
    * **Propósito:** Vector es una herramienta de pipeline de datos observacionales (logs, métricas, trazas).
    * **Funcionalidad:** Actúa como un agente ligero para recolectar, transformar y enrutar datos de telemetría (principalmente logs en este contexto de "observability") desde varias fuentes hacia destinos como sistemas de análisis de logs, bases de datos de métricas, etc. Contribuye a la observabilidad general del sistema.

* **kong (kong [ v2.8.1 ]) (Aparece dos veces, lo que podría indicar redundancia o instancias separadas para diferentes propósitos)**
    * **Propósito:** Kong es una API Gateway de código abierto.
    * **Funcionalidad:** Actúa como un punto de entrada unificado para todas las solicitudes a la API. Proporciona funcionalidades clave como enrutamiento de API, autenticación, autorización, limitación de tasas, almacenamiento en caché, monitoreo y transformación de solicitudes. Es fundamental para la seguridad y la gestión del tráfico de las API.

* **Supabase Studio (supabase/studio [ 2025.06.02-sha-8f2993d ])**
    * **Propósito:** Es la interfaz de usuario web para gestionar tu proyecto Supabase.
    * **Funcionalidad:** Proporciona una consola visual para interactuar con la base de datos, gestionar tablas, ejecutar consultas SQL, ver logs, configurar autenticación, gestionar almacenamiento de archivos, y más. Es la herramienta principal para los desarrolladores que trabajan con Supabase. La fecha en la versión (`2025.06.02`) es interesante, podría ser una versión de desarrollo o una fecha de compilación.

* **postgres meta (supabase/postgres-meta [ v0.89.3 ])**
    * **Propósito:** Postgres-meta es una API RESTful para gestionar tu base de datos PostgreSQL.
    * **Funcionalidad:** Proporciona una capa de abstracción sobre PostgreSQL, permitiendo a Supabase Studio y otros servicios interactuar programáticamente con la base de datos para realizar operaciones como la introspección del esquema, gestión de roles, creación de tablas, etc., sin necesidad de interactuar directamente con el cliente SQL.

La arquitectura describe un entorno Supabase, donde **PostgreSQL** es la base de datos principal, **Supavisor** gestiona las conexiones, **Kong** maneja las API, **Logflare** y **Vector** se encargan de la observabilidad y los logs, y **Supabase Studio** junto con **Postgres-meta** proporcionan las herramientas de gestión y la interfaz de usuario.
