from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("person/update/<str:id>", views.update_person, name="update_delete_person"),
    path("person", views.get_persons, name="get_persons"),

    path('student/list/', views.student_list, name='student_list'),  
    path('student/<int:pk>/', views.student_detail, name='student_detail'),  
    path('student/create/', views.student_create, name='student_create'),  
    path('student/<int:pk>/update/', views.student_update, name='student_update'),  
    path('student/<int:pk>/delete/', views.student_delete, name='student_delete'),


    path('home/<int:id>/', views.MyView.as_view(), name="home"),
    path('home/template/<int:id>', views.DynamicTemplateView.as_view(name="K", extra_context={"course":"Python"}), name="dynamic"),


    path("home/redirect/<int:id>", views.MyRedirectView.as_view(), name="redirect"),

    path("user/register", views.user_registration, name="register user"),

    path("user/create", views.sign_up, name="register"),
    path("user/login", views.user_login, name='login')




] 



