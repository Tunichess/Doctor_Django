from django.contrib import admin
from first_app.models import Personne,Score,Etudiant,Medecin
# Register your models here.
class PersonneAdmin(admin.ModelAdmin):
    fields=['first_name','last_name','birthday','state']
    
    search_fields=['first_name','last_name','birthday','state']
    
    list_filter=['first_name','last_name','birthday','state']

    list_display=['first_name','last_name','birthday','state']
  
    list_editable=['birthday']

class ScoreAdmin(admin.ModelAdmin):
    fields=['first_name','last_name','score','resultat']
    
    search_fields=['first_name','last_name','score','resultat']
    
    list_filter=['first_name','last_name','score','resultat']

    list_display=['first_name','last_name','score','resultat']

#admin.site.register(AccessRecord)
#admin.site.register(Topic)
#admin.site.register(Webpage)
#admin.site.register(UserProfileInfo)
admin.site.register(Personne,PersonneAdmin)
admin.site.register(Etudiant)
admin.site.register(Medecin)
admin.site.register(Score,ScoreAdmin)


