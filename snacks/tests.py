from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Snack
from django.urls import reverse

# Create your tests here.

class Snacktest(TestCase) :
    def setUp(self) :
        self.user = get_user_model().objects.create_user(
            username='eman',
            email='amoonobeidat43@gmail.com',
            password='1234'
        )

        self.snack = Snack.objects.create(
            name='test',
            purchaser= self.user,
            desc='test description'
        )

    def test_str_method(self):
        expected_string = "test"  # Replace with the expected string representation of your Snack object
        self.assertEqual(str(self.snack), expected_string)

    def test_list_view(self):
        response = self.client.get(reverse("snacks_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "snacks_list.html")

    def test_detail_view(self):
            url = reverse('snacks_detail',args=[self.snack.id])  
            response = self.client.get(url)

            self.assertEqual(response.status_code,200)
            self.assertTemplateUsed(response,'snacks_detail.html')


    def test_create_view(self):
        url = reverse('snacks_create')
        data={
            "name": "test_2",
            "purchaser" : self.user.id,
            "description": 'test_02'
        }


        response = self.client.post(path=url,data = data,follow = True)
        self.assertTemplateUsed(response,'snacks_detail.html')
        self.assertEqual(len(Snack.objects.all()),2)
        self.assertRedirects(response, reverse('snacks_detail',args=[2]))

    def test_update_view(self):
       
        response = self.client.post(reverse('snack_update',args="1"),
                    {"name": "Updated name", "description": "description", "purchaser": self.user.id})
        
        self.assertRedirects(response, reverse('snacks_list'))

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)