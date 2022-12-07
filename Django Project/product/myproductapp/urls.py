from django.urls import path
from myproductapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("",views.home, name="home"),
    path("adminproductadd", views.adminhtml, name="adminproduct"),
    path('deletedata/<int:stid>',views.deletedata, name="deletedata"),
    path('updatedata/<int:stid>',views.updatedata, name="updatedata"),
    path('adminadd', views.adminadddata, name="adminadddata"),
    path('signup', views.signup, name="signup"),
    path('searchproduct', views.searchproduct, name="searchproduct"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)