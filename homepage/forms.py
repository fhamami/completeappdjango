from django import forms

STATUS_APP = (
    ('OnGoing' ,'On-Going'),
    ('Finish', 'Finish')
)

class StatusApp(forms.Form):
    status_app = forms.MultipleChoiceField(required=True, choices=STATUS_APP)