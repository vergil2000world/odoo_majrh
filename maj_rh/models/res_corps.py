from odoo import fields,api,models,_
from odoo.exceptions import ValidationError

class MAJRHCorps(models.Model):
    _name="majrh.corps"
    
    
    _description="Les Corps (MAJ RH)"
   
    category_id=fields.Many2one('majrh.categories',string="Catégorie")
    code=fields.Char("Code")
    name=fields.Char("Nom")
    
    _rec_name='name'
    
    # @api.constrains('name')
    # def check_name(self):
        # a=[]
        # i=0
        # for rec in self:
            # if (rec.name).isdigit()  :
          
                 # raise ValidationError('Entrer un Champ Valide name doit etre deux nombres séparés par - ')
            # elif   isinstance(rec.name, str):
                 # raise ValidationError('Entrer un Champ Valide name doit etre deux nombres séparés par - ')
            # else :
                # a=rec.name.split('-')
                # for i in range(len(a)):
                    # if  a[i].isdigit()==0 :
                        # raise ValidationError('Entrer un Champ Valide')
    
    