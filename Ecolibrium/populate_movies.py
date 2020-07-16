import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ecolibrium.settings')
import django
django.setup()
from firstapp.models import Movie, Genre

def populate():
    with open ("./Task_1_data(1).json") as f:
        data=json.load(f)
        # print(data ,type(data))
        for movie in data:
            name=movie.get("name")
            imdb_score=movie.get("imdb_score")
            director=movie.get("director")
            popularity=movie.get("99popularity")
            mov,status=Movie.objects.get_or_create(name=name,
                                 imdb_score=imdb_score,
                                 director=director,
                                 popularity=popularity)
            genres=movie.get("genre")
            for genre in genres:
                gen,status=Genre.objects.get_or_create(name=genre)
                mov.genre.add(gen)
                mov.save()
            print(mov)
if __name__ =="__main__":
    populate()









