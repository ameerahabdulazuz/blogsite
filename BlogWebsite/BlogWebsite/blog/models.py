from django.db import models


class Post(models.Model):
    Title = models.CharField(max_length=255)
    Content = models.CharField(max_length=255)
    Category = models.CharField(max_length=255)
    Date_Published = models.DateField(null=True)


def __str__(self):
    return f"{self.Title} {self.Content} {self.Category}{self.Date_Published}"


class myUsers(models.Model):
    Username = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)


def __str__(self):
    return f"{self.Username} {self.Email} {self.Password}"


class Comment(models.Model):
    PostID = models.ForeignKey(Post,on_delete=models.CASCADE)
    UserID = models.ForeignKey(myUsers,on_delete=models.CASCADE)
    Content = models.CharField(max_length=255)
    DatePosted = models.DateField(null=True)

    def __str__(self):
        return f"{self.PostID} {self.UserID} {self.Content}{self.DatePosted}"


class category(models.Model):
    Name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.Name}"
