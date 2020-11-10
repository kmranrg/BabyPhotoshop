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
        img.save("media/sharpness_kumar_anurag.jpg")
        return "jpg"
    elif imageFile[-3:] == "png":
        img.save("media/sharpness_kumar_anurag.png")
        return "png"
    elif imageFile[-4:] == "jpeg":
        img.save("media/sharpness_kumar_anurag.jpeg")
        return "jpeg"
    else:
        return "file not saved"

def saturate(saturationValue, imageFileName):
    imageFileName = str(imageFileName)
    saturationValue = int(saturationValue)
    img = Image.open(imageFileName)
    
    color = ImageEnhance.Color(img)
    img = color.enhance(saturationValue)

    if imageFileName[-3:] == "jpg":
        img.save("media/saturated_kumar_anurag.jpg")
        return "jpg"
    elif imageFileName[-3:] == "png":
        img.save("media/saturated_kumar_anurag.png")
        return "png"
    elif imageFileName[-4:] == "jpeg":
        img.save("media/saturated_kumar_anurag.jpeg")
        return "jpeg"
    else:
        return "file not saved"

def transpose(transposeValue, imageFileName):
    imageFileName = str(imageFileName)
    transposeValue = str(transposeValue)

    img = Image.open(imageFileName)

    if transposeValue == "FLIP_LEFT_RIGHT":
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif transposeValue == "FLIP_TOP_BOTTOM":
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
    elif transposeValue == "ROTATE_90":
        img = img.transpose(Image.ROTATE_90)
    elif transposeValue == "ROTATE_180":
        img = img.transpose(Image.ROTATE_180)
    elif transposeValue == "ROTATE_270":
        img = img.transpose(Image.ROTATE_270)
    else:
        return "file not saved"
    
    if imageFileName[-3:] == "jpg":
        img.save("media/transposed_kumar_anurag.jpg")
        return "jpg"
    elif imageFileName[-3:] == "png":
        img.save("media/transposed_kumar_anurag.png")
        return "png"
    elif imageFileName[-4:] == "jpeg":
        img.save("media/transposed_kumar_anurag.jpeg")
        return "jpeg"
    else:
        return "file not saved"

def brightness(brightnessValue, imageFileName):
    imageFileName = str(imageFileName)
    brightnessValue = int(brightnessValue)

    img = Image.open(imageFileName)

    brightness = ImageEnhance.Brightness(img)
    img = brightness.enhance(brightnessValue)

    if imageFileName[-3:] == "jpg":
        img.save("media/brightness_kumar_anurag.jpg")
        return "jpg"
    elif imageFileName[-3:] == "png":
        img.save("media/brightness_kumar_anurag.png")
        return "png"
    elif imageFileName[-4:] == "jpeg":
        img.save("media/brightness_kumar_anurag.jpeg")
        return "jpeg"
    else:
        return "file not saved"

def photo_brightness(request):
    usr_uploaded_file = ""
    usr_brightnessValue = 0
    if request.method == 'POST':

        uploaded_file = request.FILES['imageFileForBrightness']
        usr_uploaded_file = str(uploaded_file.name)

        brightnessValue = float(request.POST["brightnessValue"])
        usr_brightnessValue = brightnessValue

        # deleting the file if filename already exists
        if path.exists("media/"+usr_uploaded_file):
            remove("media/"+usr_uploaded_file)

        # saving the file
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

        # calling brightness function
        fileType = brightness(usr_brightnessValue , "media/"+usr_uploaded_file)

        if fileType == "file not saved":
            usr_uploaded_file = "File  not uploaded. Please upload jpg, png and jpeg file formats only"
        else:
            usr_uploaded_file = {"name":uploaded_file.name, "type":fileType}

    return render(request, 'photo_brightness.html', {'usr_uploaded_file': usr_uploaded_file})

def photo_transpose(request):

    usr_uploaded_file = ""
    usr_transposeValue = 0
    if request.method == 'POST':

        uploaded_file = request.FILES['imageFileForTranspose']
        usr_uploaded_file = str(uploaded_file.name)

        transposeValue = str(request.POST["transposeValue"])
        usr_transposeValue = transposeValue

        # deleting the file if filename already exists
        if path.exists("media/"+usr_uploaded_file):
            remove("media/"+usr_uploaded_file)

        # saving the file
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

        # calling sharpness function
        fileType = transpose(usr_transposeValue , "media/"+usr_uploaded_file)

        if fileType == "file not saved":
            usr_uploaded_file = "File  not uploaded. Please upload jpg, png and jpeg file formats only"
        else:
            usr_uploaded_file = {"name":uploaded_file.name, "type":fileType}

    return render(request, 'photo_transpose.html', {'usr_uploaded_file': usr_uploaded_file})

def photo_saturation(request):
    usr_uploaded_file = ""
    usr_saturationValue = 0
    if request.method == 'POST':
        uploaded_file = request.FILES['imageFileForSaturation']
        usr_uploaded_file = str(uploaded_file.name)

        saturationValue = float(request.POST["saturationValue"])
        usr_saturationValue = saturationValue

        # deleting the file if filename already exists
        if path.exists("media/"+usr_uploaded_file):
            remove("media/"+usr_uploaded_file)

        # saving the file
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

        # calling saturate function
        fileType = saturate(usr_saturationValue, "media/"+usr_uploaded_file)

        if fileType == "file not saved":
            usr_uploaded_file = "File  not uploaded. Please upload jpg, png and jpeg file formats only"
        else:
            usr_uploaded_file = {"name":uploaded_file.name, "type":fileType}

    return render(request, 'photo_saturation.html', {'usr_uploaded_file': usr_uploaded_file})

def photo_sharpness(request):
    usr_uploaded_file = ""
    usr_sharpnessValue = 0
    if request.method == 'POST':

        uploaded_file = request.FILES['imageFileForSharpness']
        usr_uploaded_file = str(uploaded_file.name)

        sharpnessValue = float(request.POST["sharpnessValue"])
        usr_sharpnessValue = sharpnessValue

        # deleting the file if filename already exists
        if path.exists("media/"+usr_uploaded_file):
            remove("media/"+usr_uploaded_file)

        # saving the file
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

        # calling sharpness function
        fileType = sharpness(usr_sharpnessValue , "media/"+usr_uploaded_file)

        if fileType == "file not saved":
            usr_uploaded_file = "File  not uploaded. Please upload jpg, png and jpeg file formats only"
        else:
            usr_uploaded_file = {"name":uploaded_file.name, "type":fileType}

    return render(request, 'photo_sharpness.html', {'usr_uploaded_file': usr_uploaded_file})