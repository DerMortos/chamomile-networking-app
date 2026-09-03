from django.test import TestCase
from django.contrib.auth.models import User
from.models import Profile
from .models import Post
from django.core.files.uploadedfile import SimpleUploadedFile

class ProfileModelTest(TestCase):
    def test_profile_can_be_created(self):
        user = User.objects.create_user(username="testuser", password="testpass123")
        Profile.objects.create(user=user)

    def test_profile_links_to_user(self):
        user = User.objects.create_user(username="testuser2", password="testpass123")
        profile = Profile.objects.create(user=user)
        self.assertEqual(profile.user, user)

    def test_profile_has_bio_field(self):
        user = User.objects.create_user(username="testuser3", password="testpass123")
        profile = Profile.objects.create(user=user, bio="Hello world")
        self.assertEqual(profile.bio, "Hello world")

    def test_profile_has_image_field(self):
        user = User.objects.create_user(username="testuser4", password="testpass123")
        fake_image = SimpleUploadedFile("test.jpg", b"fake image content", content_type="image/jpeg")
        profile = Profile.objects.create(user=user, image=fake_image)
        self.assertTrue(profile.image.name.endswith(".jpg"))

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="postuser1", password="pass123")

    def test_post_has_content(self):
        post = Post.objects.create(author=self.user, content="Hello world")
        self.assertEqual(post.content, "Hello world")

    def test_post_has_timestamp(self):
        post = Post.objects.create(author=self.user, content="Test")
        self.assertIsNotNone(post.timestamp)
