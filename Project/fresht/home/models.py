from django.db import models

class movies(models.Model):
    GENRE=(("Action","Action"),("Adventure","Adventure"),("Horror","Horror"),("Rom-Com","Rom-Com"),("Romantic","Romantic"),("Slice of life","Slice of life"),("Drama","Drama"),("Thriller","Thriller"),("Sci-fi","Sci-fi"),("Crime","Crime"),("Comedy","Comedy"),("Fantasy","Fantasy"),("Animated","Animated"))
    name=models.CharField(max_length=50)
    synopsis=models.CharField(max_length=300)
    director=models.CharField(max_length=20)
    actors=models.CharField(max_length=200)
    genre=models.CharField(max_length=20,choices=GENRE)
    rating=models.CharField(max_length=4)
    trailer=models.CharField(max_length=250)
    img=models.CharField(max_length=150)
    slug=models.SlugField(default="", null=False)
    vno=models.IntegerField(default="1")

class movies_theatre(models.Model):
    GENRE=(("Action","Action"),("Adventure","Adventure"),("Horror","Horror"),("Rom-Com","Rom-Com"),("Romantic","Romantic"),("Slice of life","Slice of life"),("Drama","Drama"),("Thriller","Thriller"),("Sci-fi","Sci-fi"),("Crime","Crime"),("Comedy","Comedy"),("Fantasy","Fantasy"),("Animated","Animated"))
    name=models.CharField(max_length=50)
    synopsis=models.CharField(max_length=300)
    director=models.CharField(max_length=20)
    actors=models.CharField(max_length=200)
    genre=models.CharField(max_length=20,choices=GENRE)
    rating=models.CharField(max_length=4)
    trailer=models.CharField(max_length=250)
    img=models.CharField(max_length=150)
    slug=models.SlugField(default="", null=False)
    vno=models.IntegerField(default="2")

class movies_hollywood(models.Model):
    GENRE=(("Action","Action"),("Adventure","Adventure"),("Horror","Horror"),("Rom-Com","Rom-Com"),("Romantic","Romantic"),("Slice of life","Slice of life"),("Drama","Drama"),("Thriller","Thriller"),("Sci-fi","Sci-fi"),("Crime","Crime"),("Comedy","Comedy"),("Fantasy","Fantasy"),("Animated","Animated"))
    name=models.CharField(max_length=50)
    synopsis=models.CharField(max_length=300)
    director=models.CharField(max_length=20)
    actors=models.CharField(max_length=200)
    genre=models.CharField(max_length=20,choices=GENRE)
    rating=models.CharField(max_length=4)
    trailer=models.CharField(max_length=250)
    img=models.CharField(max_length=150)
    slug=models.SlugField(default="", null=False)
    vno=models.IntegerField(default="3")

class movies_surprises(models.Model):
    GENRE=(("Action","Action"),("Adventure","Adventure"),("Horror","Horror"),("Rom-Com","Rom-Com"),("Romantic","Romantic"),("Slice of life","Slice of life"),("Drama","Drama"),("Thriller","Thriller"),("Sci-fi","Sci-fi"),("Crime","Crime"),("Comedy","Comedy"),("Fantasy","Fantasy"),("Animated","Animated"))
    name=models.CharField(max_length=50)
    synopsis=models.CharField(max_length=300)
    director=models.CharField(max_length=20)
    actors=models.CharField(max_length=200)
    genre=models.CharField(max_length=20,choices=GENRE)
    rating=models.CharField(max_length=4)
    trailer=models.CharField(max_length=250)
    img=models.CharField(max_length=150)
    slug=models.SlugField(default="", null=False)
    vno=models.IntegerField(default="4")

class user_info(models.Model):
    username=models.CharField("Username",max_length=75)
    email_address=models.EmailField("Email Id")
    password=models.CharField("Password",max_length=50)
    notif=models.BooleanField("Notifications",default="False")

class user_review(models.Model):
    review=models.CharField(max_length=300)
    rating=models.IntegerField()
    slug=models.IntegerField(default="0")
    vno=models.IntegerField(default="0")
