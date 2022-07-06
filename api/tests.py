import copy
import json
from datetime import datetime

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from shop.models import Shirt, Cap

test_checkout = {
    "Email sent:": {
        "subject": "Tu compra en IATI SHOP",
        "message": [
            "Este es un resumen de tu compra:",
            {
                "creation_date": "2022-05-29",
                "total_products": 1,
                "items": [
                    {
                        "product": {
                            "id": 4,
                            "description": "Shirt b Description 123",
                            "picture": "http://testserver/media/blue_red_Shirt_Woman.jpg",
                            "unitary_price": "24.63",
                        },
                        "quantity": 1
                    }
                ]
            },
            "Gracias por tu compra!",
            "IATI SHOP"
        ],
        "from": "iati_shop@example.es",
        "to": "user@example.es"
    }
}

test_add_to_cart = {
    "creation_date": datetime.now().strftime('%Y-%m-%d'),
    "total_products": 1,
    "items": [
        {
            "product": {
                "id": 4,
                "description": "Shirt b Description 123",
                "picture": "http://testserver/media/blue_red_Shirt_Woman.jpg",
                "unitary_price": "24.63",
            },
            "quantity": 1
        }
    ]
}

test_product_list = [
    {
        "id": 4,
        "creation_date": "2022-07-05",
        "primary_color": "red",
        "secondary_color": "orange",
        "brand": "nike",
        "picture": "http://testserver/media/blue_red_Shirt_Woman.jpg",
        "description": "Shirt b Description 123",
        "unitary_price": "24.63",
        "logo_color": "black"
        },
        {
        "id": 3,
        "creation_date": "2022-07-04",
        "primary_color": "white",
        "secondary_color": "black",
        "brand": "H&M",
        "picture": "http://testserver/media/blue_red_Shirt_Woman.jpg",
        "description": "Cap Description 123",
        "unitary_price": "29.69",
        "logo_color": "white"
    },
    {
        "id": 2,
        "creation_date": "2022-07-05",
        "primary_color": "red",
        "secondary_color": "orange",
        "brand": "nike",
        "picture": "http://testserver/media/blue_red_Shirt_Woman.jpg",
        "description": "Shirt Description 123",
        "unitary_price": "24.63",
        "size": "S",
        "type_of_fabric": "Cotton",
        "sizing": "Man",
        "hasSleeves": False,
    },
    {
        "id": 1,
        "creation_date": "2022-07-01",
        "primary_color": "navy blue",
        "secondary_color": "red",
        "brand": "adidas",
        "picture": "http://testserver/media/blue_red_Shirt_Woman.jpg",
        "description": "Shirt Description 123",
        "unitary_price": "29.69",
        "size": "M",
        "type_of_fabric": "Cotton",
        "sizing": "Woman",
        "hasSleeves": True,
    },
]
test_add_to_cart_2 = copy.deepcopy(test_add_to_cart)
test_add_to_cart_2["total_products"] = 10
test_add_to_cart_2["items"][0]["quantity"] = 10

test_add_to_cart_3 = copy.deepcopy(test_add_to_cart)
test_add_to_cart_3["creation_date"] = "2022-05-29"

test_add_to_cart_4 = copy.deepcopy(test_add_to_cart)
test_add_to_cart_4["creation_date"] = "2022-05-29"
test_add_to_cart_4["total_products"] = 10
test_add_to_cart_4["items"][0]["quantity"] = 10

test_cart = copy.deepcopy(test_add_to_cart)
test_cart["creation_date"] = "2022-05-29"


def generic_setup():

    shirt = Shirt(
        creation_date='2022-07-01',
        primary_color='navy blue',
        secondary_color='red',
        brand='adidas',
        picture='blue_red_Shirt_Woman.jpg',
        description='Shirt Description 123',
        unitary_price=29.69,
        size='M',
        type_of_fabric='Cotton',
        sizing='Woman',
        hasSleeves=True,
    )

    shirt_b = Shirt(
        creation_date='2022-07-05',
        primary_color='red',
        secondary_color='orange',
        brand='nike',
        picture='blue_red_Shirt_Woman.jpg',
        description='Shirt Description 123',
        unitary_price=24.63,
        size='S',
        type_of_fabric='Cotton',
        sizing='Man',
        hasSleeves=False,
    )

    cap = Cap(
        creation_date='2022-07-04',
        primary_color='white',
        secondary_color='black',
        brand='H&M',
        picture='blue_red_Shirt_Woman.jpg',
        description='Cap Description 123',
        unitary_price=29.69,
        logo_color='white',
    )

    cap_b = Cap(
        creation_date='2022-07-05',
        primary_color='red',
        secondary_color='orange',
        brand='nike',
        picture='blue_red_Shirt_Woman.jpg',
        description='Shirt b Description 123',
        unitary_price=24.63,
        logo_color='black',
    )

    shirt.save()
    shirt_b.save()
    cap.save()
    cap_b.save()


# Test product_lit
class Product_list_testCase(TestCase):

    def test_get_product_list(self):
        generic_setup()
        client = APIClient()

        response = client.get('/api/v1/product_list/')
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), test_product_list)


# test add_to_cart
class add_to_cart_testCase(TestCase):
    # test endpoint with product id
    def test_add_to_cart_1(self):
        generic_setup()
        client = APIClient()

        response = client.post('/api/v1/add_to_cart/4')
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), test_add_to_cart)

    # test endpoint with product id + quantity
    def test_add_to_cart_10(self):
        generic_setup()
        client = APIClient()

        response = client.post('/api/v1/add_to_cart/4/10')
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), test_add_to_cart_2)

    # test endpoint with product id + date
    def test_add_to_cart_date(self):
        generic_setup()
        client = APIClient()

        response = client.post('/api/v1/add_to_cart/4/2022-05-29')
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), test_add_to_cart_3)

    # test endpoint with product id + quantity + date
    def test_add_to_cart_date_10(self):
        generic_setup()
        client = APIClient()

        response = client.post('/api/v1/add_to_cart/4/10/2022-05-29')
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), test_add_to_cart_4)


# test check_cart
class check_cart_testCase(TestCase):

    def test_check_cart(self):
        generic_setup()
        client = APIClient()

        client.post('/api/v1/add_to_cart/4/2022-05-29')
        response = client.get('/api/v1/cart/2022-05-29')
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), test_cart)


# test check_out
class checkout_testCase(TestCase):
    # test checkout with creation date
    def test_checkout(self):
        generic_setup()
        client = APIClient()

        client.post('/api/v1/add_to_cart/4/2022-05-29')
        response = client.get('/api/v1/checkout/2022-05-29')
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), test_checkout)
