from odoo import api, fields, models


class Panggung(models.Model):
    _name = 'wedding.panggung'
    _description = 'Panggung Deskripsi'

    name = fields.Char(string='Name')
    pelaminan = fields.Char(string='Tipe Pelaminan')
    bunga = fields.Selection(string='Bunga', selection=[('bunga hidup', 'bunga hidup'), ('bunga mati', 'bunga mati'),])
    accesories = fields.Char(string='Accessories Pelaminan')
    harga = fields.Integer(string='Harga Sewa')
    
    
    
