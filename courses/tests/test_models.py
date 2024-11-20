from django.contrib.auth.models import User
from django.test import TestCase

from courses.models import Subject, Course, Module


class TestSubjectModel(TestCase):
    """Тест модели Subject"""
    def setUp(self):
        self.subject = Subject.objects.create(title='Test subject', slug='test-subject')

    def test_create_subject(self):
        self.assertIsInstance(self.subject, Subject)

    def test_str_representation(self):
        self.assertEquals(str(self.subject), 'Test subject')


class TestCourseModel(TestCase):
    """Тесты для модели Course """
    def setUp(self):
        user = User.objects.create_user(username='name', email='email@email.com', password='Pass2345')
        subject = Subject.objects.create(title='Test sub', slug='title-sub')
        self.course = Course.objects.create(owner=user, subject=subject,
                                            title='backend', slug='backend',
                                            overview='backend course')

    def test_create_course(self):
        self.assertIsNotNone(self.course, Course)

    def test_str_representation(self):
        self.assertEquals(str(self.course), 'backend')


class TestModuleModel(TestCase):
    """Тесты для модели Module"""
    def setUp(self):
        user = User.objects.create_user(username='name', email='email@email.com', password='Pass2345')
        subject = Subject.objects.create(title='Test sub', slug='title-sub')
        course = Course.objects.create(owner=user, subject=subject,
                                   title='backend', slug='backend',
                                   overview='backend course')
        self.module = Module.objects.create(course=course, title='IT', description='it')

    def test_create_module(self):
        self.assertIsInstance(self.module, Module)

    def test_str_representation(self):
        self.assertEquals(str(self.module), '0. IT')








