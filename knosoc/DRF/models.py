from django.db import models

# Create your models here.

class Member(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharFiel(max_length=20)
	last_name = models.CharFiel(max_length=20)
	email = models.EmailField(max_lenght=75)
	#profile_picture = models.Imagefield() 

	def __str__(self)
		return self.user.username

class Book(models.Model):
	title = models.CharField(max_length=20)
	slug = models.SlugField()
	overview = models.TextField()date = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	thumbnail = models.ImageField()
	categories = models.ManyToManyField(Category)
	tag = models.ManyToManyField(Tag)

    """
    Other possibles features
    """
	#featured = models.BooleanField()
	# isbn = 
	# url =	


	def __str__(self):
		return self.title

    class Category(models.Model):
	title = models.CharField(max_length=20)
	#slug = models.SlugField()
	#thumbnail = models.ImageField()
		
	def __str__(self):
		return self.title