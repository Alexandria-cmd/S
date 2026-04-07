<?php
// Папка для загрузки
$targetDir = "uploads/";
// Имя файла на сервере
$targetFile = $targetDir . basename($_FILES["my_file"]["name"]);

// Проверка: загружен ли файл
if(isset($_POST["submit"])) {
    // Проверка на ошибки при загрузке
    if ($_FILES["my_file"]["error"] == UPLOAD_ERR_OK) {
        // Попытка переместить файл из временной папки
        if (move_uploaded_file($_FILES["my_file"]["tmp_name"], $targetFile)) {
            echo "Файл ". basename( $_FILES["my_file"]["name"]). " успешно загружен.";
        } else {
            echo "Извините, произошла ошибка при загрузке.";
        }
    } else {
        echo "Ошибка загрузки: " . $_FILES["my_file"]["error"];
    }
}
?>
