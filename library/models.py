from django.db import models
import uuid
from book.models import Book
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.

class Library(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    @property
    def name_address(self):
        return f"{self.name} | {self.address}"

class Rack(models.Model):
    number = models.IntegerField(unique=True)
    uuid = models.UUIDField(default=uuid.uuid4())
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.library} | {self.number}"

    @property
    def name_uuid(self) -> dict:
        return{
            "number": self.number,
            "uuid": self.uuid
        }

class BookItem(models.Model):
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} | {self.book.title} | {self.book.owner.email}"

@receiver(post_save, sender=BookItem)
def update_status_rack(sender, instance, created, **kwargs):
    if created:
        book_item = instance
        book_id = book_item.rack.id
        rack = Rack.objects.get(pk=book_id)
        rack.status = False
        rack.save()

@receiver(post_delete, sender=BookItem)
def update_status_rack(sender, instance, **kwargs):
        book_item = instance
        book_id = book_item.rack.id
        rack = Rack.objects.get(pk=book_id)
        rack.status = True
        rack.save()