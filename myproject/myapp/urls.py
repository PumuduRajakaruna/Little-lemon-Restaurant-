from django.urls import path
from . import views 

app_name = 'myapp'

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.index, name = "index"),
    path('pizza/', views.pizza, name = 'pizza')
    # path('burger/', views.B, name = 'burger')

]
