<?php



$metodo = $_SERVER('REQUEST_METHOD');

$respuesta= [];
switch ($variable) {
    case 'GET':
        $respuesta=[
            'mensaje'=>'metodp Get Correcto',
             'data'=> $_GET
    ];
        break;
    
    default:
        # code...
        break;
}
echo json_encode ($respuesta);