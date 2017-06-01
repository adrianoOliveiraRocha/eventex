from django.test import TestCase
from django.core import mail


class SubscribePostValid(TestCase):
	def setUp(self):
		data = dict(name='Adriano Oliveira', cpf='85215856320', 
			email='adriano.qwe32@gmail.com', phone='85-99947-3839')
		self.client.post('/inscricao/', data)
		self.email = mail.outbox[0]

	def test_subscription_email_subject(self):
		expect = 'Confirmação de inscrição'
		self.assertEqual(expect, self.email.subject)

	def test_subscription_email_from(self):
		expect = 'contato@eventex.com.br'
		self.assertEqual(expect, self.email.from_email)

	def test_subscription_email_to(self):
		expect = ['contato@eventex.com.br', 'adriano.qwe32@gmail.com']
		self.assertEqual(expect, self.email.to)

	def test_subscription_email_body(self):
		contents = [
			'Adriano Oliveira',
			'85215856320',
			'adriano.qwe32@gmail.com',
			'85-99947-3839',
		]
		for content in contents:
			with self.subTest():
				self.assertIn(content, self.email.body)