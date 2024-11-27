<?php

class OperacionesString extends Padre {
 

    public function llamarPadre() {
        parent::saludo();
    }

    public function funcionesString() {
        echo <<<'EOT'
        <pre>
        strlen():  Esto imprimirá la longitud de la cadena
        strtolower():  Esto imprimirá la cadena en minúsculas
        strtoupper():  Esto imprimirá la cadena en mayúsculas
        substr():  Esto imprimirá "Hola"
        str_replace(): Esto reemplazará "mundo" por "amigo"
        </pre>
EOT;
    }
}