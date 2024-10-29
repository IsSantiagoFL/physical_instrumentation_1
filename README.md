# Proyecto de Registro y Análisis de Temperatura

## Descripción

Este proyecto fue desarrollado como parte de un trabajo de investigación para el curso de **Instrumentación Física 1**. El objetivo del proyecto era diseñar un sistema que permita recolectar, almacenar y analizar datos de temperatura utilizando el sensor **PT100** conectado a través de un dispositivo de medición y un puerto serial. Además de la adquisición de datos, el sistema ofrece análisis estadístico y visualización gráfica que incluye la temperatura y su derivada en función del tiempo.

Este repositorio, aunque ahora archivado, permanece disponible como referencia histórica para futuros estudios y proyectos académicos.

## Características Principales

- **Registro de Temperatura con PT100**: Captura de datos de temperatura utilizando el sensor **PT100** a intervalos configurables.
- **Almacenamiento en CSV**: Los datos recolectados se almacenan en un archivo CSV para su análisis posterior.
- **Análisis Estadístico**: Cálculo automático de la temperatura mínima, máxima, media y desviación estándar.
- **Visualización de Datos**: Generación de gráficos que muestran la evolución de la temperatura y su derivada respecto al tiempo.

![Gráfico Generado con el Codigo del Proyecto para la aquisisción de Datos](https://github.com/user-attachments/assets/2cc804f9-1ed6-4264-ac68-6a72fd83feed)


## Cómo Ejecutar el Proyecto

### Requisitos Previos

- **Hardware**: Un dispositivo de medición que incluya un sensor **PT100** y un puerto serial configurado (ej. **COM15** en Windows o **/dev/ttyUSB0** en Linux).
- **Python 3.x**: El proyecto está diseñado para ejecutarse en **Python 3.x**.

### Instalación de Dependencias

Antes de ejecutar el proyecto, asegúrate de tener las dependencias instaladas. Para ello, sigue estos pasos:

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/IsSantiagoFL/temperature-logger-analyzer.git
   cd temperature-logger-analyzer
   ```

2. **Instala las dependencias**:
   Puedes usar `pip` para instalar todas las bibliotecas necesarias. El archivo `requirements.txt` contiene las dependencias del proyecto.
   ```bash
   pip install -r requirements.txt
   ```

   Si no tienes un archivo `requirements.txt`, asegúrate de instalar las siguientes bibliotecas manualmente:
   ```bash
   pip install numpy matplotlib datetime csv
   ```

### Configuración del Sensor PT100

- Conecta el **sensor PT100** al dispositivo de medición.
- Asegúrate de que el archivo de configuración del dispositivo (`config1.txt`) esté correctamente ajustado para el PT100.
- Verifica el puerto serial al que está conectado el dispositivo (ej. `COM15` para Windows o `/dev/ttyUSB0` para Linux) y modifícalo si es necesario en el código.

### Ejecución del Proyecto

1. **Configura el intervalo de muestreo**: Ejecuta el script y define el intervalo de muestreo que desees (por ejemplo, un dato por segundo).
   ```bash
   python logger.py
   ```

2. **Almacena los datos**: Una vez iniciada la adquisición, los datos se guardarán en un archivo CSV.

3. **Genera el análisis y los gráficos**: Después de recolectar los datos, puedes ejecutar el análisis estadístico y graficar los resultados utilizando el siguiente comando:
   ```bash
   python analysis.py
   ```

4. **Verifica el archivo CSV**: Los datos estarán disponibles en el archivo `temperatura_ambiente.csv` para análisis posterior o visualización adicional.

## Repositorio Activo

Este repositorio ha sido archivado y ya no se mantendrá. Sin embargo, el proyecto ha sido migrado a un nuevo repositorio donde se seguirán desarrollando nuevas características y mejoras.

Para seguir el desarrollo activo y actualizado, visita:

🔗 [**Temperature Logger and Data Analyzer**](https://github.com/IsSantiagoFL/PT100-Temperature-Logger-Analyzer)

### Mejoras en el Nuevo Repositorio

- **Visualización en Tiempo Real** durante la adquisición de datos.
- Soporte para **múltiples sensores** y diferentes dispositivos de medición.
- Implementación de una **interfaz web** para monitoreo remoto.

## Informe Técnico

Si deseas acceder al informe técnico completo que documenta el diseño del sistema de medición y análisis del **PT100**, puedes descargar el PDF en el siguiente enlace:

📄 [**Descargar Informe Técnico**](https://github.com/IsSantiagoFL/physical_instrumentation_1/blob/main/Informe_PT100_Instrumentacion_Fisica_Santiago_Flores.pdf)

---

### Contacto

- **Autor**: Santiago Ismael Flores-Chávez  
- **GitHub**: [IsSantiagoFL](https://github.com/IsSantiagoFL)

