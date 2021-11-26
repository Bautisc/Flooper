// Selectores
var input_Tareas = document.querySelector(".input-tareas");
var tareas_Btn = document.querySelector(".tareas-btn");
var lista_Tareas = document.querySelector(".lista-tareas");
var filtros = document.querySelector(".filtros-tareas")

//Eventos
tareas_Btn.addEventListener('click', AgregarTarea);
lista_Tareas.addEventListener('click', completarBorrar)
filtros.addEventListener('click', filtroTareas)

//Funciones
function AgregarTarea(event){
        //Esto evita que se recargue la página cada vez que se agrega una tarea.
    event.preventDefault();
        //Generar div que contiene las tareas
    const div_Tareas = document.createElement("div");
    div_Tareas.classList.add("tareas");
        //Esto genera un li que contiene la tarea
    const nueva_Tarea = document.createElement('li');
    nueva_Tarea.innerText = input_Tareas.value;
    nueva_Tarea.classList.add('item-tareas');
    div_Tareas.appendChild(nueva_Tarea);

    //Esto genera los botones de completado y eliminar dentro del div

    const completedButton = document.createElement('button');
    completedButton.innerHTML = '<i class="fas fa-check"></i>';
    completedButton.classList.add("completar-btn");
    div_Tareas.appendChild(completedButton)

    const deleteButton = document.createElement('button');
    deleteButton.innerHTML = '<i class="fas fa-trash"></i>';
    deleteButton.classList.add("eliminar-btn");
    div_Tareas.appendChild(deleteButton)
    
    //Agregar nuestro nuevo div a la lista de tareas
    lista_Tareas.appendChild(div_Tareas)
    // Limpiar valor del input-tareas
    input_Tareas.value = "";
}

function completarBorrar(e){
    const item = e.target;
    //Borrar tarea
    if(item.classList[0] === 'eliminar-btn'){
        const tarea = item.parentElement;

        tarea.classList.add('fall')
        tarea.addEventListener('transitionend', function(){
            tarea.remove()
        })
    }
    //Completar tarea
    if (item.classList[0] === 'completar-btn') {
        const tarea = item.parentElement;
        tarea.classList.toggle("completada");
 }   
}
function filtroTareas(e){
    const tareas = lista_Tareas.childNodes;
    tareas.forEach(function(tareas){
        switch (e.target.value) {
            case "todas":
                tareas.style.display = "flex"
                break;
            case "completas":
                if(tareas.classList.contains('completada')){
                    tareas.style.display = "flex";
                } else {
                    tareas.style.display = "none"
                }
                break
            case "incompletas":
                if(!tareas.classList.contains('completada')){
                    tareas.style.display = "flex";
                }  else {
                    tareas.style.display = "none"
                }
                break
        }
    })
}

 
//Guardar las tareas en el cache

function guardarTareas(tarea){
    //Con esto se verifica si ya se tienen tareas guardadas
    let tareas;
    if(localStorage.getItem('tareas') === null){
        tareas = [];
    }else{
        tareas = JSON.parse(localStorage.getItem('tareas'));
    }
    tareas.push(tarea)
    localStorage.setItem('tareas', JSON.stringify(tareas));
}