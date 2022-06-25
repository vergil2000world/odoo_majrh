from odoo import fields,api,models,_
from odoo.exceptions import ValidationError


class MAJRHEchelon(models.Model):
    _name="majrh.echelon"
    _description="Les Echelons (MAJ RH)"
    
    grade_id=fields.Many2one('majrh.grade',string="Grade")
    echelon=fields.Integer('Echelon')
    code=fields.Char("Code")
    name=fields.Char("Nom")
    
    _rec_name='name'
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