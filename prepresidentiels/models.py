from django.db import models


class prepresidentiel(models.Model):
    prenom = models.TextField(db_column='Prenom')  # Field name made lowercase.
    nom = models.TextField(db_column='Nom')  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.nom