from django.test import TestCase
from django.urls import reverse
from .models import Category
from user.models import CustomUser

class ViewsTestCase(TestCase):
    def test_home_page_load(self):
        Category.objects.create(title='test', slug='test')
        Category.objects.create(title='test2', slug='test2')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_catalog_page_load(self):
        response = self.client.get('/catalog/dveri/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog.html')

    def test_profile_page_load(self):
        user = CustomUser.objects.create(username='admin',password='admin')
        self.client.force_login(user)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile.html')

    def test_signin_page_load(self):
        response = self.client.get('/auth/signin/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'user/signin.html')

    def test_login_page_load(self):
        response = self.client.get('/auth/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/login.html')

    def test_cart_page_load(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart_detail.html')

    def test_contact_page_load(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")
     

