from django import forms
from AlchemyCommon.models import Element

class ElementForm(forms.Form):
    name = forms.CharField(label = 'Название',max_length=50)
    first_recipe_el = forms.IntegerField()
    second_recipe_el = forms.IntegerField()
    discription = forms.CharField(max_length=140)

    def clean(self):
        cleaned_data = super(ElementForm,self).clean()
        name = cleaned_data.get('name')
        f_rec_el = cleaned_data.get('first_recipe_el')
        s_rec_el = cleaned_data.get('second_recipe_el')
        if f_rec_el > s_rec_el:
            cleaned_data['first_recipe_el'] = s_rec_el
            cleaned_data['second_recipe_el'] = f_rec_el
        if f_rec_el != 0 and s_rec_el != 0:
            try:
                Element.objects.get(pk = cleaned_data.get('first_recipe_el'))
                Element.objects.get(pk = cleaned_data.get('second_recipe_el'))
            except Element.DoesNotExist:
                raise forms.ValidationError("Ошибка: элемент из рецепта не существует!")
            
            try:
                Element.objects.get(first_recipe_el = cleaned_data.get('first_recipe_el'),second_recipe_el=cleaned_data.get('second_recipe_el'))
                raise forms.ValidationError("Ошибка: элемент с таким рецептом уже существует!")
            except Element.DoesNotExist:
                pass
            
        try:
            el=Element.objects.get(name = cleaned_data.get('name'))
            if el:
                raise forms.ValidationError("Ошибка: элемент с таким именем уже существует!")
        except Element.DoesNotExist:
            pass 

        return cleaned_data
