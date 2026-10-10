headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Анатолий",
    "phone": "+79995553322",
    "address": "г. Москва, ул. Пушкина, д. 10"
}

products_ids = {
    "ids": [1, 2, 3]
}

order_body = {
    "firstName": "Ivanov Ivan",
    "items": [
        {"products_ids": 1, "quantity": 1}
    ],
    "address": "г. Москва, ул. Пушкина, д. 10"
}
