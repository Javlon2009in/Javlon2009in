from django.shortcuts import render

def main(request, name):
    return render(request, 'index.html', {'name':name})
