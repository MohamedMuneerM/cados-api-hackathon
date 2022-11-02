from django.db import models

class AbstractTimestampMixin(models.Model):
	last_updated = models.DateTimeField(auto_now=True, editable=False)
	created = models.DateTimeField(auto_now_add=True, editable=False)

	class Meta:
		ordering = ("-id",)
		abstract = True

class Company(AbstractTimestampMixin):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Advocate(AbstractTimestampMixin):
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    bio = models.TextField()
    twitter = models.URLField()
    companies = models.ManyToManyField(Company, related_name="advocates")
    follower_count = models.IntegerField()

    class Meta:
        verbose_name = "Advocate"
        verbose_name_plural = "Advocates"

    def __str__(self):
        return str(self.username)


