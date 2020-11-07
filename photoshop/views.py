from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from os import path, remove

# Create your views here.
def index(request):
    return render(request, 'index.html')

def photo(request):
    uploaded_file_name = ""
    if request.method == 'POST':
        uploaded_file = request.FILES['imageFile']
        uploaded_file_name = str(uploaded_file.name)

        # deleting the file if filename already exists
        if path.exists("media/"+uploaded_file_name):
            remove("media/"+uploaded_file_name)

        # saving the file
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'photo.html', {'uploaded_file_name': uploaded_file_name})