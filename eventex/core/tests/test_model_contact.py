from django.test import TestCase
from eventex.core.models import Speaker, Contact
from django.core.exceptions import ValidationError


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
                name='Adriano Oliveira',
                slug='adriano-oliveira',
                photo='http://hbn.link/ad-pic'
                )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker,
                                         kind=Contact.EMAIL,
                                         value='adriano.qwe32@gmail.com')
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker,
                                         kind=Contact.PHONE,
                                         value='85-999473839')
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker,
                          kind=Contact.EMAIL,
                          value='adriano.qwe32@gmail.com')
        self.assertEqual('adriano.qwe32@gmail.com', str(contact))


class ContactManageerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
                name='Adriano Oliveira',
                slug='adriano-oliveira',
                photo='http://hbn.link/ao-pic'
                )
        s.contact_set.create(kind=Contact.EMAIL,
                             value='adriano.qwe32@gmail.com')
        s.contact_set.create(kind=Contact.PHONE,
                             value='85-999473839')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['adriano.qwe32@gmail.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['85-999473839']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

