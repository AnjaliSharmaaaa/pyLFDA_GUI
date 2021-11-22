from django.shortcuts import render, redirect

from .forms import *
from .models import *

from .script import *

# Create your views here.
def home_page(request):
    return render(request, 'homepage.html')

def new_workspace(request):
    data = {'form': new_workspace_form()}
    if request.method == 'POST':
        form = new_workspace_form(request.POST)
        if form.is_valid():
            WorkSpace = workspace(experiment_name = form.cleaned_data['experiment_name'],
                                  workspace_folder = form.cleaned_data['workspace_folder'],
                                  pdb_filename = form.cleaned_data['pdb_filename'],
                                  gro_filename = form.cleaned_data['gro_filename'],
                                  trr_filename = form.cleaned_data['trr_filename'],
                                  tpr_filename = form.cleaned_data['tpr_filename'],
                                  ndx_filename = form.cleaned_data['ndx_filename'],
                                  gfda_version = form.cleaned_data['gfda_version'])
            WorkSpace.save()
            print('New workspace is created')
            return redirect('homepage')
        else:
            data = {'form': form}
    return render(request, 'new_workspace.html', data)

def all_workspace(request):
    data = {'all_workspace': workspace.objects.all()}
    return render(request, 'all_workspace.html', data)

def open_workspace(request, workspace_id):
    data = {'workspace': workspace.objects.get(id=workspace_id)}
    return render(request, 'workspace.html', data)

def run_experiment(request, workspace_id, work_id):
    work_by_id(workspace_id, work_id)
    return redirect(f'workspace/{workspace_id}')