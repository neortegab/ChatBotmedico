# Frotend para ChatBot medico

---

Este es un proyecto en React que busca ser la interfaz de usuario de cara del chatbot medico desarrollado para el curso de Inteligencia Artificial.

## Alcance

---

En su forma inicial, esta interfaz sera sencilla, con pocos botones y validaciones. De forma que acepte una lista de síntomas en formato de lista separada por comas de forma que el chatbot pueda procesar los síntomas y proveer una prescripción.

Por lo tanto, en esta versión solamente se contará con:

- Punto de ingreso de los síntomas
- Botón de envío de síntomas
- Pantalla mostrando historial de síntomas y respuestas.

## Estructura

---

La aplicacion se conformara de una pagina principal, sin persistencia de usuario, conectada a un backend realizado en Flask (Python) que la conecte al modelo y así obtener las debidas interpretaciones.

## Instrucciones de instalación

---

### Requisitos

- Node 20

Para ejecutar el proyecto solo será necesario ejecutar los siguientes comandos desde la carpeta `/client`

```bash
npm i
```

```bash
npm run dev
```

Una vez ejecutados estos comandos, ingresar a un navegador web e introducir la ruta `localhost:5173` o `[::1]:5173`
