from django.contrib import admin

# Register your models here.
from .models import Person,Cnic,Projects,Customer,Product,Author,Authorship,Book,Vehicle,Car,Student,Movie,Genre
admin.site.register(Person)
admin.site.register(Cnic)
admin.site.register(Projects)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Author)
admin.site.register(Authorship)
admin.site.register(Book)
admin.site.register(Vehicle)
admin.site.register(Car)
admin.site.register(Student)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "rating", "display_genre", "best_movie")
    list_filter = ("name", "rating")
    # fields = ["name", ("rating", "genre")]
    list_display_links = ["name", "rating"]

    fieldsets = (
        ("Add Movie", {
            'fields':('name', 'rating')
        }),
        ("Select Genre", {
            'fields':('genre',)
        })
    )

    
from django import forms

class GenreAdminForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"

    def clean_name(self):
        if self.cleaned_data["name"] == "Spike":
            raise forms.ValidationError("No Vampires")

        return self.cleaned_data["name"]
    
    

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    form = GenreAdminForm
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        
        form.base_fields["name"].label = "First Name (Humans only!):"
        return form
    list_display = ("name", "description")