from odoo import api, fields, models


class Panggung(models.Model):
    _name = 'wedding.panggung'
    _description = 'Panggung Deskripsi'

    name = fields.Char(string='Name')
    pelaminan = fields.Char(string='Tipe Pelaminan')
    bunga = fields.Char(string='bunga')
    accesories = fields.Char(string='Accessories Pelaminan')
    harga = fields.Integer(string='Harga Sewa')
    
    
    
