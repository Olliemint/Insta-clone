from django.test import TestCase
from .models import Profile,User

# Create your tests here.

class ProfileTest(TestCase):
    '''
    Profile model
    '''
    def setUp(self):
        self.user = User.objects.create(username='Ollie')

    def tearDown(self):
        self.user.delete()

    def test_new_profile(self):
        self.assertIsInstance(self.user.profile, Profile)
        self.user.save()
        self.assertIsInstance(self.user.profile, Profile)
