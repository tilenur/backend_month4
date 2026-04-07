from django.db import models
import uuid

# Create your models here.

# INSERT INTO posts_post () ==> Post.objects.create(header="dasda", description="tesdad", user=1, rate=1)

# SELECT * FROM posts_post; ==> posts = Post.objects.all()

# SELECT * FROM posts_post WHERE user = 1; ==> posts = Post.objects.filter(user=1)

# UPDATE posts_post SET user = 2 WHERE user = 1; ==> 
#post = posts[1]
#post.user = 2
#post.save()

# SELECT * FROM posts_post WHERE id =1; ==> post = Post.objects.get(id=1)


# SELECT * FROM posts_post WHERE header ILIKE '% AB %'; ==> posts = Post.objects.filter(header__icontains="ab", is_deleted = False)

class Post(models.Model):
  # deleted_at = models.DateTimeField(null=True)
  # is_deleted = models.BooleanField(default=False)
  header = models.CharField(max_length=255)
  description = models.TextField()
  rate = models.IntegerField(null=True, blank=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  image = models.ImageField()
  
  def __str__(self):
    return f"{self.header}"