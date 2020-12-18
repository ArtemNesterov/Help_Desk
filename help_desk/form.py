from django import forms

from help_desk import models


class NewClaimForm(forms.ModelForm):
    class Meta:
        model = models.ClaimModel
        fields = ('claim_topic', 'text', 'image', 'priority')


class EditClaimForm(forms.ModelForm):
    class Meta:
        model = models.ClaimModel
        fields = ('text', 'image', 'priority')


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.CommentModel
        fields = ('text',)
