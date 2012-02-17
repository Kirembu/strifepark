<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Database setup</title>
</head>
<body>
<h1>Setup</h1>
<?php if (!isset($_POST['submit'])) { ?>
			<form name="setup" action="<?php $_SERVER['PHP_SELF']?>" method="post">
    				<input type="submit" value="Setup" name="submit" />
			</form>
<?php
			}
	else
    		{
    		$success='';
			//radio section is for the radio button tutorial.
			require ('Database.class.php');
			$db->connect();
			$query= "CREATE TABLE IF NOT EXISTS events(
			id int(1) NOT NULL auto_increment,
			event text NOT NULL,
			primary key (id))";

			$success=$db->query($query);
			$data   ['id'] = '1' ;$data    ['event'] = 'Test 1';
			$data1  ['id'] = '2' ;$data1   ['event'] = 'Test 2';
			$data2  ['id'] = '3' ;$data2   ['event'] = 'Test 3';
            $data3  ['id'] = '4' ;$data3   ['event'] = 'Test 4';
            $data4  ['id'] = '5' ;$data4   ['event'] = 'Test 5';
			$data5  ['id'] = '6' ;$data5   ['event'] = 'Test 6';
			$data6  ['id'] = '7' ;$data6   ['event'] = 'Test 7';
            $data7  ['id'] = '8' ;$data7   ['event'] = 'Test 8';
            $data8  ['id'] = '9' ;$data8   ['event'] = 'Test 9';
			$data9  ['id'] = '10';$data9   ['event'] = 'Test 10';
			$data10 ['id'] = '11';$data10  ['event'] = 'Test 11';
            $data11 ['id'] = '12';$data11  ['event'] = 'Test 12';

			$db->query_insert("events", $data);
			$db->query_insert("events", $data1);
			$db->query_insert("events", $data2);
			$db->query_insert("events", $data3);
			$db->query_insert("events", $data4);
			$db->query_insert("events", $data5);
			$db->query_insert("events", $data6);
			$db->query_insert("events", $data7);
			$db->query_insert("events", $data8);
			$db->query_insert("events", $data9);
			$db->query_insert("events", $data10);
			$db->query_insert("events", $data11);



			if ($success)
				{
    				header('Location: ../index.php');
				}

   	 }?>
</body>
</html>

