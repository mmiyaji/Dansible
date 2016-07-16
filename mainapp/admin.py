from django.contrib import admin

from .models import ServerAttribute
from .models import Server
from .models import OSTemplate
from .models import ConfigFile
from .models import ConfigData
from .models import ConfigCommand
from .models import Config
admin.site.register(ServerAttribute)
admin.site.register(Server)
admin.site.register(OSTemplate)
admin.site.register(ConfigFile)
admin.site.register(ConfigData)
admin.site.register(ConfigCommand)
admin.site.register(Config)
