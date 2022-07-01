from turtle import title
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Produit(models.Model):
    """Model definition for Produit."""
    titre = models.CharField(("Title"),max_length=250)
    prix = models.FloatField(_("Price"))
    # TODO: Define fields here

    class Meta:
        """Meta definition for Produit."""

        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'

    # ToString()
    def __str__(self):
        return f'[{self.titre}:{self.prix}]'


        