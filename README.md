# ChatGPT respondiendo la PAES
En este repositorio podrás encontrar el proyecto que en EvoAcadmy desarrollamos para hacer respoonder a ChatGPT responder la PAES. Los resultados del experimento fueron publicados en el artículo [ChatGPT supera al 99% de los estudiantes en la PAES](https://www.evoacademy.cl/chatgpt-supera-al-99-de-los-estudiantes-en-paes-chile/) de la página [EvoAcademy](https://www.evoacademy.cl/).

Una descripción detalla de la estructura de este proyecto la podrás encontrar en el artículo [Así es como hicimos a ChatGPT responder la PAES](https://www.evoacademy.cl/codigo-chatgpt-respondiendo-la-paes/).

**Interesado en clonar el proyecto y correrlo en tu computadora?**
Primero debes clonar el proyecto ejecutando en tu terminal:

```
git clone https://github.com/jovasque156/chatgpt_paes.git
```

Y luego debes instalar los paquetes que están en *requirements.txt* y tambien asegurarte de que tienes instalados los Python bindings oficiales de OpenAI

```
pip install openai
pip install -r requirements.txt
```

## API Key
Para que tu experimento funcione, debes asegurarte de crear una API Key en OpenAI siguiende los pasos que aparecen en este [link](https://platform.openai.com/docs/quickstart/add-your-api-key?ref=evoacademy.cl). La API Key que generes debes copiarla en el archivo *key.txt*. Sin este paso, el llamado a la API no funcionara.

## Prompts para [chat.open](https://chat.openai.com/chat)
Si deseas hacer la prueba directo en ChatGPT usando la interfaz creada por OpenAI, puedes explorar los prompts en la carpeta [prompts](https://github.com/jovasque156/chatgpt_paes/tree/main/ensayos). Hemos generado archivos planos con los prompts separados por los caracteres ----, que consideran el largo máximo de texto que puedes ingresar en el chat.

## Contacto
Además de levantar issues o generar un pull requests, puedes usar este [formulario](https://www.evoacademy.cl/contacto/) para contactarnos ante cualquier inquietud.
