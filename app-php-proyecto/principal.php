<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
</head>

<body>

    <div class="container">
        <h3>PHP BÁSICO</h3>
        <ul>
            <ol>1. Operaciones con String</ol>
            <ol>2. Operadores Aritméticos</ol>
            <ol>3. Tipos de datos</ol>
            <ol>4. Operaciones con Array</ol>
            <ol>5. Condicionales</ol>
            <ol>6. Ciclos</ol>
            <ol>7. Salir</ol>
        </ul>

        <h6>Formulario</h6>
        <hr>

        <form method="POST" action="">
            <div class="mb-3">
                <label for="numero" class="form-label">Ingresar Número</label>
                <input type="number" name="numero" class="form-control" id="numero" placeholder="Insertar número" required>
            </div>
            <button type="submit" class="btn btn-outline-secondary">Enviar</button>
        </form>
        <hr>

        <?php
        include "./Padre.php";
        include "./OperacionesString.php";
        include "./OperadoresLogicos.php";
        include "./operadoresAritmeticos.php";
        


        if (isset($_POST["numero"])) {
            $opcion = $_POST["numero"];
            switch ($opcion) {
                case 1:
                    $operaciones = new OperacionesString();
                    $operaciones->funcionesString();
                    break;
                case 2:
                    $operaciones = new operadoresAritmeticos();
                    $operaciones->arit();
                    
                    break;
                case 3:
                    $operaciones = new tipoDeDatos();
                    $operaciones->tip();
                    break;
                case 4:
                    $operaciones = new tipoDeDatos();
                    $operaciones->tip();
                    break;
                case 5:
                    $operaciones = new tipoDeDatos();
                    $operaciones->tip();
                    break;
                case 6:
                    $operaciones = new tipoDeDatos();
                    $operaciones->tip();
                    break;
                default:
                    echo "Ingrese una opción válida.";
                    break;
            }
        }
        ?>
    </div>
</body>
</html>