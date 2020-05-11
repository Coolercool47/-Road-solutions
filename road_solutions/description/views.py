from django.shortcuts import render, redirect


def description(request):
    return render(request, "project_info.html")


def main(request):
    return redirect('/')
