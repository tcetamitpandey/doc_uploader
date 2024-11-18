# document_uploader/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from doc_uploader import views

urlpatterns = [
    path('', views.Home,name='home'),
    # path('upload/', views.upload_document, name='upload_document'),
    path('upload/', views.upload_folder, name='upload_document'),
    path('documents/', views.document_list, name='document_list'),
    path('folders/', views.list_folders, name='list_folders'),
    path('folders/<str:folder_name>/download/', views.download_folder, name='download_folder'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
