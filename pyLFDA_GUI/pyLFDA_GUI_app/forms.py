from django import forms
from django.forms import ModelForm
from .models import *

class new_workspace_form(ModelForm):
    class Meta:
        model = workspace
        fields = ('experiment_name', 'workspace_folder', 'pdb_filename', 'gro_filename', 'trr_filename', 'tpr_filename', 'ndx_filename', 'gfda_version')