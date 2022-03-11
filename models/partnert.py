from odoo import api, fields, models


class Partner(models.Model):
    _name = 'wedding.partner'
    _description = 'Stardar Class partners'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='')
    
