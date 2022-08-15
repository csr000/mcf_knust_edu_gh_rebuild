from django.shortcuts import render
from .models import Index, About, Cohort, Register, Staff, Event, News, Announcements, Publications, Contact, Socials



def index(request, context={}):
    context['data'] = Index.objects.get(pk=1)
    return render(request, 'index.html', context)


def apply(request):
    return render(request, 'apply.html')


def about(request, context={}):
    context['data'] = About.objects.all()
    return render(request, 'about.html', context)


def register(request, context={}):
    context['data'] = Register.objects.get(pk=1)
    return render(request, 'register.html', context)


def staff(request, context={}):
    context['data'] = Staff.objects.all()
    return render(request, 'staff.html', context)


def event(request,context={}):
    context['data'] = Event.objects.all()
    return render(request, 'event.html', context)


def news(request):
    return render(request, 'news.html')


def announcements(request):
    return render(request, 'announcements.html')


def publications(request, context={}):
    context['data'] = Publications.objects.all()
    return render(request, 'publications.html', context)


def contact(request):
    return render(request, 'contact.html')


def cohort(request, id):
    match id:
        case '1':
            return render(request, 'cohort_one.html')
        case '2':
            return render(request, 'cohort_two.html')
        case '3':
            return render(request, 'cohort_three.html')
        case '4':
            return render(request, 'cohort_four.html')
        case '5':
            return render(request, 'cohort_five.html')
