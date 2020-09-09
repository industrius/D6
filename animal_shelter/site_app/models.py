from django.db import models

KIND = [
    ("Собака", "Собака"),
    ("Кошка", "Кошка"),
    ("Птица", "Птица")
]

class Pet(models.Model):
    kind_of = models.CharField("Вид", max_length=10, choices=KIND)
    nickname = models.CharField("Кличка", max_length=50)
    breed = models.CharField("Порода", max_length=50)
    age = models.PositiveSmallIntegerField("Возраст", default=1)
    description = models.TextField("Описание")
    receipt_date = models.DateField("Дата поступления", auto_now=True)
    foto = models.ImageField("Фото", upload_to="")
    comment = models.ManyToManyField("site_app.Comment", blank=True, verbose_name="Комментарий")

    class Meta:
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"

    def __str__(self):
        return self.nickname

    def age_str(self):
        word = "лет"
        n = self.age
        if n > 99:
            n = n % 100
        if n in range(5, 21):
            word = "лет"
        elif n % 10 == 1:
            word = "год"
        elif n % 10 in range(2, 5):
            word = "года"
        return "{} {}".format(self.age, word)


class Recall(models.Model):
    name = models.CharField("Имя", max_length=50)
    review = models.TextField("Отзыв")
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.name

class Comment(models.Model):
    note = models.CharField("Комментарий", max_length=50)

    class Meta:
        verbose_name = "Комменатрий"
        verbose_name_plural = "Комменатрии"

    def __str__(self):
        return self.note