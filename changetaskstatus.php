<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    if($_SERVER["REQUEST_METHOD"]=="POST"){
        $updateID=$_POST["updateID"];
        $newstatus=$_POST["newstatus"];
    }
    $validstatuses=[0,1,2];
    if(!in_array($newstatus, $validstatuses)){
        echo "Invalid status";
        exit();
    }


    $con= new mysqli("localhost", "root", "", "todolist");
    if ($con->connect_error){
        die("Connection failed:". $con->connect_error);
    }

    $sql="UPDATE `tasks` SET `Task_status`='$newstatus' WHERE `Task_id`=$updateID";
    if ($con->query($sql)===TRUE){
    header("Location: index.php"); 
    exit();   
    }else{
        echo "Error:". $sql. "<br>". $con->error;
    }
    $con->close();
    ?>
</html>