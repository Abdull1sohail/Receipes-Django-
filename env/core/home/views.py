from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "home.html")

def About(request):
    return render(request, "About.html")

def Contacts(request):
    return render(request, "Contacts.html")

def Surahs(request):
    # return render(request, "Surahs.html")
    Surahs = [
        {'surah_no': 'Sūra I' , 'name': 'Fātiḥa, or the Opening Chapter.'},
        {'surah_no': 'Sūra II' , 'name': 'Baqara, or the Heifer.'},
        {'surah_no': 'Sūra III' , 'name': 'Fātiḥa, or the Opening Chapter.'},
        {'surah_no': 'Sūra IV' , 'name': 'Nisāa, or The Women.'},
        {'surah_no': 'Sūra V' , 'name': 'Māïda, or The Table Spread.'},
        {'surah_no': 'Sūra VI' , 'name': 'Anām, or Cattle.'},
        {'surah_no': 'Sūra VII' , 'name': 'Arāf, or the Heights'},
        {'surah_no': 'Sūra VIII' , 'name': 'Anfāl, or the Spoils of War.'},
        {'surah_no': 'Sūra IX' , 'name': 'Tauba (Repentance) or Barāat (Immunity).'},
        {'surah_no': 'Sūra X' , 'name': 'Yūnus, or Jonah.'},

    ]
  
    
    return render(request, "Surahs.html", context = {'Surahs': Surahs})