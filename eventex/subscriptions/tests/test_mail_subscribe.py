from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Henrique Bastos', cpf='12345678901',
                    email='jef720@trafficrobot.tk', phone='21-99618-6180')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'jef720@trafficrobot.tk'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['jef720@trafficrobot.tk', 'jef720@trafficrobot.tk']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Henrique Bastos',
                    '12345678901',
                    'jef720@trafficrobot.tk',
                    '21-99618-6180',
                    ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
                