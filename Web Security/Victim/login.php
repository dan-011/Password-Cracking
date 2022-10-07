<?php
/* These are our valid username and passwords */
if(!empty($_COOKIE['username']) && !empty($_COOKIE['password'])){
        header('Location: index.php');
}
if (isset($_POST['username']) && isset($_POST['password'])) {
        $user = '';
        $pass = '';
        $pwd_file = 'auth.txt';
        $has_acct = false;

        $f = fopen($pwd_file, "r");
        while(!feof($f)){
                $line = fgets($f, 4096);
                $user_pass = explode(":", $line);
                $comp_pass = substr($user_pass[1], 0, 32);
                if(($_POST['username'] == $user_pass[0]) && (md5($_POST['password']) == $comp_pass)){
                        //header('Location: place.html');
                        $has_acct = true;
                        break;
                }
        }
        fclose($f);
        if(($_POST['username'] == $user && $_POST['password'] == $pass) || $has_acct){
                //header('Locaiton: place.html');}}
                if (isset($_POST['rememberme'])) {
                        setcookie('username', $_POST['username'], time()+60*60*24*365, $httponly = false);
                        setcookie('password', md5($_POST['password']), time()+60*60*24*365, $httponly = false);
                }
                else{
                        setcookie('username', $_POST['username'], $httponly = false);
                        setcookie('password', md5($_POST['password']), $httponly = false);
                }
                header('Location: index.php');
        }
        else {
                echo "Invalid Username/Password";
        }
}
else{
        echo 'You must supply a username and password.';
}
?>
