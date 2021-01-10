from django.urls import path
from first_app import views

app_name='first_app'

urlpatterns=[
    path('login', views.user_login,name='login'),
    path('register', views.register, name='register'),
    path('user', views.Profile, name='user'),
    path('user2', views.Profile2, name='user2'),

    path('start', views.Start, name='start'),

    path('creequest', views.Creequest, name='creequest'),
    path('questiondoc', views.Questiondoc, name='questiondoc'),
    path('table', views.IndexView.as_view(), name='table'),
    path('dashboard', views.Dashboard, name='dashboard'),


    path('personnes1',views.PersonneListView1.as_view(),name='personne_list1'),
    path('personnes2',views.PersonneListView1.as_view(),name='personne_list2'),
    path('<int:pk>',views.PersonneDetailView.as_view(), name='detail'),
    path('create', views.PersonneCreateView.as_view(), name='create'),
    path('create/<int:pk>', views.PersonneUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.PersonneDeleteView.as_view(), name='delete'),
    path('question', views.Questions,name='question'),
   #path('accueil', views.accueil, name='accueil'),
    path('score', views.Scores,name='score'),
    path('scores', views.ScoreListView.as_view(),name='score_list'),
]