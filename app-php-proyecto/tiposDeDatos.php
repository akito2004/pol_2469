
<?php

class tipoDeDatos  {
 

    public function tip() {
    }

    public function funcionesString() {
        echo <<<'EOT'
        <pre>
         $entero = 10; // Entero
        $flotante = 10.5; // Flotante
        $cadena = "Hola, mundo!"; // Cadena
        $booleano = true; // Booleano
        $array = array(1, 2, 3); // Array

        echo "Entero: $entero<br>";
        echo "Flotante: $flotante<br>";
        echo "Cadena: $cadena<br>";
        echo "Booleano: " . ($booleano ? 'true' : 'false') . "<br>";
        echo "Array: " . implode(", ", $array) . "<br>";
        </pre>
EOT;
    }
}