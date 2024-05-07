from django.db import models


class Books_category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'books_category'

    def __str__(self) -> str:

        return f"{self.category_name}"


class Books(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    ISBN = models.CharField(max_length=255)
    price = models.FloatField(max_length=100)
    image = models.ImageField(upload_to='books/', blank=True, null=True)
    year = models.IntegerField()
    book_category = models.ForeignKey(Books_category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'books'

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    year = models.IntegerField()

    class Meta:
        db_table = 'author'

    def __str__(self) -> str:
        return f"{self.first_name}"

class Book_author(models.Model):
    author_book = models.ForeignKey(Author, on_delete=models.CASCADE)
    books_name = models.ForeignKey(Books, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_author'

    def __str__(self) -> str:
        return self.author_book



class Review(models.Model):
    comment = models.TextField()
    star_given = models.IntegerField()
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    class Meta:
        db_table ='review'

    def __str__(self) -> str:
        return self.comment

