Descripción

Este script en Python automatiza el proceso de escanear una dirección IP en busca de puertos abiertos. Primero, realiza un ping a la IP para verificar si está activa. Si la IP responde, el script procede con un escaneo de puertos completos usando Nmap, buscando puertos abiertos en la red. Los puertos abiertos se extraen del archivo de resultados y se copian automáticamente al portapapeles para facilitar su uso.

Después, el script realiza un escaneo detallado de los puertos 22 y 80, incluyendo la detección de versiones de servicios y la ejecución de scripts de Nmap para obtener información más precisa sobre los servicios que se ejecutan en esos puertos. Los resultados del escaneo detallado se guardan en un archivo llamado targeted.
Funcionalidades:

    Ping: Verifica si la IP está activa antes de realizar el escaneo.
    Escaneo de puertos: Escanea todos los puertos abiertos en la IP.
    Extracción y copiado de puertos: Extrae los puertos abiertos y los copia al portapapeles.
    Escaneo detallado: Realiza un análisis más profundo de los puertos 22 y 80 con detección de versiones.

Requisitos:

    Nmap instalado en tu sistema.
    wl-copy para copiar los puertos abiertos al portapapeles.

Este script es útil para realizar auditorías de seguridad básicas o para comprobar rápidamente los servicios disponibles en un servidor. 🚀

Para Instalar nmap el Archlinux usa el siguiente comando 

    sudo pacman -S nmap
Tambien requieres la herramienta de clipboard de wayland que en archlinux se instala 

    sudo pacman -S wl-clipboard
