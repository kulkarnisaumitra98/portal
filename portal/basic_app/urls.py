from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('questions/', views.add_question, name='questions'),
    path('questionhub/', views.question_hub, name='question_hub'),
    path('editquestion/<int:id>/', views.edit_question, name='edit_question'),
    path('leaderboard/', views.leader, name='leaderboard'),
    path('login/', views.elogin, name='login'),
    path('logout/',views.log_out, name='logout'),
]