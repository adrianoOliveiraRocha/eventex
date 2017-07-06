from django.test import TestCase
from eventex.core.models import Talk, Course
from eventex.core.managers import PeriodManager


class TalkModelTest(TestCase):
    def seTup(self):
        self.talk = Talk.objects.create(
                title='Título da Palestra',
                start='10:00',
                description='Descrição da Palestra.'
                )

    def test_ordering(self):
        self.assertListEqual(['start'], Talk._meta.ordering)

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


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
                title='Título do curso',
                start='09:00',
                description='Descrição do curso',
                slots=20)

    def test_create(self):
        self.assertTrue(Course.objects.exists())

    def test_speaker(self):
        """Course has many speakers and vice-versa"""
        self.course.speakers.create(
                name='Adriano Oliveira',
                slug='adriano-oliveira',
                website='http://adrianooliveira.net'
                )
        self.assertEqual(1, self.course.speakers.count())

    def test_manager(self):
        self.assertIsInstance(Course.objects, PeriodManager)

    def test_ordering(self):
        self.assertListEqual(['start'], Course._meta.ordering)
