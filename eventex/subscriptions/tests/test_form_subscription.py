from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def test_form_has_fields(self):
        """Form must have four fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digt(self):
        """CPF must only accept digits"""
        form = self.make_validated_form(cpf='ABCD5856320')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have eleven digits"""
        form = self.make_validated_form(cpf='8521')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_must_to_be_captalized(self):
        """Name must to be captalized"""
        form = self.make_validated_form(name="ADRIANO oliveira")
        self.assertEqual('Adriano Oliveira', form.cleaned_data['name'])

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Adriano Oliveira da Rocha',
                     cpf='85215856320',
                     email='adriano.qwe32@gmail.com',
                     phone='85-999473839')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
