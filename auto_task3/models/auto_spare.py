# -*- coding: utf-8 -*-
""" Auto Spare """
from odoo import api, fields, models, _
from odoo.exceptions import UserError, Warning, ValidationError 


class ProductTemplate(models.Model):
    """ inherit Product Template """
    _inherit = 'product.template'

    @api.onchange('type')
    def onchange_type(self):
        if self.type == 'service':
            self.barcode = False



class AutoTask3(models.Model):
    """ Auto Task 3 """
    _name = 'auto.task3'
    _description = 'Auto Task 3'




