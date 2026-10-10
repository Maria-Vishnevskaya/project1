import data
from sender_stand_request import post_create_order, get_order_by_track

def test_create_order_and_get_by_track():
    r_create = post_create_order(data.order_body)

    print("=== DEBUG: CREATE ORDER ===")
    print("URL:", r_create.request.url)
    print("Status code:", r_create.status_code)
    print("Body:", r_create.text)
    print("=============================")

    assert r_create.status_code == 201, f"Ожидался статус 201 при создании заказа, получен {r_create.status_code}"

    order_data = r_create.json()
    track_value = order_data.get("track")
    assert track_value, "В ответе на создание заказа отсутствует track"

    r_get = get_order_by_track(track_value)

    print("=== DEBUG: GET ORDER BY TRACK ===")
    print("Requested URL:", r_get.request.url)
    print("Status code:", r_get.status_code)
    print("Body:", r_get.text)
    print("==================================")

    assert r_get.status_code == 200, f"Ожидался статус 200 при получении заказа, получен {r_get.status_code}"