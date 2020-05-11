from django.shortcuts import render, redirect


def map_choice(request):
    return render(request, 'Map_chose.html')


def map_open(request):
    a = request.POST.getlist('checks')
    if a:
        if a == ['1']:
            return render(request, 'MAP1.html')
        elif a == ['2']:
            return render(request, 'MAP2.html')
        elif a == ['3']:
            return render(request, 'MAP3.html')
        if a == ['4']:
            return render(request, 'MAP4.html')
        elif a == ['1', '2']:
            return render(request, 'MAP5.html')
        elif a == ['1', '3']:
            return render(request, 'MAP6.html')
        if a == ['1', '4']:
            return render(request, 'MAP7.html')
        elif a == ['2', '3']:
            return render(request, 'MAP8.html')
        elif a == ['2', '4']:
            return render(request, 'MAP9.html')
        if a == ['3', '4']:
            return render(request, 'MAP10.html')
        elif a == ['1', '2', '3']:
            return render(request, 'MAP11.html')
        elif a == ['1', '2', '4']:
            return render(request, 'MAP12.html')
        if a == ['1', '3', '4']:
            return render(request, 'MAP13.html')
        elif a == ['2', '3', '4']:
            return render(request, 'MAP14.html')
        elif a == ['1', '2', '3', '4']:
            return render(request, 'MAP15.html')
    else:
        return redirect('/map/')


def main(request):
    return redirect('/')
