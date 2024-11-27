<?php

class operadoresAritmeticos  {
 


    public function arit() {
        echo <<<'EOT'
        <pre>
        Suma: 10 + 5 = 15
        Resta: 10 - 5 = 5
        Multiplicación: 10 * 5 = 50
        División: 10 / 5 = 2
        Módulo: 10 % 5 = 0
        </pre>
EOT;
    }
}