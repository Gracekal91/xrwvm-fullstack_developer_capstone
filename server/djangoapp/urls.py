# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
    path(route='register', view=views.register, name='register'),
    path(route='get_cars', view=views.get_cars, name ='getcars'),
    # path(route='get_dealers/', view=views.get_dealerships, name='get_dealers'),
    # path for login
    
    path(route='login', view=views.login_user, name='login'),
    path(route='logout', view=views.logout_request, name='logout'),
    path(route='dealers', view=views.get_dealers, name='dealers'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
