# # Мария Вишневская, 48-я когорта — Финальный проект. Инженер по тестированию плюс
import data
from sender_stand_request import post_create_order, get_order_by_track

def test_create_order_returns_201_and_has_track():
    r_create = post_create_order(data.order_body)
    assert r_create.status_code == 201, f"Не удалось создать заказ: статус {r_create.status_code}"

    order_data = r_create.json()
    track_value = order_data.get("track")
    assert track_value, "В ответе нет поля track"


def test_get_order_by_track_returns_200():
    
    r_create = post_create_order(data.order_body)
    assert r_create.status_code == 201

    order_data = r_create.json()
    track_value = order_data["track"]

    r_get = get_order_by_track(track_value)
    assert r_get.status_code == 200, f"Не удалось получить заказ: статус {r_get.status_code}"