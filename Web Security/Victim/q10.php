<html>
<body>
        <h1>ERROR 404 PAGE NOT FOUND</h1>
<?php
        $uri = filter_var($_SERVER['REQUEST_URI'], FILTER_SANITIZE_SPECIAL_CHARS);
        $url = $protocol . $_SERVER['HTTP_HOST'] . $uri;

        echo "Page does not exist at: " . $url;
?>
        <h2>And if you're trying to hack us NICE TRY</h2>
        <div class="figure">
                <img src="https://thumbs.dreamstime.com/b/hacker-fail-to-log-data-centre-digital-animation-56175427.jpg"
                     alt="lol wrecked"
                     width="400"
                     height="341">

  <p>Get sauced on</p>
</div>
</body>
</html>
