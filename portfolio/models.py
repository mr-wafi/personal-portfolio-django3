from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    urls = models.URLField(blank=True)
#this the place where we can define details for our databse table and after defining it here we have to pass it to admin.py
#and in admin.py we will just simple import this to admin and then pass it to databse

    def __str__(self):
        return self.title


#what this __str__ function is doing?? this function returning the names or title of the inserted data in database
#in database the names or title of the table are like project one project tow but when we use this function this will
# return there title se we can easly find the post by there names and can edit delete or whatever we want we can apply.
