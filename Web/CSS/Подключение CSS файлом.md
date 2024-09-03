Чтобы подключить CSS файл к HTML-документу, используется элемент `<link>` внутри тега `<head>`. Вот базовый пример:

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Пример подключения CSS</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Заголовок</h1>
    <p>Текст на странице.</p>
</body>
</html>
```

В этом примере CSS файл под именем `styles.css` подключается к HTML-документу. Файл `styles.css` должен находиться в той же директории, что и HTML-документ, или путь в `href` нужно указать относительно местоположения HTML-файла.

### Детали:
- **`rel="stylesheet"`** — указывает, что файл является таблицей стилей.
- **`href="styles.css"`** — путь к CSS файлу. Если CSS файл находится в другой папке, например в `css/styles.css`, нужно указать полный путь: `href="css/styles.css"`.

Если нужно подключить несколько CSS файлов, можно добавить дополнительные теги `<link>`:

```html
<link rel="stylesheet" href="reset.css">
<link rel="stylesheet" href="main.css">
```

Таким образом, HTML-документ будет использовать стили из всех подключенных файлов.