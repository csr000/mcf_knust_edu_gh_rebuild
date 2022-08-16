from django.shortcuts import render
from .models import Index, About, CohortBatch, Register, Staff, Event, News, Announcements, Publications, Contact, Socials


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


def event(request, context={}):
    context['data'] = Event.objects.all()
    return render(request, 'event.html', context)


def news(request, context={}):
    context['data'] = News.objects.all()
    return render(request, 'news.html', context)


def announcements(request, context={}):
    context['data'] = Announcements.objects.all()
    return render(request, 'announcements.html', context)


def publications(request, context={}):
    context['data'] = Publications.objects.all()
    return render(request, 'publications.html', context)


def contact(request, context={}):
    context['data'] = Contact.objects.get(pk=1)
    context['socials'] = Socials.objects.get(pk=1)
    return render(request, 'contact.html', context)


def cohort(request, id, context={}):
    context['data'] = CohortBatch.objects.all()
    match id:
        case '1':
            context['data'].filter(batch='2014/2015 Academic Year')
            return render(request, 'cohort_one.html', context)
        case '2':
            context['data'].filter(batch='2015/2016 Academic Year')
            return render(request, 'cohort_two.html', context)
        case '3':
            context['data'].filter(batch='2016/2017 Academic Year')
            return render(request, 'cohort_three.html', context)
        case '4':
            context['data'].filter(batch='2017/2018 Academic Year')
            return render(request, 'cohort_four.html', context)
        case '5':
            context['data'].filter(batch='2018/2019 Academic Year')
            return render(request, 'cohort_five.html', context)
