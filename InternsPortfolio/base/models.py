from django.db import models

# Create your models here.
class Interns(models.Model):
    name = models.CharField(max_length=100)
    role  = models.CharField(max_length=100, default="Software Engineering Intern")
    bio = models.TextField()
    avatar_url =models.URLField(blank=True,help_text="Direct link to a premium profile image")
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    joined_date = models.DateField()


    def __str__(self):
        return self.name
    

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject  = models.CharField(max_length=70)
    message = models.TextField()
    created_at  =models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Message from {self.full_name} - {self.subject}"