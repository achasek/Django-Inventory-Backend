from django.test import TestCase
from .models import Item, Profile


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Item.objects.create(name='test')
        Item.objects.create(price=10)
        Item.objects.create(description='a description here')
        Item.objects.create(category='test')
        Item.objects.create(image='test.com')
        Profile.objects.create(username='test user')
        Profile.objects.create(password='password')

    def test_title_content(self):
        item = Item.objects.get(id=1)
        expected_object_name = f'{item.name}'
        self.assertEquals(expected_object_name, 'test')

    def test_association(self):
        item = Item.objects.get(id=1)
        user = Profile.objects.get(id=1)
        user.items.add(item)
        print(user.items.all())

    def test_description_content(self):
        item = Item.objects.get(id=1)
        expected_object_description = f'{item.description}'
        self.assertEquals(expected_object_description, 'a description here')
