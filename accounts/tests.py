from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignUpTest(TestCase):
    username = 'ahmadreza'
    email = 'am@gmail.com'

    def test_signup_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        get_user_model().objects.create_user(
            self.username,
            self.email,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)

    def test_signup_form_invalid(self):
        response = self.client.post(reverse('signup'), {
            'username': 'ahmadreza', 'age': 25, 'password1': '123', 'password2': '456'})
        self.assertEqual(response.status_code, 200)

    def test_signup_form_valid(self):
        response = self.client.post(reverse('signup'), {
            'username': 'ahmadreza', 'age': 25, 'password1': '@ahmad1383', 'password2': '@ahmad1383'})
        self.assertEqual(response.status_code, 302)
