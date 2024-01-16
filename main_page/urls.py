from . import views
from django.urls import path



urlpatterns = [
    path('',views.home,name='home'),
    path('service/<str:service_name>',views.service, name='service'),
    path('achievement/<str:achievement_name>',views.achievement, name='achievement'),
    path('article/<str:article_name>',views.article, name='article'),
    path('contact/',views.contact,name='contact'),
    path('service_detials/',views.service_detials,name='service_detials'),
    path('achievement_list/',views.achievement_list,name='achievement_list'),
    path('articles_list/',views.articles_list,name='articles_list'),
    path('about/',views.about,name='about'),
    path('lawyerinfo/',views.lawyer_info,name='lawyer'),
    path('lawyer/<str:lawyer_name>',views.lawyer_cv, name='lawyer'),
    path('videos/',views.videos,name='videos'),

    
]
