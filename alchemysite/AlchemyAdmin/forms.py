from django import forms
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
            'first_recipe_el': forms.HiddenInput(),
            'second_recipe_el': forms.HiddenInput()
        }

    def clean(self):
        cleaned_data = super(ElementForm, self).clean()
        name = cleaned_data.get('name')
        f_rec_el = cleaned_data.get('first_recipe_el')
        s_rec_el = cleaned_data.get('second_recipe_el')
        if f_rec_el > s_rec_el:
            cleaned_data['first_recipe_el'] = s_rec_el
            cleaned_data['second_recipe_el'] = f_rec_el
        if f_rec_el != 0 and s_rec_el != 0:
            try:
                Element.objects.get(pk=cleaned_data.get('first_recipe_el'))
                Element.objects.get(pk=cleaned_data.get('second_recipe_el'))
            except Element.DoesNotExist:
                raise forms.ValidationError("Ошибка: элемент из рецепта не существует!")

            if self.instance:
                if cleaned_data.get('first_recipe_el') == self.instance.id or cleaned_data.get('second_recipe_el') == self.instance.id:
                    raise forms.ValidationError("Ошибка: рецепт элемента не может содержать ссылку на себя!")

            try:
                Element.objects.get(first_recipe_el=cleaned_data.get('first_recipe_el'), second_recipe_el=cleaned_data.get('second_recipe_el'))
                if self.instance:
                    if self.instance.first_recipe_el != cleaned_data.get('first_recipe_el') or self.instance.second_recipe_el != cleaned_data.get('second_recipe_el'):
                        raise forms.ValidationError("Ошибка: элемент с таким рецептом уже существует!")
                else:
                    raise forms.ValidationError("Ошибка: элемент с таким рецептом уже существует!")
            except Element.DoesNotExist:
                pass

            try:
                Element.objects.get(name=cleaned_data.get('name'))
                if self.instance:
                    if self.instance.name != cleaned_data.get('name'):
                        raise forms.ValidationError("Ошибка: элемент с таким именем уже существует!")
                else:
                    raise forms.ValidationError("Ошибка: элемент с таким именем уже существует!")
            except Element.DoesNotExist:
                pass

        return cleaned_data
