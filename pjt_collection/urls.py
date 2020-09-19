from django.urls import path
from pjts import views
urlpatterns = [
    path('<pjt_name>/', views.index, name='index'),
]
