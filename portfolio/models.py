from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    completion_date = models.DateField()
    description = models.TextField(blank=True)
    certificate_url = models.URLField(blank=True)
    
    def get_season_year(self):
        """Convert date to Season Year format"""
        month = self.completion_date.month
        year = self.completion_date.year
        
        if month in [12, 1, 2]:
            season = "Winter"
        elif month in [3, 4, 5]:
            season = "Spring"
        elif month in [6, 7, 8]:
            season = "Summer"
        else:  # month in [9, 10, 11]
            season = "Fall"
            
        return f"{season} {year}"

    def __str__(self):
        return self.name

class Experience(models.Model):
    EXPERIENCE_TYPES = [
        ('work', 'Work Experience'),
        ('volunteer', 'Volunteer'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance'),
        ('Conference/Summit', 'Conference/Summit'),
    ]
    
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    experience_type = models.CharField(max_length=20, choices=EXPERIENCE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    skills_used = models.CharField(max_length=500, help_text="Comma-separated skills")
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.title} at {self.company}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300, help_text="Comma-separated technologies")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    featured = models.BooleanField(default=False)
    created_date = models.DateField()
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title