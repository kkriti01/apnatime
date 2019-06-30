from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.year_of_experience = data.get('year_of_experience')
        user.address = data.get('address')
        user.profile_picture = data.get('profile_picture')
        user.preferred_language = data.get('preferred_language')
        user.birth_date = data.get('birth_date')
        user.is_active = True
        user.save()

        return user
