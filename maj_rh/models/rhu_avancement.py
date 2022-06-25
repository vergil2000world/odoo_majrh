from odoo import models,fields,api


class MajRhavancement(models.Model):
    _name="hru.avancement"
    _description="Avancement"
    _rec_name="fonction_id"
    
    
    #####################
    fonction_id=fields.Many2one("hru.fonction",string="Fonction")
    
    
    # parametre de source
    corps_id_src=fields.Integer(string='Corps récent' )  
    cadre_id_src=fields.Integer(string='Cadre récent')
    grade_id_src=fields.Integer('Grade récent')
    categorie_id_src=fields.Integer('Categorie récent')
    echelle_id_src=fields.Integer('Echelle récent')
    echelon_id_src=fields.Integer('Echelon récent')
    indice_src=fields.Integer('Indice récent') 
   
   #parametre de destination
    corps_id_des=fields.Integer('Corps aprévue')
    cadre_id_des=fields.Integer('Cadre aprévue')
    grade_id_des=fields.Integer('Grade aprévue')
    categorie_id_des=fields.Integer('Categorie aprévue')
    echelle_id_des=fields.Integer('Echelle aprévue')
    echelon_id_des=fields.Integer('Echelon aprévue')
    indice_des=fields.Integer('Indice aprévue')
    
    ##################
    duree=fields.Integer('Durée')
    state=fields.Selection(string="State",selection=([('B','Brouillant'),('V','Validé'),('C','Confirmé')]))
    
   
    