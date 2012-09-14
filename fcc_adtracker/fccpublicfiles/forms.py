from django import forms
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse_lazy
from django.forms.extras.widgets import SelectDateWidget
from doccloud.models import Document
from fccpublicfiles.models import PoliticalBuy, PoliticalSpot, Organization, Person, Role
from broadcasters.models import Broadcaster


class SelectWithPopUp(forms.Select):
    model = None

    def __init__(self, model=None, add_url=None):
        self.model = model
        self.add_url = add_url
        super(SelectWithPopUp, self).__init__()

    def render(self, name, *args, **kwargs):
        html = super(SelectWithPopUp, self).render(name, *args, **kwargs)

        if not self.model:
            self.model = name

        popupplus = render_to_string("_form_popuplink.html", {'field': name, 'model': self.model, 'add_url': self.add_url})
        return html + popupplus


class DocCloudFormBase(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file',)


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization


class SimpleOrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        exclude = ('addresses', 'employees', 'is_visible')
    organization_type = forms.CharField(widget=forms.HiddenInput)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ('is_visible',)


class AdvertiserSignatoryForm(forms.Form):
    """
    Custom form for advertiser_signatory popup form.
    Can't mixin two modelforms, so these fields aren't bound to models.
    """
    first_name = forms.CharField(max_length=40)
    middle_name = forms.CharField(max_length=40, required=False)
    last_name = forms.CharField(max_length=40)
    suffix = forms.CharField(max_length=10, required=False)
    job_title = forms.CharField(required=False, help_text="Job title or descriptor for position they hold.")
    advertiser_id = forms.IntegerField(required=False, widget=forms.HiddenInput)


class PoliticalSpotForm(forms.ModelForm):
    class Meta:
        model = PoliticalSpot


class PoliticalBuyFormBase(forms.ModelForm):
    class Meta:
        model = PoliticalBuy
        fields = ('broadcasters',)


class PrelimDocumentForm(DocCloudFormBase, PoliticalBuyFormBase):
    broadcasters = forms.ModelMultipleChoiceField(queryset=Broadcaster.objects.all())


class PoliticalBuyFormFull(forms.ModelForm):
    class Meta:
        model = PoliticalBuy
        fields = (
            'advertiser',
            'total_spent_raw',
            'num_spots_raw',
            'contract_start_date',
            'contract_end_date',
            'contract_number',
            'advertiser_signatory',
            'bought_by',
            'lowest_unit_price',
            'is_complete',
            'broadcasters',
        )

    contract_start_date = forms.DateField(widget=SelectDateWidget(attrs={'class':'input-mini'}))
    contract_end_date = forms.DateField(widget=SelectDateWidget(attrs={'class':'input-mini'}))
    advertiser = forms.ModelChoiceField(queryset=Organization.objects.filter(organization_type='AD'),
                                        widget=SelectWithPopUp(add_url=reverse_lazy('add_advertiser'))
                                        )
    bought_by = forms.ModelChoiceField(queryset=Organization.objects.filter(organization_type='MB'),
                                        widget=SelectWithPopUp(add_url=reverse_lazy('add_media_buyer')),
                                        required=False)
    advertiser_signatory = forms.ModelChoiceField(queryset=Person.objects.all(),
                                    widget=SelectWithPopUp(add_url=reverse_lazy('add_advertiser_signatory')),
                                    required=False)

    def __init__(self, *args, **kwargs):
        super(PoliticalBuyFormFull, self).__init__(*args, **kwargs)
        for fieldname in 'advertiser advertiser_signatory bought_by broadcasters'.split():
            append_ajax_class(self.fields[fieldname])


def append_ajax_class(field):
    if field.widget.attrs.has_key('class'):
        field.widget.attrs['class'] += ' suggestions'
    else:
        field.widget.attrs.update({'class':'suggestions'})
