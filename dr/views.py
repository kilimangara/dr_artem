from django.shortcuts import render, redirect
from django.template.context_processors import csrf
import threading
import bot.telegram_bot
FIRST_ANSWER = 'Я очень хочу купить подарок Артему'
SECOND_ANSWER = 'vitalya'
SECOND_TRIGGER_ANSWER = 'dog'
SECOND_TRIGGER_ANSWER_TRANSLATE1 = 'пес'
SECOND_TRIGGER_ANSWER_TRANSLATE2 = 'собака'

def get_session(request):
    if 'stage' in request.session:
        return request.session['stage']
    return 0

def root_view(request):
    return render(request, 'hello_view.html')


def numbers_view(request):
    if get_session(request) == 1:
        return redirect('/videos/')
    request.session['stage'] = 0
    args = {}
    args.update(csrf(request))
    if request.method == 'GET':
        return render(request, 'numbers_form.html', args)
    elif request.method == 'POST':
        if request.POST.get('answer', '') == FIRST_ANSWER:
            request.session['stage'] = 1
            return redirect('/videos/')
        return render(request, 'numbers_form.html', args)


def videos(request):
    args = {}
    args.update(csrf(request))
    if not get_session(request) == 1:
        return redirect('/numbers/')
    if request.method == 'GET':
        return render(request, 'last_page.html', args)
    elif request.method == 'POST':
        answer = request.POST.get('answer', '')
        if answer == SECOND_ANSWER:
            args.update({'url': 'https://www.youtube.com/watch?v=CZhvcXquN3w', 'desc': 'Вот и оно!'})
        elif answer == SECOND_TRIGGER_ANSWER_TRANSLATE1 or answer == SECOND_TRIGGER_ANSWER_TRANSLATE2 or answer == SECOND_TRIGGER_ANSWER:
            args.update({'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'desc': 'Не все так просто'})
        else:
            args.update({'desc': 'Неа', 'url':False})
            print(args)
        return render(request, 'last_page.html', args)






