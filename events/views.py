from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from .models import Event
from django.http import HttpResponse

def events(request):
    if request.method == 'POST':
        data = request.POST
        event_image = request.FILES.get('event_image')
        event_name = data.get('event_name')
        event_description = data.get('event_description')

        Event.objects.create(
            event_image=event_image,
            event_name=event_name,
            event_description=event_description,
        )
        return redirect('/')

    queryset = Event.objects.all()

    # if request.GET.get('search'):
    #     queryset = queryset.filter(
    #         recipe_name__icontains=request.GET.get('search'))

    context = {'events': queryset}
    return render(request, 'event/events.html', context)

def delete_event(request, id):
    queryset = Event.objects.get(id=id)
    queryset.delete()
    return redirect('/')

# def update_recipe(request, id):
#     queryset = Recipe.objects.get(id=id)

#     if request.method == 'POST':
#         data = request.POST
#         recipe_image = request.FILES.get('recipe_image')
#         recipe_name = data.get('recipe_name')
#         recipe_description = data.get('recipe_description')

#         queryset.recipe_name = recipe_name
#         queryset.recipe_description = recipe_description

#         if recipe_image:
#             queryset.recipe_image = recipe_image

#         queryset.save()
#         return redirect('/')
    
#     context = {'recipe': queryset}
#     return render(request, 'recipe/update_recipe.html', context)
