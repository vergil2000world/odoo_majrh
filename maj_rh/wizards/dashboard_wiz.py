from odoo import models,fields,api
import datetime
from odoo import exceptions

class OACreatevWizard(models.TransientModel):
    _name="hr.avancementusms"
    # _inherit='hr.employee'
    _description="Search an avancement"
    date_avancement=fields.Date("Date")
    
    
    
       
    def search_avancement(self):
        # print("hello")
       
        fonctions = self.env['hr.employee'].search([("fonction.state","=",'a')])
        # date_act= datetime.date.today()
        # rec=[]
        for rec in fonctions :
            
                bdate = fields.Datetime.to_datetime(rec.date_fonction).date()
                
                duree=rec.fonction.avancement_ids.duree
                
                date_test=datetime.timedelta(duree)+bdate
                # views = [(self.env.ref('account.invoice_supplier_tree').id, 'tree'), (self.env.ref('account.invoice_supplier_form').id, 'form')]
                
                if date_test.strftime('%Y-%m-%d')<=self.date_avancement.strftime('%Y-%m-%d') :
                    
                    return {
                            'type':'ir.actions.act_window',
                            'name': 'Search Avancement',
                            'res_model':'hr.employee',
                            
                            # 'domain':[('date_fonction.strftime('%Y-%m-%d')+datetime.timedelta(fonction.avancement_ids.duree).strftime('%Y-%m-%d')','=',self.date_avancement.strftime('%Y-%m-%d')],
                            'view_mode':'tree',
                            'target':'popup',
                            
                            
                            }
        
                                     
            
    
    # def action_creation_apply(self):
        # leads2 = self.env['oa.score'].browse(self.env.context.get('active_ids'))
        # return leads.action_set_lost(s_id=self.s_id.id)
    
    
    