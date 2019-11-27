from django.test import TestCase
from webblog.models import Blog, Entry


class modelTest(TestCase):
    def testDemo(self):
        blog = Blog.objects.all().filter(name="Home")
        print(blog)

