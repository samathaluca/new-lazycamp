from django.test import TestCase

from campspots.models import Category


class TestCategory(TestCase):
    def setUp(self):
        Category.objects.create(name='catone', friendly_name='First Category')
        Category.objects.create(name='cattwo', friendly_name='')

    def test_get_friendly_name(self):
        catone = Category.objects.get(name='catone')
        cattwo = Category.objects.get(name='cattwo')
        self.assertEqual(catone.get_friendly_name(), 'First Category')
        self.assertEqual(cattwo.get_friendly_name(), 'cattwo')
