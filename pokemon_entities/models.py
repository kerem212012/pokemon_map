from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.title}"

class PokemonEntity(models.Model):
    Pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    Lat = models.FloatField()
    Lon = models.FloatField()
    Appeared_at = models.DateTimeField()
    Disappeared_at = models.DateTimeField()
    Level = models.IntegerField()
    Health = models.IntegerField()
    Strength = models.IntegerField()
    Defence = models.IntegerField()
    Stamina = models.IntegerField()

    def __str__(self):
        return f"{self.Lat} , {self.Lon}"