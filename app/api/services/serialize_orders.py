def serialize_cookie_orders(cookie_orders):
    cookie_orders_list = []

    for cookie_order in cookie_orders:
        cookie_orders_list.append(
            {
                "cookie_id": cookie_order.cookie_id,
                "number_of_cookies": cookie_order.number_of_cookies,
                "cookie_name": cookie_order.cookie.name,
            }
        )

    return cookie_orders_list


def serialize_orders(orders):
    orders_list = []

    for order in orders:
        orders_list.append(
            {
                "id": order.id,
                "date": order.date.strftime("%Y-%m-%d %H:%M:%S"),
                "address": {
                    "city": order.address.city,
                    "country": order.address.country,
                    "name": order.address.name,
                    "state": order.address.state,
                    "street": order.address.street,
                    "zip": order.address.zip,
                },
                "cookie_orders": serialize_cookie_orders(order.cookie_orders),
            }
        )

    return orders_list
