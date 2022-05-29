from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home_page'),
    path('phones',views.phones,name = 'phone_page'),
    path('tablet',views.tablet,name = 'ablet_page'),
    path('television',views.television,name = 'television_page'),
    path('computer',views.computer,name = 'computerpage'),
    path('gaming',views.gaming,name = 'gaming_page'),
    path('about',views.about,name = 'about_page'),
    path('contact',views.contact,name = 'contact_page')

]
#path('home',views.home,name = 'home') ,
#path('details',views.item_details,name='itdtl')