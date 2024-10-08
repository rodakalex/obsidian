Automake — это инструмент, который автоматически генерирует файлы `Makefile.in`, используемые для сборки программного обеспечения. Он работает в связке с Autoconf, который создает `configure` скрипты. Основная цель Automake — упростить процесс создания `Makefile` файлов и сделать сборку программ более стандартизированной и совместимой с различными системами.

### Основные функции Automake:

1. **Автоматизация создания `Makefile` файлов:** Automake генерирует `Makefile.in` файлы, которые затем используются `configure` скриптом для создания конечных `Makefile` файлов. Это упрощает процесс сборки и поддерживает стандарты GNU.

2. **Поддержка стандартов GNU:** Automake обеспечивает поддержку стандартов GNU для сборки, тестирования, установки и очистки программного обеспечения, что делает процесс сборки более предсказуемым и совместимым.

3. **Обработка зависимостей:** Automake автоматически обрабатывает зависимости между исходными файлами и объектными файлами, что упрощает управление сборкой.

### Основные компоненты:

- **`Makefile.am`:** Файл конфигурации для Automake, где определяются цели сборки, источники и другие параметры. Вы пишете в этом файле правила и зависимости, а Automake генерирует соответствующий `Makefile.in`.

- **`Makefile.in`:** Файл, создаваемый Automake, который содержит правила сборки, подготовленные для использования `configure` скриптом. `Makefile.in` является шаблоном, из которого `configure` создает окончательный `Makefile`.

### Как это работает:

1. **Создание `Makefile.am`:** Вы создаете файл `Makefile.am`, описывающий, как должны собираться ваши программы и библиотеки, какие файлы нужно включить и т.д.

2. **Генерация `Makefile.in`:** Запускаете команду `automake`, которая использует ваш `Makefile.am` для создания `Makefile.in`.

3. **Запуск `configure`:** Запускаете скрипт configure, который использует `Makefile.in`, чтобы создать конечный `Makefile`, учитывая конфигурацию вашей системы.

4. **Сборка программы:** Используете [[make]] для сборки программы согласно правилам в `Makefile`.

Использование Automake упрощает процесс сборки и помогает сделать ваш проект более совместимым с различными системами.