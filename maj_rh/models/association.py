from odoo import models,fields,api,_
from odoo import exceptions


class MajRhAssociation(models.Model):
    _name="majrh.association"
    _description="Ce modéle associe Fonction & Employé"
    
    fonction_id=fields.Many2one('majrh.fonction','fonction')
    employee_id=fields.Many2one('hr.employee','Employee')
    date_grade=fields.Date('Date Grade')
    date_echelon=fields.Date('Date Echelon')
    
    
    
    _rec_name="fonction_id"
    