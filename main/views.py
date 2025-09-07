from django.shortcuts import render

def show_main(request):
    context = {
        'app_title': 'Footballed Co.',
        'name': 'Laudya Michelle Alexandra',
        'class': 'PBP A',
    }

    return render(request, 'main.html', context)