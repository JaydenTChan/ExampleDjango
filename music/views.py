from django.http import Http404
from django.shortcuts import render
from .models import Album

import json
from django.http import StreamingHttpResponse

def main_page(request):
    if request.method=='POST':
            received_json_data=json.loads(request.body)
            return StreamingHttpResponse('it was post request: '+str(received_json_data))
    return StreamingHttpResponse('it was GET request')

def index(request):
	all_albums = Album.objects.all()
	return render(request, 'music/index.html', {'all_albums': all_albums})
	
def detail(request, album_id):
	try:
		album = Album.objects.get(id=album_id)
	except Album.DoesNotExist:
		raise Http404("Album does not exist")
	return render(request, 'music/detail.html', {'album': album})