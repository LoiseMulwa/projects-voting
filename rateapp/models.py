from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
  bio = HTMLField()
  profile_pic = ImageField(manual_crop ='1080x1080')
  contact_info = models.CharField(max_length=144)

  @classmethod
  def get_by_id(cls, id):
    profile = Profile.objects.get(user = id)
    return profile


  @classmethod
  def filter_by_id(cls, id):
    profile = Profile.objects.filter(user = id).first()
    return 

class Project(models.Model):
  profile = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
  title = models.CharField(max_length=144)
  description = models.TextField()
  img = ImageField(manual_crop = '1920x1080')
  live_site = models.URLField(max_length=250)

  @classmethod
  def get_projects(cls):
    projects = cls.objects.all()
    return projects

  @classmethod
  def search_by_title(cls,search_term):
    projects = cls.objects.filter(title__icontains=search_term)
    return projects

  @classmethod
  def get_profile_projects(cls, profile):
    projects = Project.objects.filter(profile__pk = profile)
    return projects

class Review(models.Model):
  design = models.IntegerField(default=0)
  usability = models.IntegerField(default=0)
  content = models.IntegerField(default=0)
  average = models.IntegerField(default=0)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.project