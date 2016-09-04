# -*- coding: utf-8 -*-

from openerp import models, fields, api

class physical_access_control(models.Model):
    _name = 'physical.access.control'
    _description = 'Demo default data'
    name = fields.Char('Name', required=True)
    description = fields.Html('Description')
