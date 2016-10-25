from django import forms
from django.db.models import Q
from AlchemyCommon.models import Element


class ElementForm(forms.ModelForm):

    class Meta:
        model = Element
        fields = ['name',
                  'first_recipe_el',
                  'category',
                  'second_recipe_el',
                  'description']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'first_recipe_el': forms.HiddenInput(),
            'second_recipe_el': forms.HiddenInput(),
            'category': forms.Select(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'})
        }

    def clean(self):
        cleaned_data = super(ElementForm, self).clean()
        f_rec_el = cleaned_data.get('first_recipe_el')
        s_rec_el = cleaned_data.get('second_recipe_el')
        if f_rec_el is None or s_rec_el is None:
            raise forms.ValidationError("Не задан рецепт")
        if f_rec_el > s_rec_el:
            cleaned_data['first_recipe_el'] = s_rec_el
            cleaned_data['second_recipe_el'] = f_rec_el
            f_rec_el, s_rec_el = s_rec_el, f_rec_el

        if f_rec_el == 0 or s_rec_el == 0:
            if f_rec_el != s_rec_el:
                raise forms.ValidationError("Ошибка: Должно быть два элемента!")
        else:
            if (not Element.objects.filter(Q(pk=f_rec_el) | Q(pk=s_rec_el)).exists()):
                raise forms.ValidationError("Ошибка: Элемент из рецепта не существует!")

            isRecipeDuplicate = Element.objects.filter(first_recipe_el=f_rec_el, second_recipe_el=s_rec_el).exists()
            if isRecipeDuplicate:
                if self.instance:
                    if (self.instance.first_recipe_el != f_rec_el and self.instance.second_recipe_el != s_rec_el):
                        raise forms.ValidationError("Ошибка: Элемент с таким рецептом уже существует")
                else:
                    forms.ValidationError("Ошибка: Элемент с таким рецептом уже существует")
            if (self.instance):
                query = Element.objects.filter(Q(pk=f_rec_el) | Q(pk=s_rec_el)).filter(Q(first_recipe_el=self.instance.id) | Q(second_recipe_el=self.instance.id))
                if (query.exists()):
                    raise forms.ValidationError("Ошибка: Элемент будет невозможно создать")
                if (s_rec_el == self.instance.id and f_rec_el == self.instance.id):
                    raise forms.ValidationError("Ошибка: Элемент не может содержать ссылку на себя")

        return cleaned_data
