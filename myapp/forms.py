from django import forms

class UploadVideoForm(forms.Form):

    title = forms.CharField(
        label="video title", 
        max_length=100,
    )
    src = forms.CharField(
        label="youtube video id", 
        max_length=100,
    )
    thumbnail = forms.CharField(
        label="thumbnail", 
        max_length=100,
    )



    def validate_data(self, request):
        return True
