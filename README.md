# Todo list API

## Descripción

API REST realizada para conectarse con proyecto TodoList con React. (Tarea día 21)

Implementa los siguientes Endpoints:

* [GET] /todos/user/<user_name>

Entrega una lista con todas las tareas por hacer del usuario indicado
```JavaScript
Content-Type: "application/json"
PARAMS: None
RESPONSE:
  [
    { label: "Make the bed", done: false },
    { label: "Walk the dog", done: false },
    { label: "Do the replits", done: false }
  ]
```
* [POST] /todos/user/<user_name>

Crea un nuevo usuario. 
Sólo es necesario enviar el nombre del nuevo usuario a través de la ruta.
```JavaScript
Content-Type: "application/json"
BODY: []
RESPONSE:
    {
        "result": "ok"
    }
```
* [PUT] /todos/user/<user_name>

Actualiza toda la lista de tareas del usuario indicado.
Se debe enviar una lista con las tarea del usuario.
```JavaScript
Content-Type: "application/json"
BODY:
  [
    { label: "Make the bed", done: false },
    { label: "Walk the dog", done: false },
    { label: "Do the replits", done: false }
  ]
RESPONSE:
    {
        "result": "ok"
    }
```
* [DELETE] /todos/user/<user_name>

Elimina un usuario y todas sus tareas.
```JavaScript
Content-Type: "application/json"
FORM PARAMS: none
RESPONSE:
  {
    "result": "ok"
  }
 ```
