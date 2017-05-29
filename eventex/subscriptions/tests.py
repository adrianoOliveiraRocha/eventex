from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from django.core import mail

class SubscribeTest(TestCase):
	def setUp(self):
		self.resp = self.client.get('/inscricao/')
	def test_get(self):
		""" GET /inscricao must status code 200 """
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		"""Must use subscriptions/subscription_form.html"""
		self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

	def test_html(self):
		"""HTML must contain input tags"""
		self.assertContains(self.resp, '<form')
		self.assertContains(self.resp, '<input', 6)
		self.assertContains(self.resp, 'type="text"', 3)
		self.assertContains(self.resp, 'type="email"')
		self.assertContains(self.resp, 'type="submit"')

	def test_csrf(self):
		"""html must contain csrf"""
		self.assertContains(self.resp, 'csrfmiddlewaretoken')

	def test_has_form(self):
		"""Context must have subscription form"""
		form = self.resp.context['form']
		self.assertIsInstance(form, SubscriptionForm)

	def test_form_has_fields(self):
		"""Form must have four fields"""
		form = self.resp.context['form']
		self.assertSequenceEqual(['name','cpf','email','phone'], list(form.fields))


class SubscriptionPostTest(TestCase):
	def setUp(self):
		data = dict(name='Adriano Oliveira', cpf='85215856320', 
			email='adriano.qwe32@gmail.com', phone='85-99947-3839')
		self.resp = self.client.post('/inscricao/', data)

	def test_post(self):
		"""Valid post should redirect to /inscricao/"""
		
		self.assertEqual(302, self.resp.status_code)

	def test_subscription_send_email(self):
		self.assertEqual(1, len(mail.outbox))

	def test_subscription_email_subject(self):
		email = mail.outbox[0]
		expect = 'Confirmação de inscrição'

		self.assertEqual(expect, email.subject)

	def test_subscription_email_from(self):
		email = mail.outbox[0]
		expect = 'contato@eventex.com.br'

		self.assertEqual(expect, email.from_email)

	def test_subscription_email_to(self):
		email = mail.outbox[0]
		expect = ['contato@eventex.com.br', 'adriano.qwe32@gmail.com']

		self.assertEqual(expect, email.to)

	def test_subscription_email_body(self):
		email = mail.outbox[0]
		
		self.assertIn('Adriano Oliveira', email.body)
		self.assertIn('85215856320', email.body)
		self.assertIn('adriano.qwe32@gmail.com', email.body)
		self.assertIn('85-99947-3839', email.body)


class SubscribInvalidPost(TestCase):
	def setUp(self):
		self.resp = self.client.post('/inscricao/', {})

	def test_post(self):
		"""Invalid post should not redirect"""
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

	def test_has_form(self):
		form = self.resp.context['form']
		self.assertIsInstance(form, SubscriptionForm)

	def test_form_has_errors(self):
		form = self.resp.context['form']
		self.assertTrue(form.errors)