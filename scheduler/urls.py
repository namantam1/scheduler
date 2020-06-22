from django.urls import include, path
from django.contrib import admin
from scApi import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.schedule),
    path('ping', views.PingView.as_view()),
]