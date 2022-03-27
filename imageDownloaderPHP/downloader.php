<?php
    if(isset($_POST['imgUrl'])){
        $url = $_POST['imgUrl'];
        $filename = $_POST['filename'];
        $curl = curl_init($url);
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
        $downloadedImage = curl_exec($curl);
        $curl = curl_close($curl);
        header('Content-Type: image/jpg');
        header("Content-Disposition: attachment; filename=$filename.jpg");
        echo $downloadedImage;
    }
?>