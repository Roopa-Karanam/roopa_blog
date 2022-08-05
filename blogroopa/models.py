# blog/models.py
from django.urls import reverse
from django.db import models
from django.conf import settings  # Imports Django's loaded settings

class Topic(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True  # No duplicates!
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


    class Meta:
        ordering = ['name']
    
    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse('topic-detail', kwargs=kwargs)

class Post(models.Model):
    """
    Represents a blogroopa post
    """
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [   
        (DRAFT, 'Draft'),
        
        (PUBLISHED, 'Published')
    ]
    title = models.CharField(max_length=255)
    content = models.TextField()
 
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each save
    
    author = models.ForeignKey(
       settings.AUTH_USER_MODEL,  # The Django auth user model
       on_delete=models.PROTECT,  # Prevent posts from being deleted
       related_name='blogroopa_posts',  # "This" on the user model
       null=True
   )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        null=True,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible',
    )
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date & time this article was published',
    )
    slug = models.SlugField(
       null=False,
       help_text='The date & time this article was published',
       unique_for_date='published',  # Slug is unique for publication date
   )
    topics = models.ManyToManyField(
        Topic,
        related_name='blogroopa_posts'
    )
    
    
    
    def __str__(self):
        return self.title
    class Meta:
        # Sort by the `created` field. The `-` prefix
        # specifies to order in descending/reverse order.
        # Otherwise, it will be in ascending order.
        ordering = ['-created']
        
    def get_absolute_url(self):
        if self.published:
            kwargs = {
                'year': self.published.year,
                'month': self.published.month,
                'day': self.published.day,
                'slug': self.slug
            }
        else:
            kwargs = {'pk': self.pk}

        return reverse('post-detail', kwargs=kwargs)
    
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    submitted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted']

    def __str__(self):
        return f'{self.submitted.date()}: {self.email}'  
class Contest(models.Model):
    name=models.CharField(max_length=50)
    email = models.EmailField()
    photo = models.ImageField(
        blank=True,
        null=True,
        help_text='submit image'
    )
    submitted = models.DateTimeField(auto_now_add=True)
    

    
    
    
        
        
class Comments(models.Model):
    """
    Represents a blogroopa post
    """

    name = models.CharField(max_length=255)
    text = models.TextField()
    approved=models.BooleanField()
    email=models.EmailField ()
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each save
    
    post = models.ForeignKey(
       Post,  # The Django auth user model
       on_delete=models.PROTECT,  # Prevent posts from being deleted
       related_name='comments',  # "This" on the user model
       null=False
   )
   
    def __str__(self):
        return self.name
    class Meta:
        # Sort by the `created` field. The `-` prefix
        # specifies to order in descending/reverse order.
        # Otherwise, it will be in ascending order.
        ordering = ['-created']
        
        