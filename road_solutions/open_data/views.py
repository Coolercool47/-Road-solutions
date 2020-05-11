from django.shortcuts import render, redirect


def open_data(request):
    return render(request, "open_data.html")


def main(request):
    return redirect('/')
