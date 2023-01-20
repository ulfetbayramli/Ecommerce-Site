from django.test import TestCase
from .models import Category, Author, Blog, Comment

class TestModels(TestCase):

    @classmethod
    def setUpClass(cls):
        
        cls.data1 = {
            "name": "Culture"
        }
        cls.category = Category.objects.create(**cls.data1)
        cls.data2 = {
            "author": "John Doe"
        }
        cls.author = Author.objects.create(**cls.data2)
        cls.data3 = {
            "title": "Blog1",
            "author": cls.author,
            "category": cls.category
        }
        cls.blog = Blog.objects.create(**cls.data3)
        cls.data4 = {
            "name": "Sarah Gadon",
            "email": "sarahgadon@gmail.com",
            "blog": cls.blog
        }
        cls.comment = Comment.objects.create(**cls.data4)

    def test_category(self):
        self.assertEqual(self.data1['name'], self.category.name)
    
    def test_author(self):
        self.assertEqual(self.data2['author'], self.author.author)

    def test_blog(self):
        with self.subTest():
            self.assertEqual(self.data3['title'], self.blog.title)
        with self.subTest():
            self.assertEqual(self.data3['author'], self.blog.author)
        with self.subTest():
            self.assertEqual(self.data3['category'], self.blog.category)


    def test_comment(self):
        with self.subTest():
            self.assertEqual(self.data4['name'], self.comment.name)
        with self.subTest():
            self.assertEqual(self.data4['email'], self.comment.email)
        with self.subTest():
            self.assertEqual(self.data4['blog'], self.comment.blog)

    @classmethod
    def tearDownClass(cls):
        del cls.category
        del cls.author
        del cls.blog
        del cls.comment
