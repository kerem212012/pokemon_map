from pokemon_entities.models import Pokemon
from django.contrib import admin

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass