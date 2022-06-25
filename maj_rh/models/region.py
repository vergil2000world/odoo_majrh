from odoo import fields,api,models,_
from odoo import exceptions


class MAJRHregion(models.Model):
    _name="majrh.region"
    _description="region"
    
    name_reg=fields.Char(string="la region")
    
    
    _rec_name="name_reg"
    @api.model
    def create(self,vals):
        
        if self.env["majrh.region"].search([("name_reg","=",vals['name_reg'])]) :
                raise exceptions.UserError("Cette qualification est déja crée!!")
        rec=super(MAJRHregion,self).create(vals)
        return rec
    def write(self,vals):
        if self.env["majrh.region"].search([("name_reg","=",vals['name_reg'])]) :
                raise exceptions.UserError("Cette region est déja crée!!")
        rec=super(MAJRHregion,self).create(vals)
        return rec