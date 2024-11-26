const apiUrl ="file:///C:/laragon/www/App_php_js__chat_yes_no_senati/index.html#/api.php";
async function getData(){
    console.log('ingreso a getData');
    try {
        const respuesta = await fetch(`${apiUrl}?ID=123&nombre-paul&apellido_alcos`,{
            method:"GET"

        });
        const data = await respuesta.json();
        console.log(data);
        
    } catch (error) {
        console.log("error al  al momento de hacer la peticion  GET ", error);
        
    }

}
let botonGet = document.querySelector('.getData')
botonGet.addEventListener('click', function(){
    getData();
})