from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import *

# Create your tests here.

class CRUDTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'adminn',
            email = 'adminn@adminn.com',
            password = '123456adminn'
        )
        self.crud = Crud_r.objects.create(
            title = 'test me',
            author = self.user,
            body = 'i hate myself'
        )

    def test_status(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_details_status(self):
        response = self.client.get(reverse('crud_detail', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_details_content(self):
        response = self.client.get(reverse('crud_detail', args='1'))
        self.assertContains(response, 'test me')

    def test_update(self):
        response = self.client.post(reverse('crud_update', args='1'), {
            'body': 'i hate myself',
        })
        self.assertContains(response, 'i hate myself')
