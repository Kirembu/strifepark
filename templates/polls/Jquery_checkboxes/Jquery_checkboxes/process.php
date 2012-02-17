<?php
require ('lib/Database.class.php');
$db->connect();
    foreach ($_POST['deleteCB'] as $value)
    {
      $query_delete = "DELETE FROM events WHERE id='$value'";
      $db->query($query_delete);
    }
$db->close();
?>

