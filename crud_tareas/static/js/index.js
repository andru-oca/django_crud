
function injecter(data){

            
    let appender = document.getElementById('to_append')

    let to_delete = document.querySelector('#to_append > div');

    if (to_delete != null){

        appender.removeChild(to_delete)
    }    
  
    let whole = ''
    
    let wholeNode = document.createElement('div');
    
    wholeNode.innerHTML = whole;
    
    
    
    if (data.length != 0){
        
        itemList = 1

        for (let i of data){
            
            
            let data_appender=`
            
            <div class="item">
               ${itemList++} :  ${i.fact}
            </div>   
                
            ` ; 
            
            whole += data_appender ; 

        }    

    }    
    else{
            
        whole = '<h2> No hay data disponible </h2>'
    }    
    
    wholeNode.innerHTML = whole;
    
    appender.appendChild(wholeNode);
    
}    

function injector(data){

    let appender = document.getElementById('details')

    let to_delete = document.querySelector('#details> div');

    if (to_delete != null){

        appender.removeChild(to_delete)
    }
 

    let wholeNode = document.createElement('div');
    
    let data_appender=`
    
    <div class="item">
    <h1>${data.nombre}</h1> 
    
        <ul>
        <li>Descripcion: ${data.descripcion}</li>
        <li>Horario de inicio de la tarea:  ${data.horario_inicio}</li>
        <li>Dia a realizarlo: ${data.dia_realizar}</li>
        </ul>
    
    </div>
    
    ` ; 
    
    wholeNode.innerHTML = data_appender;
    appender.appendChild(wholeNode);   
}




const URL = 'https://catfact.ninja/facts'

fetch(URL)
.then(data => data.json())
.then(data => injecter(data.data))
.catch(e => console.log(e))


let base_host = 'http://ander1987.pythonanywhere.com/api/'
let todo_list_url = 'todo/'

let path



document.addEventListener('click',

    e =>{

        if (e.target.tagName == "INPUT"){

            value_id = e.target.dataset.id
    
            if (value_id != null){

                path = `${base_host}${todo_list_url}${value_id}`
                
                fetch(path)
                .then(e => e.json())
                .then(e=> injector(e))

            }    

            return

        }    
        
    }    
)    


