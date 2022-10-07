<?php
if (isset($_COOKIE['username']) && isset($_COOKIE['password'])) {
        $user = '';
        $pass = '';

        $pwd_file = 'auth.txt';
        $has_acct = false;

        $has_user = false;
        $has_pass = false;

        $f = fopen($pwd_file, "r");
        while(!feof($f)){
                $line = fgets($f, 4096);
                $user_pass = explode(":", $line);
                $comp_pass = substr($user_pass[1], 0, 32);
                if(($_COOKIE['username'] == $user_pass[0]) && ($_COOKIE['password'                                                                            ] == $comp_pass)){
                        //header('Location: place.html');
                        $has_acct = true;
                        break;
                }
        }
        fclose($f);
        if (!$has_acct && (($_COOKIE['username'] != $user) || ($_COOKIE['password'                                                                            ] != md5($pass)))) {
                header('Location: login.html');
        }
        else {
                echo 'Welcome back ' . $_COOKIE['username'];
                //setcookie('username', $_POST['username'],time(), $httponly = tru                                                                            e);
                //setcookie('password', md5($_POST['password']), $httponly = true)                                                                            ;
        }
}
else{
        header('Location: login.html');
}
if($_POST){
                if(empty($_POST['name'])){
                        $name = $_COOKIE['username'];
                }
                else{
                        $name = $_POST['name'];
                }
                $content = filter_var($_POST['commentContent'], FILTER_SANITIZE_SP                                                                            ECIAL_CHARS);
                $handle = fopen("comments.html", "a");
                fwrite($handle, "<b>" . $name . "</b>:<br/>" . $content . "<br/>")                                                                            ;
                fclose($handle);
}

?>
<html>
        <head>
        <script>
                var message = "Hello, world it's section 3 group 10 Ryan Brown and                                                                             Daniel Paliulis"
        </script>
                <button type = "button" onclick = "document.write(message)">Press                                                                             Here</button>
        </head>
        <body>
                <p><b>Welcome to the best group</b></p>
                <p><i>That group being us, Ryan Brown and Daniel Paliulis</i></p>
                <p><b>Things We Like About the Lab:</b></p>
                <li>Writing Websites</li>
                <li>Cybersecurity stuff</li>
                <button type = "button" onclick = "window.location.href = 'registe                                                                            r.php'">Register</button>
                <form action = "logout.php" method = "POST">
                        <input type = "submit" value = "logout"><br/>
                </form>
                <form action = "" method = "POST">
                        Enter Name:<input type = "text" name = "name"><br/>
                        Enter Comment: <textarea rows = "10" cols = "30" name = "c                                                                            ommentContent"></textarea><br/>
                        <input type = "submit" value = "Post!"><br/>
                </form>
                <p><b>Comments:</b></p>
                <?php include "comments.html";?>
        </body>
</html>
