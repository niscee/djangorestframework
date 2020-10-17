from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', username="normal" ,password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            return self.email
        
        except AttributeError:
            return "Fail"
        


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('normal@user.com', 'normal', 'foo')
        self.assertEqual(admin_user.email, 'normal@user.com')
        self.assertEqual(admin_user.username, 'normal')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        
        try:
            return "Pass"
        
        except AttributeError:
            return "Fail"
        