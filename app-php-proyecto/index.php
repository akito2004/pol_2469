<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <p>paul andres alcos </p>
  <?php
  echo "imprimido de php </br>";
  $dato_1 = 1;
  $dato_2 = 2;

  // Asegúrate de usar paréntesis correctamente para la concatenación
  echo "el resultado es: " . ($dato_1 + $dato_2) . "</br>";
  echo "incremento: " . ($dato_1 + 1) . "</br>";

  // Usar llaves {} en lugar de paréntesis () para los bloques if
  if ($dato_2 == 2) {
      echo "no es igual</br>";
  } else if ($dato_2 === 100) {
      echo "si es igual</br>";
  }
  ?>

  <!-- crear 5 tipos de datos ---- -->
  <?php
  // Declaración de variables
  $nombre = "paul";        
  $edad = 30;               
  $altura = 1.75;           
  $esEstudiante = true;     
  $materias = array("Matemáticas", "Física", "Química"); // Una variable de tipo array

  // Imprimir las variables
  echo "Nombre: " . $nombre . "<br>";
  echo "Edad: " . $edad . "<br>";
  echo "Altura: " . $altura . "<br>";
  echo "Es estudiante: " . ($esEstudiante ? 'Sí' : 'No') . "<br>";
  echo "Materias: " . implode(", ", $materias) . "<br>";
  ?>

  <?php
  $materias = array("siuuu", "saoo", "souuu", "look", "abcd");
  $nombres = ["paul","pedro","pablo","ricardo"];
  $emojis = ["😀","🚀","🌟","😎","👍"];

  foreach($emojis as $item){
      echo $item ."</br>";
  }

  for ($i = 0; $i < count($materias); $i++) {
      echo "Materia " . ($i + 1) . ": " . $materias[$i] . "</br>";
  }
  $numeros = range(1, 12);

  foreach ($numeros as $numero) {
      echo "Tabla del $numero: <br>";

      for ($i = 1; $i <= 10; $i++) { // Cambiar a un bucle for para imprimir la tabla de multiplicar
          echo "$numero x $i = " . ($numero * $i) . "<br>";
      }
      echo "<br>";
  }
 
  ?>
  
</body>
</html>