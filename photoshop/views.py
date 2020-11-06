from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request, 'index.html')

def photo(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['imageFile']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'photo.html')