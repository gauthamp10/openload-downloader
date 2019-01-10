<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>OPen Load</title>
</head>
<body>
	<?php
    $URI='https://openload.co/f/zb9lNKP6EPE';
    $data = file_get_contents($URI);
    preg_match_all('/<a[^>]+>/i', $data, $result);
    echo $data
	  ?>
</body>
</html>