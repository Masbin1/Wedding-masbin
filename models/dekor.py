from odoo import api, fields, models


class Dekor(models.Model):
    _name = 'wedding.dekor'
    _description = 'Model Untuk Tabel Dekor'

    name = fields.Char(string='Nama Dekorasi')
    harga = fields.Integer(string='Harga Dekorasi')
    deskripsi = fields.Char(string='Deskripsi Dekorasi')
    
    
