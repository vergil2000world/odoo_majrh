from odoo import fields,api,models,_
from odoo import exceptions


class MAJRHville(models.Model):
    _name="majrh.ville"
    _description="ville"
    
    name=fields.Char(string="Nom du ville")
    province=fields.Char(string="Province de ville")
    code=fields.Char(string="Code du ville")
    
    
    _rec_name="name"
    @api.model
    def create(self,vals):
        
        if self.env["majrh.ville"].search([("name","=",vals['name']),("code","=",vals['code']),("province","=",vals['province'])]) :
                raise exceptions.UserError("Cette ville est déja crée!!")
        rec=super(MAJRHville,self).create(vals)
        return rec
    def write(self,vals):
        if self.env["majrh.ville"].search([("name","=",vals['name']),("code","=",vals['code']),("province","=",vals['province'])]) :
                raise exceptions.UserError("Cette ville est déja crée!!")
        rec=super(MAJRHville,self).create(vals)
        return rec
            

                        
