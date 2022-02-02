from django.db import models
# Create your models here.


class Post(models.Model):
    CATEGORY_CHOICES = (
        ('Technology', 'Technology'),
        ('News', 'News'),
        ('Sports', 'Sports'),
        ('Games', 'Games'),
        ('Movies', 'Movies'),
        ('Health', 'Health')
    )
    cover = models.URLField(null=True)
    cover2 = models.URLField(null=True)
    title = models.CharField(max_length=2000)
    slug = models.SlugField(default='')
    author = models.CharField(max_length=2000, default='')
    text = models.TextField(default='')
    text2 = models.TextField(default='')
    quote = models.CharField(max_length=2000, default='')
    quote_name = models.CharField(max_length=2000, default='')
    l_heading = models.CharField(max_length=2000, default='')
    l_heading_text = models.CharField(max_length=2000, default='')
    s_heading = models.CharField(max_length=2000, default='')
    s_heading_text = models.CharField(max_length=2000, default='')

    category = models.CharField(max_length=2000, choices=CATEGORY_CHOICES)
    created_date = models.DateTimeField()
    tag_1 = models.CharField(max_length=2000, default='')
    tag_2 = models.CharField(max_length=2000, default='')
    tag_3 = models.CharField(max_length=2000, default='')

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title
