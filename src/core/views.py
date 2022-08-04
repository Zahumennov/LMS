from django.shortcuts import render # noqa


def index(request):

    return render(
        request=request,
        template_name='index.html'
    )
