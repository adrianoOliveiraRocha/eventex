from django.test import TestCase
from eventex.core.models import Talk
from eventex.core.managers import PeriodManager


class TalkModelTest(TestCase):
    def seTup(self):
        self.talk = Talk.objects.create(
                title='Título da Palestra',
                start='10:00',
                description='Descrição da Palestra.'
                )

#    def test_create(self):
#        self.assertTrue(Talk.objects.exists())


class PeriodManagerTest(TestCase):
    def SetUp(self):
        Talk.objects.create(title='Morning Talk', start='11:59')
        Talk.objects.create(title='Afternoom Talk', start='12:00')

    def test_manager(self):
        self.assertIsInstance(Talk.objects, PeriodManager)

#    def test_at_morning(self):
#        qs = Talk.objects.at_morning()
#        expected = ['Morning Talk']
#        self.assertQuerysetEqual(qs, expected, lambda o: o.title)
#
#    def test_at_afternoon(self):
#        qs = Talk.objects.at_afternoon()
#        expected = ['Afternoom Talk']
#        self.assertQuerysetEqual(qs, expected, lambda o: o.title)
