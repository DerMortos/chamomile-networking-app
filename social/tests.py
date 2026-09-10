from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from .models import Post
from .models import Comment
from .models import Message
from .models import Follow
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
        post = Post.objects.create(author=self.user, content="Test post")
        self.assertEqual(post.content, "Hello world")

    def test_post_has_timestamp(self):
        post = Post.objects.create(author=self.user, content="Test post 2")
        self.assertIsNotNone(post.timestamp)

    def test_post_links_to_author(self):
        post = Post.objects.create(author=self.user, content="Test post 3")
        self.assertEqual(post.author, self.user)

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="commentuser", password="pass123")
        self.post = Post.objects.create(author=self.user, content="Parent Post")

    def test_comment_has_content(self):
        comment = Comment.objects.create(post=self.post, author=self.user, content = "Test comment")
        self.assertEqual(comment.content, "Test comment")

    def test_comment_has_timestamp(self):
        comment = Comment.objects.create(post=self.post, author=self.user, content="Test comment 2")
        self.assertIsNotNone(comment.timestamp)

    def test_comment_links_to_author(self):
        comment=Comment.objects.create(post=self.post, author=self.user, content="Test comment 3")
        self.assertEqual(comment.author, self.user)

    def test_comment_links_to_post(self):
        comment=Comment.objects.create(post=self.post, author=self.user, content="Test comment 4")
        self.assertEqual(comment.post, self.post)

class MessageModelTest(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username="sender", password="pass123")
        self.recipient = User.objects.create_user(username="recipient", password="pass123")

    def test_message_has_content(self):
        msg = Message.objects.create(author=self.sender, recipient=self.recipient, content="Hi")
        self.assertEqual(msg.content, "Hi")

    def test_message_has_timestamp(self):
        msg = Message.objects.create(author=self.sender, recipient=self.recipient, content="Hey")
        self.assertIsNotNone(msg.timestamp)
    def test_message_defaults_to_public(self):
        msg = Message.objects.create(author=self.sender, recipient=self.recipient, content="Hello, again")
        self.assertFalse(msg.is_private)
    def test_message_can_be_set_to_private(self):
        msg = Message.objects.create(author=self.sender, recipient=self.recipient, content="'sup", is_private=True)
        self.assertTrue(msg.is_private)
    def test_message_links_author_and_recipient(self):
        msg = Message.objects.create(author=self.sender, recipient=self.recipient, content="yo")
        self.assertEqual(msg.author, self.sender)
        self.assertEqual(msg.recipient, self.recipient)
    def test_message_to_own_wall(self):
        msg = Message.objects.create(author=self.sender, recipient=self.sender, content="Hello, its me")
        self.assertEqual(msg.author, msg.recipient)

class FollowModelTest(TestCase):
    def setUp(self):
        self.follower = User.objects.create_user(username="follower", password="pass123")
        self.followed = User.objects.create_user(username="followed", password="pass123")
    def test_follow_has_timestamp(self):
        follow = Follow.objects.create(follower=self.follower, following=self.followed)
        self.assertIsNotNone(follow.timestamp)