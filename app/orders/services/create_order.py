from app.orders.models import Order, Address, CookieOrder


def create_order(form_data, cookies):
    order = Order()
    order.save()

    address = Address(
        name=form_data.get("name"),
        street=form_data.get("street"),
        city=form_data.get("city"),
        state=form_data.get("state"),
        zip=form_data.get("zip"),
        country=form_data.get("country"),
        order=order,
    )
    address.save()

    for cookie in cookies:
        number_of_cookies = form_data.get(cookie.slug, 0)

        if int(number_of_cookies) > 0:
            cookie_order = CookieOrder(
                cookie=cookie, order=order, number_of_cookies=number_of_cookies
            )
            cookie_order.save()
