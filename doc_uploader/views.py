# uploader/views.py
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from django.conf import settings
from django.http import JsonResponse
import os
from django.http import FileResponse
import shutil

def Home(request):
    return render(request, 'home.html')

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'up_doc.html', {'form': form})

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'doc_list.html', {'documents': documents})


def upload_folder(request):
    if request.method == 'POST':
        for file_obj in request.FILES.getlist('files'):
            folder_path = os.path.join(settings.MEDIA_ROOT, os.path.dirname(file_obj.name))
            os.makedirs(folder_path, exist_ok=True)
            file_path = os.path.join(folder_path, os.path.basename(file_obj.name))
            with open(file_path, 'wb+') as destination:
                for chunk in file_obj.chunks():
                    destination.write(chunk)
        return render(request, 'up_doc.html', {'message': 'Folder uploaded successfully!'})
    return render(request, 'up_doc.html')




def list_folders(request):
    base_path = settings.MEDIA_ROOT
    folders = [f.name for f in os.scandir(base_path) if f.is_dir()]
    return render(request, 'doc_list.html', {'folders': folders})

def download_folder(request, folder_name):
    folder_path = os.path.join(settings.MEDIA_ROOT, folder_name)
    zip_path = os.path.join(settings.MEDIA_ROOT, f"{folder_name}.zip")
    
    # Create a zip archive
    shutil.make_archive(zip_path[:-4], 'zip', folder_path)
    
    # Serve the zip archive as a download
    response = FileResponse(open(zip_path, 'rb'), as_attachment=True, filename=f"{folder_name}.zip")
    return response