from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'person_card'

urlpatterns = [
    path('', views.person_card_list, name='person_cards'),
    path('create_card/', views.person_card_create, name='create_card'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)