from odoo import models,fields,api
from odoo import exceptions
import datetime


class MajRhfonction(models.Model):
    _name="hru.fonction"
    _description="Fonction"
    _rec_name="categorie_id"
    
    
    categorie_id=fields.Many2one('majrh.categories','Categorie')
    # e=fields.One2many("majrh.association","employee_id")
    
    
    
    
    corps_id2=fields.Many2one('majrh.corps','Corps')
    cadre_id2=fields.Many2one('majrh.cadre','Cadre')
    grade_id2=fields.Many2one('majrh.grade','Grade')
    # test_employee=fields.Many2one('hr.employee')
    
    # date_grade=fields.Date('Date de grade')
    echelle_id=fields.Integer('Echelle')
    # date_echelle=fields.Date('Date echelle')
    echelon_id=fields.Many2one('majrh.echelon','Echellon')
    indice=fields.Integer('Indice')
    state=fields.Selection([('a','active'),('i','Inactive')],string='state')
    avancement_ids=fields.One2many("hru.avancement","fonction_id","Avancements")
    @api.model
    def create(self,vals):
        
        if self.env["hru.fonction"].search([("categorie_id","=",vals['categorie_id']),
        ("corps_id2","=",vals['corps_id2']),
        ("cadre_id2","=",vals['cadre_id2']),
        ("grade_id2","=",vals['grade_id2']),
        ("echelle_id","=",vals['echelle_id']),
        ("echelon_id","=",vals['echelon_id']),
        ("indice","=",vals['indice'])]) :
                raise exceptions.UserError("Cette Fonction est déja crée!!")
        rec=super(MajRhfonction,self).create(vals)
        return rec
    def write(self,vals):
        if self.env["hru.fonction"].search([("categorie_id","=",vals['categorie_id']),
        ("corps_id2","=",vals['corps_id2']),
        ("cadre_id2","=",vals['cadre_id2']),
        ("grade_id2","=",vals['grade_id2']),
        ("echelle_id","=",vals['echelle_id']),
        ("echelon_id","=",vals['echelon_id']),
        ("indice","=",vals['indice'])]) :
                raise exceptions.UserError("Cette Fonction est déja crée!!")
        rec=super(MajRhfonction,self).create(vals)
        return rec
    
    
    @api.onchange('categorie_id')
    def check_corps(self):
        domain={'corps_id2':[('category_id.code','=',self.categorie_id.code)]}
       
        return {'domain':domain}
    @api.onchange('corps_id2')
    def check_cadre(self):
        domain={'cadre_id2':[('corps_id.code','=',self.corps_id2.code)]}
        
        
        return {'domain':domain}
    @api.onchange('cadre_id2')
    def check_grade(self):
        domain={'grade_id2':[('cadre_id.code','=',self.cadre_id2.code)]}
        
        
        return {'domain':domain}
    @api.onchange('grade_id2')
    def check_echelon(self):
        domain={'echelon_id':[('grade_id.code','=',self.grade_id2.code)]}
       
       
        return {'domain':domain}
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # @api.model_create_multi
    
        
    # def create(self,vals):
        # rec=super(MajRhfonction,self).create(vals)
        # date_act= datetime.date.today()
        # bdate=rec.date_echelle
        
        
        # if  rec.date_recrutement:
            # bdate = fields.Datetime.to_datetime(rec.date_recrutement).date()
            # total_age= str(int((date_act - bdate).days/30))
            # age=total_age
                
            # enrg=self.env["hru.avancement"].search([("fonction_id","=",rec.fonction.id)])   
            # enrg=enrg and enrg[0] or False
            # if  enrg :
                        # raise exceptions.UserError("Cet avancement est déja crée!!")
                        
            # else :
                # if int(age)<4 :
                   
                    # a=self.env["majrh.cadre"].search([("id","=",(rec.fonction.cadre_id2.id)+1)])
                
                    
                    # self.env["hru.avancement"].create({
                                                        # "nom":rec.nom,
                                                        # "prenom":rec.prenom,
                                                        # "fonction_id":rec.fonction.id,
                                                        # "corps_id_src":rec.fonction.corps_id2,
                                                        # "cadre_id_src":rec.fonction.cadre_id2.code,
                                                        # "grade_id_src":rec.fonction.grade_id2,
                                                        # "categorie_id_src":rec.fonction.categorie_id,
                                                        # "echelle_id_src":rec.fonction.echelle_id,
                                                        # "echelon_id_src":rec.fonction.echelon_id,
                                                        # "indice_src":rec.fonction.indice,
                                                        # "cadre_id_des":a.code})
                    
                    
                        
        # return rec
    
    # def write(self,vals):
        # rec=super(MajRhfonction,self).write(vals)

        # if  self.env["hru.avancement"].search(["fonction_id","=",self.fonction.id]) == 1:
        
        
        # a=self.env["majrh.cadre"].search([("id","=",(self.fonction.cadre_id2.id)+1)])
        # b=self.env["majrh.grade"].search([("id","=",(self.fonction.grade_id2.id)+1)])
        # c=self.env["majrh.corps"].search([("id","=",(self.fonction.corps_id2.id)+1)])
        # d=self.env["majrh.echelon"].search([("id","=",(self.fonction.echelon_id.id)+1)])
        # e=self.env["majrh.indice"].search([("id","=",(self.fonction.echelon_id.id)+1)])
        
        
        # self.fonction.avancement_ids.nom=self.nom
        # self.fonction.avancement_ids.prenom=self.prenom
        # self.fonction.avancement_ids.corps_id_src=self.fonction.corps_id2.code
        # self.fonction.avancement_ids.cadre_id_src=self.fonction.cadre_id2.code
        # self.fonction.avancement_ids.grade_id_src=self.fonction.grade_id2.code
        # self.fonction.avancement_ids.categorie_id_src=self.fonction.categorie_id.code
        # self.fonction.avancement_ids.echelle_id_src=self.fonction.echelle_id
        # self.fonction.avancement_ids.echelon_id_src=self.fonction.echelon_id
        # self.fonction.avancement_ids.indice_src=self.fonction.indice
        # self.fonction.avancement_ids.corps_id_des=c.code
        # self.fonction.avancement_ids.cadre_id_des=a.code
        # self.fonction.avancement_ids.grade_id_des=b.code
        # self.fonction.avancement_ids.categorie_id_des=self.fonction.categorie_id
        # self.fonction.avancement_ids.echelle_id_des=self.fonction.echelle_id+5
        # self.fonction.avancement_ids.echelon_id_des=d.code
        # self.fonction.avancement_ids.indice_des=self.fonction.indice+5
            
            
               
        # return rec
   
   
   
                
    

    
    
   
    