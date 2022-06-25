from odoo import models,fields,api,_
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError


class MajRhechellon(models.Model):
    _name="hr.echellon"
    _description="Ce module gére les avencements echellons"
    
    grade_id=fields.Integer("Grade")
    
    echellon=fields.Integer("Echellon")
    code=fields.Integer("Code")
    name=fields.Char("Name")
    
    
    @api.constrains('code')
    def check_code(self):
        
        test=self.env['hr.echellon'].search_count([('code','=',self.code)])
        if test!=0:
            raise ValidationError('Le code doit etre Unique')
    
    
    
    
    @api.constrains('name')
    def check_name(self):
        a=[]
        i=0
        for rec in self:
            if (rec.name).isdigit()  :
          
                 raise ValidationError('Entrer un Champ Valide name doit etre deux nombres séparés par - ')
            # elif   isinstance(rec.name, str):
                 # raise ValidationError('Entrer un Champ Valide name doit etre deux nombres séparés par - ')
            else :
                a=rec.name.split('-')
                for i in range(len(a)):
                    if  a[i].isdigit()==0 :
                        raise ValidationError('Entrer un Champ Valide')