import folium
import json
from pokemon_entities.models import Pokemon,PokemonEntity
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime




MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)
def get_pokemon_image(request,pokemon):
    return request.build_absolute_uri(pokemon.image.url) if pokemon.image else DEFAULT_IMAGE_URL

def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    now = localtime().now()
    pokemons = Pokemon.objects.all()
    pokemon_img = []
    i = 0
    k = 0
    for pokemon in pokemons:
        pokemon_img.append(get_pokemon_image(request,pokemon))

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in PokemonEntity.objects.filter(appeared_at__lt = now,disappeared_at__gt = now):
        add_pokemon(
            folium_map, pokemon.lat,
            pokemon.lon,
            pokemon_img[k]
        )
        k += 1
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon_img[i],
            'title_ru': pokemon.title,
        })
        i += 1
    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    now = localtime().now()
    pokemon = get_object_or_404(Pokemon,id=pokemon_id)
    requested_pokemon = {
        "title_ru": pokemon.title,
        "img_url": request.build_absolute_uri(pokemon.image.url),
        "description": pokemon.description,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
    }




    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in PokemonEntity.objects.filter(pokemon=pokemon,appeared_at__lt = now,disappeared_at__gt = now):
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon.image.url)
        )
    if pokemon.previous_evolution:
        requested_pokemon["previous_evolution"] = {
            "title_ru": pokemon.previous_evolution.title,
            "pokemon_id": pokemon.previous_evolution.id,
            "img_url": request.build_absolute_uri(pokemon.previous_evolution.image.url)
        }

    if pokemon.next_evolution.all():
        requested_pokemon["next_evolution"] ={
            "title_ru": pokemon.next_evolution.all()[0].title,
            "pokemon_id": pokemon.next_evolution.all()[0].id,
            "img_url": request.build_absolute_uri(pokemon.next_evolution.all()[0].image.url)
        }
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': requested_pokemon
    })
