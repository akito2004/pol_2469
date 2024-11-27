<?php
// ciclos.php
echo "<h4>Ciclos</h4>";

// Ciclo while
$i = 1;
echo "Ciclo while:<br>";
while ($i <= 5) {
    echo "Número: $i<br>";
    $i++;
}

// Ciclo for
echo "<br>Ciclo for:<br>";
for ($j = 1; $j <= 5; $j++) {
    echo "Número: $j<br>";
}

// Ciclo foreach
echo "<br>Ciclo foreach:<br>";
$array = array("manzana", "banana", "naranja");
foreach ($array as $fruta) {
    echo "Fruta: $fruta<br>";
}
?>