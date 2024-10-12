from app.orders.models import Order, Address
from app.cookies.models import Cookie


def test_get_checkout_renders(client):
    # page loads and renders checkout
    response = client.get("/orders/checkout")
    assert b"Checkout" in response.data


def test_post_checkout_creates_order(client):
    # creates an order record
    response = client.post(
        "/orders/checkout",
        data={
            "chocolate-chip": 2,
            "name": "John Doe",
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "90210",
            "country": "USA",
        },
    )

    assert Order.query.first() is not None


def test_post_checkout_creates_address(client):
    # creates an address related to the order
    response = client.post(
        "/orders/checkout",
        data={
            "chocolate-chip": 2,
            "name": "John Doe",
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "90210",
            "country": "USA",
        },
    )
    assert Address.query.first().order_id is 1


def test_post_checkout_creates_cookie_order(client):
    # creates a cookie order related to the order
    new_cookie = Cookie(slug="chocolate-chip", name="Chocolate Chip", price="1.50")
    new_cookie.save()

    response = client.post(
        "/orders/checkout",
        data={
            "chocolate-chip": 2,
            "name": "John Doe",
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "90210",
            "country": "USA",
        },
    )

    assert Order.query.first().cookie_orders[0].number_of_cookies == 2
