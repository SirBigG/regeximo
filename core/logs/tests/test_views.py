from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from django.urls import reverse


class LogParseFormViewTests(TestCase):

    def test_response_get(self):
        response = self.client.get(reverse('logs:parse'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'logs/log_parse_form.html')

    def test_response_post(self):
        _file = SimpleUploadedFile('file.txt', b'test content', content_type='text')
        response = self.client.post(reverse('logs:parse'), data={'site_name': 'site', 'file': _file})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')


class IndexViewTests(TestCase):
    def test_using_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
