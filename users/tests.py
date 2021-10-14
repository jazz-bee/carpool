from django.test import TestCase
from django.contrib.auth import get_user_model


# USER SPECS
class UsersManagersTests(TestCase):
    # a new user, by default, is not verified and not a driver
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='normal@user.com', username='aUsername', password='foo')

        self.assertEqual(user.email, 'normal@user.com')
        self.assertEqual(user.username, 'aUsername')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_verified)
        self.assertFalse(user.is_driver)

    # a super user is always staff and superuser
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='super@user.com', username='superUser', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertFalse(admin_user.is_verified)
        self.assertFalse(admin_user.is_driver)

        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(
                email='super@edu.com.ar', username='aUsername', password='foo', is_superuser=False)
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(
                email='super@edu.com.ar', username='aUsername', password='foo', is_staff=False)

    # test email is mandatory
    def test_mandatory_fields(self):
        User = get_user_model()
        with self.assertRaisesMessage(ValueError, 'The Email must be set'):
            User.objects.create_user(
                email='', username='aUser', password='foo'
            )
        with self.assertRaisesMessage(ValueError, 'The Username must be set'):
            User.objects.create_user(
                email='as@email.com', username='', password="foo")
        with self.assertRaisesMessage(ValueError, 'User must have a password'):
            User.objects.create_user(email='a', username='x', password='')
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
