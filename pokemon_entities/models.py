from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.title}"

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,null=True)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(blank=True,null=True)
    disappeared_at = models.DateTimeField(blank=True,null=True)
    level = models.IntegerField(blank=True,null=True)
    health = models.IntegerField(blank=True,null=True)
    strength = models.IntegerField(blank=True,null=True)
    defence = models.IntegerField(blank=True,null=True)
    stamina = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f"{self.lat} , {self.lon}"