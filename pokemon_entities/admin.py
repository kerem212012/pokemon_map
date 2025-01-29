from pokemon_entities.models import Pokemon,PokemonEntity
from django.contrib import admin

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass
@admin.register(PokemonEntity)
class PokemonEntityAdmin(admin.ModelAdmin):
    pass