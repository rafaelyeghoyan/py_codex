from django.shortcuts import render


def home(request):
    menuBar = {
        "menu": ["Home", "Project", "Events", "Courses", "About us", "Contact"],
        "footerMenu": {
            "menuOne": ["Home", "Project", "About us", "Contact"],
            "menuTwo": ["Robotics", "Web Desing", "Machine Learning"],
            "menuThree": [
                "Getting started",
                "Network status",
                "FAQ",
                "Referal program",
            ],
        },
    }

    return render(request, "./home/index.html", {"menus": menuBar})
