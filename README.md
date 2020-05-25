# APM - Ansible package manager

### Why? 

Ansible-galaxy предлагает использовать meta/main.yml для описания зависимостей, однако не позволяет
установить их из этого файла. Вместо этого нам предлогают использовать reqs.txt с другим форматом (collections/roles)
И устанавливать через него с помощью ansible-galaxy install -r reqs.txt
И при установке роли, если в ней есть зависимость в meta/main то она будет установленна. Выходит
что meta/main подходит только для установки транзитивных зависимостей, что мне не нравится. 
Я считаю не верным иметь 2 разных метода установки зависимостей! (а ведь некоторые используют еще и GILT)

Чтобы избежать путаницы, и сложности, я написал мета пакет APM (Ansible Package Manager)
Который фокусируется на файле meta/main.yml как едином файле зависимостей. 
Пакетный менеджер может установить ваши зависимости из этого файла (под копотом, он конвертирует формат meta/main в reqs.txt и отправляет 
их в ansible-galaxy) что исключает лишнюю логику, и не дает ничему сломаться. Также по умолчанию APM использует 
локальную папку с ролями, а не устанавливает их в глобальную область видимости. 

Управлять поведением APM можно с помощью файла конфигурации .apmrc в папке пользователя глобально, или в папке проекта локально. 
Также через ENV (для удобства работы CI систем).

### Функционал

Сегодня функционал apm ограничен, он умеет лишь устанавливать зависимости из файла meta/main.yml
Проверять их наличие, и обрабатывать ошибки.

```
apm install
```

### Roadmap 

В будущем планируется добавить интересные вещи, как например. 
Возможность работы с частными gitlab инстансами, для поиска в них утилит, и работ cli
Например, имея роль Kafka в своем частном репозитории можно будет задать один (или несколько инстансов)
И устанавливать зависимости, как с глобального ansible-galaxy, так и с локального (частного) gitlab командой
```
apm install kafka
```
Данное действие установит зависимость в локальную папку, в файл meta/main.yml добавит необходимую запись, а также привяжет к текущему мажору версию. 

В будущем можно будет получать обновления версий, по команде
```
apm update 
```
Можно будет увидеть, в каких из зависимостей появились новые версии. 
Также есть вероятность, что можно будет проработать получение security обновлений уведомлением, при использовании роли!



