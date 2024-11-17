# document_uploader/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from doc_uploader import views

urlpatterns = [
    path('', views.Home),
    path('upload/', views.upload_document, name='upload_document'),
    path('documents/', views.document_list, name='document_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
