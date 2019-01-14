from django.contrib import admin
from login import models as lm

admin.site.register(lm.RegisteredUser)
admin.site.register(lm.Activation)
admin.site.register(lm.ProfilePhoto)
admin.site.register(lm.Follow)
