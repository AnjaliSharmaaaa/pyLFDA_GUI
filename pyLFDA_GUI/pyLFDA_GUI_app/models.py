from django.db import models

# Create your models here.
class workspace(models.Model):
    experiment_name  = models.CharField("Experiment name", max_length=128, blank=False, unique=True, null=False)
    workspace_folder = models.CharField("Workspace folder", max_length=128, blank=False, null=False)
    pdb_filename = models.FilePathField(path='E:/Project/LFDA/testfiles', allow_files=True, allow_folders=False, max_length=200)
    gro_filename = models.FilePathField(path='E:/Project/LFDA/testfiles', allow_files=True, allow_folders=False, max_length=200)
    trr_filename = models.FilePathField(path='E:/Project/LFDA/testfiles', allow_files=True, allow_folders=False, max_length=200)
    tpr_filename = models.FilePathField(path='E:/Project/LFDA/testfiles', allow_files=True, allow_folders=False, max_length=200)
    ndx_filename = models.FilePathField(path='E:/Project/LFDA/testfiles', allow_files=True, allow_folders=False, max_length=200)
    gfda_version = models.CharField("G-LFDA folder/version", max_length=128, blank=False, null=False)
    
    def __str__(self):
        return str(self.experiment_name)