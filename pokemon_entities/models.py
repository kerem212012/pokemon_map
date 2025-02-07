from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(verbose_name="имя",max_length=200)
    image = models.ImageField(verbose_name="картинка")
    description = models.TextField(verbose_name="описание",blank=True)
    title_en = models.CharField(verbose_name="имя на английском",max_length=200,blank=True)
    title_jp = models.CharField(verbose_name="имя по японски",max_length=200,blank=True)
    previous_evolution = models.ForeignKey("self",verbose_name="прошлая и следующая эволюция", on_delete=models.CASCADE,null=True,blank=True,related_name="next_evolution")
    def __str__(self):
        return f"{self.title}"

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon,verbose_name="покемон", on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name="широта")
    lon = models.FloatField(verbose_name="долгота")
    appeared_at = models.DateTimeField(verbose_name="появится в")
    disappeared_at = models.DateTimeField(verbose_name="исчезнет в")
    level = models.IntegerField(verbose_name="уровень",blank=True,null=True)
    health = models.IntegerField(verbose_name="здоровые",blank=True,null=True)
    strength = models.IntegerField(verbose_name="сила",blank=True,null=True)
    defence = models.IntegerField(verbose_name="защита",blank=True,null=True)
    stamina = models.IntegerField(verbose_name="выносливость",blank=True,null=True)

    def __str__(self):
        return f"{self.lat} , {self.lon}"