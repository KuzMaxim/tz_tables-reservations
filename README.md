Сервис предоставляет REST API для управления бронированием столиков в ресторане. Решение включает все необходимые функции для работы с бронированиями и столиками, с проверкой доступности столиков в запрашиваемое время.

Доступные методы
Столы:

GET /tables/ - Список всех столиков

POST /tables/ - Добавить новый столик

DELETE /tables/{id} - Удалить столик

Бронь:

GET /reservations/ - Список всех бронирований

POST /reservations/ - Создать новое бронирование

DELETE /reservations/{id} - Отменить бронирование

Запуск

docker-compose build
docker-compose up