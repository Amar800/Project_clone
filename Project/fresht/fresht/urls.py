"""
URL configuration for fresht project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name="home"),
    path('review/<slug:n>', views.review_page.as_view() , name="review"),
    path('review_theatre/<slug:n>', views.review_page_theatre.as_view() , name="review_theatre"),
    path('review_hollywood/<slug:n>', views.review_page_hollywood.as_view() , name="review_hollywood"),
    path('review_surprises/<slug:n>', views.review_page_surprises.as_view() , name="review_surprises"),
    path('signup', views.signup , name="signup"),
    path('users/',include("django.contrib.auth.urls")),
    path('users/',include("users.urls")),
    path('user_review_page/<slug:n>/<slug:m>', views.user_review_page.as_view(), name="user_review_page")
]
