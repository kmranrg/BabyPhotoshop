from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request, 'index.html')

def photo(request):
    uploaded_file_name = ""
    if request.method == 'POST':
        uploaded_file = request.FILES['imageFile']
        print(type(uploaded_file))
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        uploaded_file_name = str(uploaded_file.name)
    return render(request, 'photo.html', {'uploaded_file_name': uploaded_file_name})