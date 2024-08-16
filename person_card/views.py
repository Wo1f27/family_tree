from django.shortcuts import render, redirect

from .models import Person
from .forms import CombinedPersonCardForm


def person_card_list(request):
    cards = Person.objects.filter(deleted=False)

    context = {
        'cards': cards
    }

    return render(request, 'person_card/person_cards_list.html', context)


def person_card_create(request):
    if request.method == 'POST':
        form = CombinedPersonCardForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            # cd = form.cleaned_data
            form.save()
            return redirect('person_card:create_card')
        else:
            print(form.person_form.errors)
            print(form.email_form.errors)
            print(form.phone_number_form.errors)
    else:
        form = CombinedPersonCardForm()

    context = {
        'form': form
    }
    return render(request, 'person_card/create_card.html', context)

