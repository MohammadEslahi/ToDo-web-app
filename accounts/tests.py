from django.test import TestCase
from .models import CustomUser
from django.contrib.auth import authenticate


class CustomUser_test(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(username='test_CustomUser', age=22, email='test@test.test', password='test_password', is_active=True)
    
    def test_CustomUser_created(self):
        test_user_exists = CustomUser.objects.filter(username='test_CustomUser').exists()
        self.assertTrue(test_user_exists)
    
    def test_age_is_correct(self):
        test_user = CustomUser.objects.get(username='test_CustomUser')
        self.assertEqual(test_user.age, 22)

    def test_email_is_correct(self):
        test_user = CustomUser.objects.get(username='test_CustomUser')
        self.assertEqual(test_user.email, 'test@test.test')
    
    def test_CustomUser_is_active(self):
        test_user = CustomUser.objects.get(username='test_CustomUser')
        self.assertEqual(test_user.is_active, True)

    def test_user_can_sign_in(self):
        test_user = authenticate(username='test_CustomUser', password='test_password')
        self.assertIsNotNone(test_user)
    
    def test_invalid_username_signin(self):
        test_user = authenticate(username='invalid_CustomUser', password='test_password')
        self.assertIsNone(test_user)

    def test_invalid_password_signin(self):
        test_user = authenticate(username='test_CustomUser', password='invalid_password')
        self.assertIsNone(test_user)

    def test_edit_username(self):
        test_user = CustomUser.objects.get(username='test_CustomUser')
        test_user.username = 'edited_test_CustomUser'
        test_user.save()
        self.assertEqual(test_user.username, 'edited_test_CustomUser')

    def test_edit_password(self):
        test_user = CustomUser.objects.get(username='test_CustomUser')
        test_user.password = 'edited_password'
        test_user.save()
        self.assertEqual(test_user.password, 'edited_password')

    def test_edit_age(self):
        test_user = CustomUser.objects.get(username='test_CustomUser')
        test_user.age = 66
        test_user.save()
        self.assertEqual(test_user.age, 66)