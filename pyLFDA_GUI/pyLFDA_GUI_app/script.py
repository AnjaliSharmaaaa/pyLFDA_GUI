import pickle

from .pyLFDA import *
from .models import workspace

def get_object(id):
    return workspace.objects.get(id)

def work_by_id(workspace_id, work_id):
    work_space_obj = get_object(workspace_id)
    if work_id==1:
        experiment = LFDA(experiment_name= work_space_obj.experiment_name,
                          trr_filename = work_space_obj.trr_filename, 
                          tpr_filename = work_space_obj.tpr_filename, 
                          ndx_filename = work_space_obj.ndx_filename, 
                          pdb_filename = work_space_obj.pdb_filename, 
                          gro_filename = work_space_obj.gro_filename, 
                          gfda_version = work_space_obj.gfda_version)
