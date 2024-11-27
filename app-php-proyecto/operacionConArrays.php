<?php

class tipoDeDatos  {
 

    public function tip() {
    }

    public function funcionesString() {
        echo <<<'EOT'
        <pre>
       $array = array("manzana", "banana", "naranja");

// Agregar un elemento
$array[] = "uva";

// Imprimir el array
echo "Array: " . implode(", ", $array) . "<br>";

// Acceder a un elemento
echo "Primer elemento: " . $array[0] . "<br>";

// Contar elementos
echo "Número de elementos: " . count($array) . "<br>";
        </pre>
EOT;
    }
}