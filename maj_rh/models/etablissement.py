from odoo import fields,api,models,_
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError



class MAJRHetablissement(models.Model):
    _name="majrh.etablissement"
    _description="etablissement"
    
    name=fields.Char(string="établissement")
    
    
    _rec_name="name"
    
    # @api.constrains('name')
    # def test_name(self):
        # for rec in self:
            # enrg=self.env["majrh.etablissement"].search([("name","=",rec.name)])   
            # enrg=enrg and enrg[0] or False
            # if  enrg :
                        # raise UserError("Cet etablissement est déja crée!!")
                
    
    