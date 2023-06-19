from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack
from django.contrib.auth import get_user_model


class ThingsTests(TestCase):

    def test_list_page_status_code(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snacks.html')
        self.assertTemplateUsed(response, 'base.html')

    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='test',
            email='teas@email.com',
            password='1234'
        )

        self.snack = Snack.objects.create(
            name='test',
            description="test info",
            purchaser = self.user
        )

    def test_str_method(self):
        self.assertEqual(str(self.snack),"test")

    def test_detail_view(self):
        url = reverse('snack_detail', args=[self.snack.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snack_detail.html')

    def test_create_view(self):
        obj={
            'name':"test2",
            'description': "tasty test",
            'purchaser': self.user.id
        }

        url = reverse('snack_create')
        response = self.client.post(path=url,data=obj,follow=True)
        self.assertRedirects(response, reverse('snack_detail', args=[2]))


    def test_snacks_page_context(self):
        url = reverse('snacks')
        response = self.client.get(url)
        snack_list = response.context['Snacks']
        self.assertEqual(len(snack_list), 1)
        self.assertEqual(snack_list[0].name, "test")
        self.assertEqual(snack_list[0].description,'test info')
        self.assertEqual(snack_list[0].purchaser.username, "test")

    def test_detail_page_context(self):
        url = reverse('snack_detail',args=(1,))
        response = self.client.get(url)
        snack_detail = response.context['snack']
        self.assertEqual(snack_detail.name, "test")
        self.assertEqual(snack_detail.description, 'test info')
        self.assertEqual(snack_detail.purchaser.username, "test")
    
    def test_update_view(self):
        obj={
            'name':"test2",
            'description': "tasty test",
            'purchaser': self.user.id
        }

        url = reverse('snack_update',args=[1])
        response = self.client.post(path=url,data=obj,follow=True)
        self.assertRedirects(response, reverse('snacks'))

    def test_delete_view(self):

        url=reverse('snack_delete',args=[1])
        response = self.client.post(path=url,follow=True)
        self.assertRedirects(response,reverse('snacks'))