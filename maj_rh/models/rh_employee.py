from odoo import models,fields,api,_
from odoo import exceptions
import re
import datetime


class MajRhemployee(models.Model):
    _name="hr.employee"
    _inherit=["hr.employee","resource.resource"]
    _check_company_auto = True
   
    
    doc_ids=fields.One2many("ir.attachment","employee_id","Documents")
   

    
    department_id2 = fields.Many2one('hr.department',string="Departement", check_company=True)
    description=fields.Char("Description")
    state=fields.Char("state",tracking=True)
    source=fields.Many2one("bo.etablissement",required=True)
  
    
    
    
    
    name=fields.Char(string='Nom complet')
    nom=fields.Char(string="Nom",required=True)
    prenom=fields.Char(string="Prénom",required=True)
    _rec_name="name"
    company_id=fields.Many2one("res.company",required=True,string="Etablissement",default=lambda self:self.env.user.company_id)
    email=fields.Char("Email")
    
    
    nom_ar=fields.Char(string="إسم العائلي",required=True)
    prenom_ar=fields.Char(string="إسم الشخصي",required=True)
    fonction=fields.Many2many('hru.fonction',required=True)
   
    gendre=fields.Selection([('F','Femme'),('M','Homme'),('u','autre')],required=True,string="Genre")
    
    tel=fields.Char(string="Télephone")
    email_inst=fields.Char(string="Email Institutionnel")
    # //email institutionnel
    nppr=fields.Integer(string="NPPR")
    d_a_menperes=fields.Date(string='D-A-MENFPESRS')
    address=fields.Char(string="Address")
    categorie=fields.Char(string="categorie")
    diplome=fields.Many2one('majrh.res.diplome',string="Diplome")
    specialite=fields.Char(string="Specialité")
    universite=fields.Char(string="Université")
    
    nb_diplome=fields.Integer(string="Nombre de diplome")
    nat=fields.Many2one("res.country","Nationalité")
    nat_ar=fields.Many2one("res.country","جنسية")
    tel=fields.Char("Télephone")
    Lieu_Naissance=fields.Char(string="Lieu de naissance")
    situation_familiale_ar=fields.Selection(string="الحالة العائلية", selection=([('m','متزوج'),('d','أعزب')]))    
    situation_familiale=fields.Selection(string="situation familiale", selection=([('m','marié'),('c','célibataire')]))
    date_naiss=fields.Date(string='Date de naissance')
    cin=fields.Char("CIN")
    adresse_fam=fields.Char("Adresse")
    relation=fields.Selection(string="Relation", selection=([('p','père'),('m','mère'),('f','frère'),('s','soeur')]))
    nom_u=fields.Char("Nom complet")
    num_u=fields.Char("Numéro de telephone")
    ville_id=fields.Many2one("majrh.ville","Ville")
    province2=fields.Char(string="province",related="ville_id.province")
    code2=fields.Char(string="code",related="ville_id.code")
    
    
    namer=fields.Many2one("majrh.region","la region")
    name12=fields.Many2one("majrh.qualifications","Nom du diplome")

    
    
    
    namee=fields.Many2one("majrh.etablissement","établissement")
    
    

    
    
    
    
    
   
    
    anciennete_echellon=fields.Char(string="Anciennete echelon",compute="compute_echelon")
    echellon=fields.Integer(string="Echellon")
    type_personne=fields.Selection([('E','enseignant'),('A','adminstratif')],string='Type Personne')
    
    situation_administrative=fields.Selection([('T','titulaire'),('C','contractuaile')],string='Situation administrative',required=True)
    
    date_recrutement=fields.Date(string="Date de recrutement")
    
    
    
    date_affectation_enseignement=fields.Date(string="Date d'affectaion à l'enseignement")
    date_postion=fields.Date(string='Date de position')
    date_effet_grade=fields.Date(string="Date d'effet du grade")
    date_fonction=fields.Date("Date Fonction")
    date_echelon=fields.Date("Date Echelon")
    anciennete_grade=fields.Char(string="Anciennete dans le grade",compute='compute_fct')
    
    
    @api.depends('date_fonction','date_echelon')
    def compute_fct(self):
        date_actuelle=datetime.date.today()
        for rec in self :
            if rec.date_fonction:
                bdate=fields.Datetime.to_datetime(rec.date_fonction).date()
                res=str(int((date_actuelle - bdate).days/ 365))
                rec.anciennete_grade=res+" ans"
            else:
                rec.anciennete_grade=""
    @api.depends('date_echelon')
    def compute_echelon(self):
        date_actuelle=datetime.date.today()
        for rec in self :
            if rec.date_echelon:
                bdate=fields.Datetime.to_datetime(rec.date_echelon).date()
                res=str(int((date_actuelle - bdate).days/ 365))
                rec.anciennete_echellon=res+" ans"
            else:
                rec.anciennete_echellon=""
        
    
       
    
    
    
    
    
    
    @api.model_create_multi
    
    def create(self,vals):
        rec=super(MajRhemployee,self).create(vals)
        
        date_act= datetime.date.today()
        # bdate=rec.date_echelle
        
        
        if  rec.date_recrutement:
            bdate = fields.Datetime.to_datetime(rec.date_fonction).date()
            # total_age= str(int((date_act - bdate).days/30))
            # age=total_age
            duree=rec.fonction.avancement_ids.duree
 
            # datetime.date.today()
            # datetime.date.today() + 
            date_test=datetime.timedelta(duree)+bdate
                
            
            if date_test<rec.date_recrutement :
                   
                    # a=self.env["majrh.cadre"].search([("id","=",(rec.fonction.cadre_id2.id)+1)])
                
                    
                    self.env["majrh.dashboard"].create({
                                                        "name":rec.name
                                                        # ,"prenom":rec.prenom,
                                                        # "fonction_id":rec.fonction.id,
                                                        # "corps_id_src":rec.fonction.corps_id2,
                                                        # "cadre_id_src":rec.fonction.cadre_id2.code,
                                                        # "grade_id_src":rec.fonction.grade_id2,
                                                        # "categorie_id_src":rec.fonction.categorie_id,
                                                        # "echelle_id_src":rec.fonction.echelle_id,
                                                        # "echelon_id_src":rec.fonction.echelon_id,
                                                        # "indice_src":rec.fonction.indice,
                                                        # "cadre_id_des":a.code
                                                        })
                    
                    
                        
        return rec
    
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
    # 

    @api.onchange("nom","prenom","name")
    def change_name(self):
        for rec in self:
            rec.name=""
            if  rec.nom :
                rec.name=rec.name+rec.nom.upper()+" "
            if rec.prenom :
                rec.name=rec.name+rec.prenom.title()+" "  
           
           
            
    @api.constrains("emaili")
    def check_email(self):
        for rec in self :
            if rec.emaili:
                match = re.match('^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$', rec.emaili)
                if match == None:
                    raise ValidationError('Not a valid E-mail')
            
            
            
            
    def action_open(self):
        return {
                'type':'ir.actions.act_window',
                'name': 'Etablissement',
                'res_model':'hr.employee',
                'domain':[('company_id','=',self.id)],
                # 'view_mode':'tree,form',
                'target':'current',
                
                }
            
    def action_open2(self):
        return {
        
                'type':'ir.actions.act_window',
                'name': 'Etat Administratif',
                'res_model':'hr.employee',
                'domain':[('categorie','=',self.id)],
                'view_mode':'tree,form',
                'target':'current',
                
                }    