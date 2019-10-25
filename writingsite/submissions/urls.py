from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('view/<int:submission_id>', views.view, name='view'),
]
