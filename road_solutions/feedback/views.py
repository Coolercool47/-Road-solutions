from django.shortcuts import render, redirect
from .models import Feedback
from django.utils import timezone


def report(request):
    return render(request, 'feedback_page.html')


def write_form(request):
    print(request.POST)
    if 'problem' in request.POST and 'problem_description' in request.POST \
            and 'place' in request.POST:
        if request.POST['problem'] != '' and request.POST['problem_description'] \
                and request.POST['place'] != '':
            prob_name = request.POST['problem']
            prob_description = request.POST['problem_description']
            place = request.POST['place']
            date = timezone.now()
            model = Feedback(problem_name=prob_name, problem_text=prob_description, address=place, date=date)
            model.save()
            return render(request, 'feedback_sent.html')
        else:
            return render(request, 'feedback_fail.html')
    else:
        return render(request, 'feedback_fail.html')


def main(request):
    return redirect('/')


def feedback(request):
    return redirect('/feedback')
