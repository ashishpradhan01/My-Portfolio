from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    context={}
    return render(request, 'main/index.html', context)

def projects(request):
    projects=[
        {
            'icon':'android',
            'title':'FavDish – Android Application',
            'description':"FavDish is an Online Recipe Android App, where user can save or upload own recipes. FavDish built using kotlin, jetpack and also uses the food APIs to fetch recipes. Room Database used to store user recipes.",
            'link':None
        },
        {
            'icon':'language',
            'title':'Customer relationship management – Django Web Application',
            'description':"Customer relationship management is an Online Django application, which aims to store customer information, identify sales. CRM tool built using Python, Django, Html and CSS.",
            'link': "https://github.com/ashishpradhan01/Django-CRM-WebApp"
        },
        {
            'icon':'face',
            'title':'Face Detection System – Python Application',
            'description':"Face Detection System is an offline face detection with haar cascade, fetching details. Face detection is built using opencv module. GUI built with tkinter-gui and php mysql database used to store person information.",
            'link':"https://github.com/ashishpradhan01/Face-Detection-System"
        }
    ]
    context={
        'projects' : projects
    }
    return render(request, 'main/projects.html', context)

def languages(request):
    languages = [
        {
            'title' : 'Python',
            'icon' : "assets\icons\python-icon.png",
            'alt' : "Python-Icon",
            'description': "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics."
        },
        {
            'title' : 'Kotlin',
            'icon' : "assets\icons\kotlin-icon.png",
            'alt' : "Kotlin-Icon",
            'description': "Kotlin is a cross-platform, statically typed, general-purpose programming language with type inference."
        },
        {
            'title' : 'Java',
            'icon' : "assets\icons\java-icon.png",
            'alt' : "Java-Icon",
            'description': "Java is a class-based, object-oriented programming language, Java applications are typically compiled to bytecode that can run on any (JVM) regardless of the underlying computer architecture."
        },
        {
            'title' : 'Technical skills',
            'icon' : "assets\icons\skills.png",
            'alt' : "Technical skills-Icon",
            'description': "Data Structures, Android App Development, Django Framework, Rest APIs, Git."
        }
    ]
    context={
        'languages' : languages
    }
    return render(request, 'main/languages.html', context)