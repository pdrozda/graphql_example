from django.db import models


class BookCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=250)
    book_category = models.ForeignKey(BookCategory, related_name='books', on_delete=models.CASCADE, null=True, blank=True)
    publication_date = models.DateField()
    added_time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Client(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE,'Female'),)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)
    address = models.CharField(max_length=300)
    birthdate = models.DateField()
    added_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('last_name',)

    def __str__(self):
        return self.first_name+' '+self.last_name

class Order(models.Model):
    client = models.ForeignKey(Client, related_name='orders', on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Book, related_name='orders', on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    quantity = models.IntegerField()

