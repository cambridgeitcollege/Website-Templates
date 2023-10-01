from django.urls import path
from Index import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("",views.home,name="Index"),
]
