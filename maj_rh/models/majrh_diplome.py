from odoo import models,fields,api


class MajRhDiplome(models.Model):
    _name="majrh.diplome"
    description="Diplome"

    _name="majrh.res.diplome"
    description="Diplome"

    name=fields.Char(string='Diplome')
    _rec_name='name'
    