from django.test import TestCase
from .models import Home


class TestViews(TestCase):

    def test_home(self):
        """tests the home page renders"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_404(self):
        """tests a 404 error is raised"""
        response = self.client.get('/this_doesnt_exist/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
        self.assertTemplateUsed(response, 'base.html')


class TestModels(TestCase):

    def test_home_count(self):
        """tests a home object can be added to the db"""
        self.assertEqual(len(Home.objects.all()), 0)
        self.home = Home(content="This is the content", address="an address")
        self.home.save()
        self.assertEqual(len(Home.objects.all()), 1)

    def test_home_content(self):
        """tests the home object has the correct content"""
        self.home = Home(content="This is the content", address="an address")
        self.home.save()
        home_instance = Home.objects.all().first()
        self.assertEqual(home_instance.content, "This is the content")
        self.assertEqual(home_instance.address, "an address")
