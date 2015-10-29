from django.shortcuts import render
from django.shortcuts import render_to_response

from django.http import HttpResponse

from .models import Picture, Ocassion

# Create your views here.
def index(request):

    # Only show the first 10 most recent photos
    pictures = Picture.objects.order_by('-uploadDate')[:10]
    ocassions = Ocassion.objects.all()

    #return render(request, 'photos/index.html')
    return render_to_response('photos/index.html', {'pictures': pictures, 'ocassions': ocassions})

def ocassion(request, ocassion_id):
    pictures = Picture.objects.filter(ocassion__id = ocassion_id)
    selected_ocassion = Ocassion.objects.get(pk=ocassion_id)

    ocassions = Ocassion.objects.all()

    return render_to_response('photos/index.html', {'pictures': pictures, 'ocassions': ocassions, 'ocassion_id': ocassion_id, 'selected_ocassion': selected_ocassion})
