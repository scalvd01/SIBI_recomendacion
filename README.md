# SIBI_recomendacion

![Phone REC](/sibi-recomendacion/public/st1Recurso1.png)
Aplicación de sistema de recomendación de smartphones para SIBI

---

## Instrucciones
Para probar la aplicación primero hay que descargar el repositorio y realiza los siguientes pasos:

- Primero hay que crear la base de datos en Neo4j Desktop como se indica en las instrucciones detalladas en la carpeta de *Base de datos*

- Una vez hecho esto abrimos un terminal en la carpeta *sibi-recomendacion* y ejecutamos el siguiente comando:

    ```
    npm install
    ```
- Después, para poner a funcionar el servidor, entramos a la carpeta *backend* y ejecutamos lo siguiente:
    ```
    node servidor.js
    ```
    Esto es el servidor de la plicación, que recibe peticiones y devuelve los datos, por lo que hay que dejarlo corriendo mientras usemos la aplicación
- Por último en un terminal en la carpeta *sibi-recomendacion* ejecutaremos el comando:
    ```
    npm run serve
    ```
    Para visualizar la aplicación introducimos en el navegador la dirección `http://localhost:8080/`

---


Adjunto mi cuaderno de trabajo de [OSF](https://osf.io/duzt9/?view_only=e55bffcad7d4459485a22cfb04daad7e).