from django import forms
from TravelPlanner.models import Destination, PackingList, PackingItem, TravelPlan, Photo


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ('name', 'description', 'location', 'photo')


class PackingListForm(forms.ModelForm):
    class Meta:
        model = PackingList
        fields = ('name',)


class PackingItemForm(forms.ModelForm):
    class Meta:
        model = PackingItem
        fields = ('name', 'quantity',)


class TravelPlanForm(forms.ModelForm):
    class Meta:
        model = TravelPlan
        fields = ('destination', 'start_date', 'end_date', 'transport', 'cost')


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('name', 'image',)

#Plik forms.py definiuje klasy formularzy,
# które pozwalają na tworzenie formularzy w Django.
# W tym konkretnym pliku zdefiniowano cztery klasy formularzy:
# DestinationForm, PackingListForm, PackingItemForm oraz TravelPlanForm.
# Każdy z tych formularzy odpowiada za tworzenie formularza dla odpowiadającego mu modelu zdefiniowanego w pliku models.py.
# Każdy formularz zawiera pola, które odpowiadają polom modelu oraz w razie potrzeby dodatkowe pola zdefiniowane przez nas.