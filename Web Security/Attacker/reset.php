<?php
        if (isset($_COOKIE['username']) && isset($_COOKIE['password'])) {
                setcookie('username', $_POST['username'], time()-(60*60*24*365));
                setcookie('password', md5($_POST['password']), time()-(60*60*24*365));
        }
        header('Location: index.php');
?>
