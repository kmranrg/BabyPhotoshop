from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from os import path, remove
from PIL import ImageEnhance
from PIL import Image

# Create your views here.
def index(request):
    return render(request, 'index.html')


def sharpness(sharpness_value, imageFile):
    img = Image.open(imageFile)
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(sharpness_value)

    if imageFile[-3:] == "jpg":
        img.save("media/sharpness.jpg")
        return "jpg"
    elif imageFile[-3:] == "png":
        img.save("media/sharpness.png")
        return "png"
    elif imageFile[-4:] == "jpeg":
        img.save("media/sharpness.jpeg")
        return "jpeg"
    else:
        return "file not saved"


def photo(request):
    usr_uploaded_file = ""
    if request.method == 'POST':
        uploaded_file = request.FILES['imageFile']
        usr_uploaded_file = str(uploaded_file.name)

        # deleting the file if filename already exists
        if path.exists("media/"+usr_uploaded_file):
            remove("media/"+usr_uploaded_file)

        # saving the file
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

        # calling sharpness function
        fileType = sharpness(95 , "media/"+usr_uploaded_file)

        if fileType == "file not saved":
            usr_uploaded_file = "File  not uploaded. Please upload jpg, png and jpeg file formats only"
        else:
            usr_uploaded_file = {"name":uploaded_file.name, "type":fileType}

    return render(request, 'photo.html', {'usr_uploaded_file': usr_uploaded_file})