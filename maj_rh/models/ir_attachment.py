from odoo import api, fields, models


class MajRhattachement(models.Model):
    _name="ir.attachment"
    _inherit="ir.attachment"
    
    employee_id=fields.Many2one('hr.employee',"Employee") 
      