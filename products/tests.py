from django.test import Client, TestCase
from products.forms import EnquiryForm


class TestContact(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_200(self):
        response = self.client.get('/products/contact/')
        self.assertEqual(response.status_code, 200)

    def test_loaded_templates(self):
        response = self.client.get('/products/contact/')
        templates = response.templates
        name = get_name(templates)

        # self.assertIn('base.html', str(names))
        self.assertIn('contact.html', str(name))


    def test_contact_form_in_context(self):
        response = self.client.get('/products/contact/')
        form = response.context['enquiry_form']

        self.assertEqual(type(enquiry_form), ContactForm)




# from django.test import TestCase

# from products.models import Category


# class TestCategory(TestCase):
#     def setUp(self):
#         Category.objects.create(name='catone', friendly_name='First Category')
#         Category.objects.create(name='cattwo', friendly_name='')

#     def test_get_friendly_name(self):
#         catone = Category.objects.get(name='catone')
#         cattwo = Category.objects.get(name='cattwo')
#         self.assertEqual(catone.get_friendly_name(), 'First Category')
#         self.assertEqual(cattwo.get_friendly_name(), 'cattwo')


# Create your tests here.

# testing branches

# testing again

# ?and again

# ?and back again
