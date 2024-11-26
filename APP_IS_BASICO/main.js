/*//alert ( "paul andres alcos escobar ");

let nombre = "paul andres alcos escobar" 
const Sigla_Senati ="KDIBSVLDSJ";

console.log(Sigla_Senati);
console.log(nombre);



//Arrays
let edades =[23, 45, 1 ,13 ,15 ,100];
for(let i=0; i<edades.length; i++){
    console.log(edades[i]);

}
for(let item of edades){
    console.log(item);
}
edades.forEach(function(edad){
    console.log(edad);
});
edades.map(function(e){
    
    if (e > 18) {
        console.log(e + " es mayor de edad");
    } else {
        console.log(e + " es menor o igual a 10");
    }
});
//funcion normal
//function nombreFuncion(){

//}
//uncion anonima 
///funcion (){

//}


    //eventos en js
    let butonhtml = document.getElementById('prueba');
    //butonhtml.addEventListener('click',function(e){
    // console.log("alguien hizo click")


    //butonhtml.addEventListener('mouseover',function(e){
    //console.log("mouse encima del boton")


    //butonhtml.addEventListener('mouseout',function(e){
    //console.log("mouse fuera del boton")
            
    //focus_plica colores cuando selelccionas el  boton 
    //buttonHTML.addEventListener('focus', function (e) {
    // console.log("boton enfocado");  
    //blur:revertir los  estilos  aplicados  cuando el boton pierde el foco    
    //buttonHTML.addEventListener('blur', function (e) {
    // console.log("boton desenfocado");
    buttonHTML.addEventListener('dblclick', function (e) {
        console.log("boton doble clickeado");

    })
*/

// Declaraciones de variables
let nombre = "paul andres alcos escobar"; 
const Sigla_Senati = "KDIBSVLDSJ";

// Salida de las variables en la consola
console.log(Sigla_Senati);
console.log(nombre);

// Arreglos (Arrays)
let edades = [23, 45, 1, 13, 15, 100];

// Recorrer el arreglo usando forEach
edades.forEach(function(edad) {
    console.log(edad);
});

// Usar map para verificar si cada edad es mayor de 18
edades.map(function(e) {
    if (e > 18) {
        console.log(e + " es mayor de edad");
    } else {
        console.log(e + " es menor o igual a 18");
    }
});

// Manejo de eventos en JavaScript
let buttonHTML = document.getElementById('prueba');

// Agregar escuchadores de eventos al botón
buttonHTML.addEventListener('click', function(e) {
    console.log("alguien hizo click");
});

buttonHTML.addEventListener('mouseover', function(e) {
    console.log("mouse encima del botón");
});

buttonHTML.addEventListener('mouseout', function(e) {
    console.log("mouse fuera del botón");
});

// Evento de enfoque - cuando el botón está enfocado
buttonHTML.addEventListener('focus', function(e) {
    console.log("botón enfocado");  
});

// Evento de desenfoque - cuando el botón pierde el foco
buttonHTML.addEventListener('blur', function(e) {
    console.log("botón desenfocado");
});

// Evento de doble clic
buttonHTML.addEventListener('dblclick', function(e) {
    console.log("botón doble clickeado");

});
// Evento mouseup - cuando se suelta el botón del mouse
buttonHTML.addEventListener('mouseup', function(e) {
    console.log("botón soltado");
    buttonHTML.style.backgroundColor = ""; // Restaura el color de fondo
});

// Evento contextmenu - clic derecho
buttonHTML.addEventListener('contextmenu', function(e) {
    e.preventDefault(); // Previene el menú contextual
    console.log("clic derecho en el botón");
});

// Evento de animación - cuando se añade una clase de animación
buttonHTML.addEventListener('animationstart', function(e) {
    console.log("animación iniciada");
});

// Evento de animación - cuando se termina una animación
buttonHTML.addEventListener('animationend', function (e) {
    console.log("animación finalizada");
});