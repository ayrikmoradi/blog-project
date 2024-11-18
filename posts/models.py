from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    STATUSE_OF_ARTICLES = (
        ("checking", "checking"),
        ("rejected", "rejected"),
        ("published", "published"),
    )
     
    titel = models.CharField(max_length=300)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Articles")
    status = models.CharField(max_length=15, choices=STATUSE_OF_ARTICLES, default="checking")
    
    
    class Metaa:
        ordeing = ["-created"]
        
        
        def __str__(self) -> str:
            return f"{self.titel} writed by {self.author}"    
    