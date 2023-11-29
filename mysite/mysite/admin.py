from django.contrib import admin
from .models import SignupModel, NoValueModel, ValueModel
from .models import Profile, User
admin.site.register(NoValueModel)
admin.site.register(ValueModel)
admin.site.register(SignupModel)
#admin.site.register(WordleEntry)
admin.site.register(Profile)
