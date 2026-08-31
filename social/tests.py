from django.test import TestCase
from django.contrib.auth.models import User
from.models import Profile

class ProfileModelTest(TestCase):
    def test_profile_can_be_created(self):
        Profile.objects.create()