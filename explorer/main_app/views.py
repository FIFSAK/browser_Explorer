from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import file_names  # Assume your model is FileName


def main_page(request):
    return render(request, 'index.html')


def files_page(request):
    files = file_names.objects.all()
    return render(request, 'all_files.html', {'files': files})


def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        # Check if the uploaded file is an image
        if file.content_type not in ['image/jpeg', 'image/png', 'image/gif']:
            return HttpResponse('File type not supported. Please upload an image.')
        uploaded_file = file_names(name=file.name, image=file.image)
        uploaded_file.save()

        return redirect('main_page')
