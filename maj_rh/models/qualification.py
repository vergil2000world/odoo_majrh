from odoo import fields,api,models
from odoo import exceptions


class MAJRHqualification(models.Model):
    _name="majrh.qualifications"
    _description="Qualifications"
    id12=fields.Char(string="ID du diplome")
    name=fields.Char(string="Nom du diplome")
    _rec_name="name"
    
    @api.model
    def create(self,vals):
        
        if self.env["majrh.qualifications"].search([("name","=",vals['name']),("id12","=",vals['id12'])]) :
                raise exceptions.UserError("Cette qualification est déja crée!!")
        rec=super(MAJRHqualification,self).create(vals)
        return rec
    def write(self,vals):
        if self.env["majrh.qualifications"].search([("name","=",vals['name']),("id12","=",vals['id12'])]) :
                raise exceptions.UserError("Cette qualifications est déja crée!!")
        rec=super(MAJRHqualification,self).create(vals)
        return rec
            