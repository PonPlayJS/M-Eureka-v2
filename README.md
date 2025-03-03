# M-Eureka

¡Bienvenido al proyecto M-Eureka! Esta es una versión pre-prototipo de Eureka simplificada. Para más información, visita [Eureka Research](https://eureka-research.github.io/).

## Requisitos

- pip
- miniconda
- OpenAI API

## Crear un Entorno Virtual con Conda

Para crear y activar un entorno virtual con Conda, ejecuta los siguientes comandos:

```bash
conda create --name ekmini python=3.10
conda activate ekmini # Puedes desactivarlo con "conda deactivate"
```

## Dependencias

Instala las dependencias necesarias usando pip:

```bash
pip install gym stable-baselines3 
pip3 install openai==0.28
pip install gym[classic_control]
pip3 install numpy==1.23.1
pip install 'shimmy>=2.0'
```

## Clonar el Repositorio y Navegar al Directorio

Clona el repositorio y navega al directorio M-Eureka:

```bash
git clone https://github.com/PonPlayJS/M-Eureka
cd M-Eureka
```

## Importante

1. Después de completar los pasos anteriores, abre un editor de código y navega a la carpeta `M-Eureka`.
2. Abre `code_generator.py` y reemplaza `OPENIA_KEY` con tu clave de API de OpenAI.
3. Abre `training.py` y modifica `USER_PATH` para especificar dónde quieres guardar los videos:

    ```python
    # Modificar aquí
    model.save("USER_PATH")
    ```

4. Inserta tu clave de API de OpenAI y luego ejecuta `orden.sh` con los siguientes comandos en la terminal:

    ```bash
    chmod +x orden.sh
    ./orden.sh
    ```

## Ver tus Simulaciones

Para ver tus simulaciones, navega a la ruta especificada en `USER_PATH` y ejecuta:

```bash
cd [USER_PATH]
python view.py
```

## Estructura del Proyecto


## Capturas de Pantalla

![imagen](https://github.com/user-attachments/assets/c899c84a-e098-45e2-9579-eec26a2d510d)

---

¡Gracias por usar M-Eureka! Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue o un pull request.
