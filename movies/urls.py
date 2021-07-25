
from django.urls import path
from .views import *
urlpatterns = [
    path('', MoviesList.as_view(),name='movies'),
    path('<int:pk>/',MoviesDetials.as_view(),name='movies_detials'),
    path('update/<int:pk>/',MoviesUpdate.as_view(),name='movies_update'),
    path('create/',MoviesCreate.as_view(),name='movies_create'),
    path('delete/<int:pk>/',MoviesDelete.as_view(),name='movies_delete'),
    path('all_access/<int:pk>/',MoviesAllOpreations.as_view(),name='movies_detials_all_access'),
]
