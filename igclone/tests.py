from django.test import TestCase
from .models import Feed,Comment
# Create your tests here.



class FeedTestClass(TestCase):
    def setUp(self):
        self.post_feed = Feed(image='default.png', caption='Dodge daemon', user=self.profile_test)
    def test_save(self):
        self.test_post.save_Post()
        self.assertEqual(len(Feed.objects.all()),1)   
            
    def tearDown(self):
        Feed.objects.all().delete()
        

    def test_insatance(self):
        self.assertTrue(isinstance(self.post_feed, Feed))


