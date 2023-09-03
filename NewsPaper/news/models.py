from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum



class Author(models.Model):
    AuthorUser=models.OneToOneField(User,on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default = 0)

    def update_rating(self):
        posRat=self.post_set.aggregate(postRating=Sum("rating"))
        pRat = 0
        pRat = postRat.get("postRating")
        commentRat = self.author.user.comment_set.aggregate(commentRating = Sum("rating"))
        cRat += comment.get("commentRating")
        self.ratingAuthor = pRat*3+commentRat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length = 64,unique = True)


class Post(models.Model):
    Author = models.ForeignKey(Author,on_delete = models.CASCADE)
    NEWS = "NW"
    ARTICLE = "AR"
    CATEGORY_CHOICES = ((NEWS,"Новость"),(ARTICLE,"Статья"))
    category_type = models.CharField(max_length = 2,choice = CATEGORY_CHOICES,default = ARTICLE)
    dateCreation = models.DateTimeField(auto_now_add = True)
    postCategory = models.ManyToManyField(Category, through = "PostCategory")
    title = models.Charield(max_length = 128)
    text = models.TextField()
    rating = models.SmallIntegerField(default = 0)

    def like(self):
        self.rating +=1
        self.save()
    def dislike(self):
        self.rating -=1
        self.save()
    def preview(self):
        return self.text[0:123] + "..."


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post,on_delete = models.CASCADE)
    CategoryThrough = models.ForeignKey(Category,on_delete = models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post,on_delete = models.CASADE)
    commentUser = models.ForeignKey(User,on_delete = models.CASADE)
    datecreation = models.DateTimeField(auto_now_add = True)
    rating = models.SmallIntegerField(default = 0)




# Create your models here.
