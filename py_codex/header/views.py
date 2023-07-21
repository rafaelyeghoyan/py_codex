from django.shortcuts import render
from .utils import create_map_with_marker


def home(request):
    menus = {
        "menu": [
            {"name": "Home", "href": "home"},
            {"name": "Project", "href": "project"},
            {"name": "Events", "href": "events"},
            {"name": "Courses", "href": "courses"},
            {"name": "About us", "href": "about"},
            {"name": "Contact", "href": "contact"},
        ],
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
    return render(request, "./home/index.html", {"menus": menus})


def contact(request):
    menus = {
        "menu": [
            {"name": "Home", "href": "home"},
            {"name": "Project", "href": "project"},
            {"name": "Events", "href": "events"},
            {"name": "Courses", "href": "courses"},
            {"name": "About us", "href": "about"},
            {"name": "Contact", "href": "contact"},
        ],
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

    my_latitude = 40.78668
    my_longitude = 43.83832
    my_marker_label = "PyCodeX office"
    map_html = create_map_with_marker(my_latitude, my_longitude, my_marker_label)

    # if request.method == 'POST':
    #     form = MyForm(request.POST)
    #     if form.is.valid():
    #         name = form.cleaned_data['name']
    #         email = form.cleaned_data['email']
    #     else:
    #         pass
    # else:
    #     form = MyForm()

    return render(
        request, "./contact/contact.html", {"menus": menus, "map_html": map_html}
    )
