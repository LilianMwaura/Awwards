from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project,Profile, Review
# Create your tests here.
class ProfileTestCases(TestCase):
    def setUp(self):
        self.new_profile = Profile(id=1, profile_picture='example.jpg', bio='Live life',
                                   email='wambui@gmail.com', phone_number='071824000',username='wambui')

    def tearDown(self):
        Profile.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

class ProjectTestCases(TestCase):
    def setUp(self):
        self.new_project = Project(id=1,title='Instagram', image='exampl.jpg',description='Description',link='www.instagram.com',country='Kenya')
        
    def tearDown(self):
        Project.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))

class ReviewTestCases(TestCase):
    def setUp(self):      
        self.new_review = Review(id=1,design='1',usability='1',content='1',overall='1',comment='comment')
             
    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))