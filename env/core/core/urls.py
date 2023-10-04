from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('Surahs/', Surahs, name="Surahs"),
    path('About/', About, name="About"),
    path('Contacts/', Contacts, name="Contacts"), 
    path('delete_receipe/<id>/' , delete_receipe , name = "delete_receipe"),
    path('update_receipe/<id>/' , update_receipe , name = "update_receipe"),
    path('login/', login_page, name="login"),
    path('register/', register, name="register"),
    path("logout/", logout_page, name="logout_page"),
    path("reports/", get_students, name="get_students"),
    path("Check-the-marks/<student_id>/", see_marks , name="see_marks"),
    path('receipes/', receipes, name="receipes"),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()