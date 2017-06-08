from datetime import datetime
from django.test import TestCase 
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):

	def setUp(self):
		self.obj = Subscription(
			name='Adriano Oliveira',
			cpf='85215856320',
			email='adriano.qwe32@gmail.com',
			phone='85-999473839'
		)
		self.obj.save()

	def test_create(self):
		self.assertTrue(Subscription.objects.exists())

	def test_created_at(self):
		"""Subscription must have an auto created attr"""
		self.assertIsInstance(self.obj.created_at, datetime)

	def test_str(self):
		self.assertEqual('Adriano Oliveira', str(self.obj))