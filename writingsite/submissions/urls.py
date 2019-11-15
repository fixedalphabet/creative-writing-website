from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='submissions/index'),
    path('view/<int:submission_id>', views.view, name='submissions/view'),
    path('<int:submission_id>/comment', views.comment, name='submissions/comment'),
]
