<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yoeman's todo List</title>
    <link rel ="stylesheet" type="text/css" href="styletodo.css"> 
    <h1 style ="color:blue">WELCOME TO THE TODO LIST<h1>
</head>
<body>
   <div class="list container">
    <form action="addtask.php" method="post">
<b>Task Name:<b><br>
<input type="text" name="taskname" placeholder="Enter task name"><br>
<p>Indicate Starting time:<br><input type="time" name="starttime"></p>
<p> <input type="submit">

    </form>
</div>

    <ul>
        
    </ul>

   <?php $con=new mysqli("localhost", "root", "","todolist" );
   if ($con->connect_error){
    die("Connection failed:". $con->connect_error);
   }

   //retrieve tasks from database
   $sql="SELECT * from `tasks`";
   $result= $con->query($sql);

   if ($result -> num_rows >0){
      echo '<div class=Task-container">';
      echo '<h1>Your Tasks</h1>';
      echo '<ul>';
   while($row=$result->fetch_assoc()){
    echo  "<li> {$row['Task_id']}-{$row["Task_name"]}- {$row['Starting_time']}</li>" ;
   }
   echo "</ul>";
   echo "</div>";
   } else{
    echo "No tasks found.";
   }

   $con->close();
   ?>
<div class="actions">
<p><h2>YOUR TASKS MAY BE REMOVED HERE</h2></p>
   <form action="deletetask.php" method="post">
<p>Enter the Task ID of the task you wish to remove:</p>
<input type="number" name="deleteID" placeholder="Enter Task ID">
<input type="submit" >
   </form>


<h2>YOUR TASK STATUS MAY BE UPDATED HERE</h2><br>
<h3>They should be updated as follows: <br>
0:Cancelled task<br>
1:Completed task<br>
2:Pending task</h3>
   <form action="changetaskstatus.php" method="post">
<p>Enter the Task ID of the task you wish to update:</p>
<input type="number" name="updateID" placeholder="Enter Task ID">
<p>Enter the new status of the task:</p>
<input type="number" placeholder="Enter 0,1 or 2 as new status" name="newstatus">
<input type="submit" >
   </form>
</div>
    
</body>
</html>