<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <link href="css/admin.css" rel="stylesheet" type="text/css" />
        <link href="css/jquery-ui-1.8.7.custom.css" type="text/css" rel="stylesheet" />
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js"></script>
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.7/jquery-ui.min.js"></script>
        <script type="text/javascript" src="checkbox.js"></script>

        <title> All Events</title>
</head>
<body>
      <h1>PHP Checkbox Array Tutorial</h1>
            <div id="dialog-confirm" title="Delete Item(s)?">
                <p><span class="ui-icon ui-icon-alert" style="float:left; margin:0 7px 20px 0;">nbsp;</span>
                These items will be permanently deleted and cannot be recovered. Are you sure?</p>
            </div>
            <?php
                require('lib/Database.class.php');
                  $db->connect();
                    $query='SELECT * FROM events';
                    $rows=$db->query($query);

                  if (mysql_num_rows($rows)) {?>
                         <form name='delete_form' id='delete_form' action='' method='post'>
                               <input type="checkbox" id="selectAll" name="deleteCB[]"  /><br/>
                            <?php while ($result = $db->fetch_array($rows))
                                {
                                    $id = $result['id'];
                                    $event = $result['event'];
                                    echo "<input type='checkbox' name='deleteCB[]' value='$id' />$event<br/>";
                                }
                                echo "<input type='submit' id='deleteBtn' value='Delete' name='deleteBtn' />";
                                echo "</form>"; }  //end if?>
</body>
</html>

