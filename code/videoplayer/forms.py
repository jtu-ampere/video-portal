from django import forms

class VideoUploadForm(forms.Form):
    video_file = forms.FileField(label='Upload Video')
    description = forms.CharField(widget=forms.Textarea, label='Video Description')
