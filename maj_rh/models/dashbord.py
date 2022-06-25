from odoo import models,api,fields,_
from odoo import exceptions

class MajRhDashboard(models.Model):
    _name="majrh.dashboard"
    _description="Dashboard"
    
    name=fields.Char("Nom Complet")
    date=fields.Date("Date")
    duree=fields.Char("Durée")
    
    #  @api.model
    
    # def check_employee_fct(self):
        # record_ids=self.env['hr.employee'].search(['fonction','=',True])
        # for rec in record_ids:
            # self.name=rec.nom
        # return 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # @api.model_create_multi
    
        
    # def create(self,vals):
        # rec=super(MajRhemployee,self).create(vals)
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
        # rec=super(MajRhemployee,self).write(vals)

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
        
    
    # def write(self,vals):
        # if  self.env["hru.avancement"].search(["fonction_id","=",self.fonction.id]) == 1:
            # val['nom']=self.nom
            # self.env["hru.avancement"].search(["nom","=",vals.get('nom')).write(val)
            
               
        # rec=super(MajRhemployee,self).write(vals)
        # return rec
        
        
     
    
        
        
        
            
       
            
            
        # a=self.env["majrh.cadre"].search([("id","=",(rec.fonction.cadre_id2.id)+1)]) 
        
        # vals.update({
                                                                    # "nom":self.nom,
                                                                    # "prenom":self.prenom
                                                                    # ,"fonction_id":self.fonction.id,
                                                                    # "corps_id_src":self.fonction.corps_id2,
                                                                    # "cadre_id_src":self.fonction.cadre_id2,
                                                                    # "grade_id_src":self.fonction.grade_id2,
                                                                    # "categorie_id_src":self.fonction.categorie_id,
                                                                    # "echelle_id_src":self.fonction.echelle_id,
                                                                    # "echelon_id_src":self.fonction.echelon_id,
                                                                    # "indice_src":self.fonction.indice,
                                                                    # "cadre_id_des":a.code
                                                                  # })
        # if self.env["hru.avancement"].search([("fonction_id","=",rec.fonction.id)]) :
        # vals['cadre_id_src']=rec.fonction.cadre_id2
                                         
        
        # return rec
    