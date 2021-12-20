from django.conf import settings
from . import views
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path("",views.simra,name="main"),
    path("bolly",views.bollywood,name="bolly"),
    path("holly",views.hollywood,name="holly"),
    path("tolly",views.tollywood,name="tolly"),
    path("webs",views.webseries,name="webs"),
    path("mpage/<int:id>",views.mdata, name="mpage"),
    path("mpage/<int:id>",views.ddata, name="mpage"),
    path("fo",views.frs,name="fo"),



]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
