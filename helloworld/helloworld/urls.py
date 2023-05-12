from helloworldapp.views import quiz_list, create_quiz, take_quiz, quiz_result
from helloworldapp.views import prompt_screen_name, view_metrics, logout
from django.contrib import admin
from django.urls import path
"""
URL configuration for helloworld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', quiz_list, name='quiz_list'),
    path('quizzes/', quiz_list, name='quiz_list'),
    path('quiz/create/', create_quiz, name='create_quiz'),
    path('quiz/<str:quiz_id>/', take_quiz, name='quiz'),
    path('quiz_result/<str:quiz_id>/', quiz_result, name='quiz_result'),
    path('prompt_screen_name/', prompt_screen_name, name='prompt_screen_name'),
    path('view_metrics/<str:quiz_id>/', view_metrics, name='view_metrics'),
    path('logout/', logout, name='logout'),
]
