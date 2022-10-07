<?php
        if (isset($_COOKIE['username']) && isset($_COOKIE['password'])) {
                setcookie('username', $_POST['username'], time()-(60*60*24*365));
                setcookie('password', md5($_POST['password']), time()-(60*60*24*365));
        }
        header('Location: login.html');
?>
cse@cse3140-HVM-domU:/var/www/html$ ^C
cse@cse3140-HVM-domU:/var/www/html$ cat register.php
<?php
if($_POST) {
                $fh = fopen("auth.txt", "a");
                $username = $_POST['username'];
                $password = $_POST['password'];
                $pwd = md5($password);
                fwrite($fh, $username . ":" . $pwd . "\n");
                fclose($fh);
                header('Location: login.html');
}

?>
<html>
        <head>
        </head>
        <body>
                <p><b>Register Here:</p></b>
                <form action = "" method = "POST">
                        Enter Username:<input type = "text" name = "username"><br/>
                        Enter Password:<input type = "text" name = "password"><br/>
                        <input type = "submit" value = "Register"><br/>
                </form>
        </body>
</html>
