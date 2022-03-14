from odoo import api, fields, models


class KursiTamu(models.Model):
    _name = 'wedding.kursitamu'
    _description = 'Daftar Kursi Tamu Dan Harga'

    name = fields.Char(string='Name')
    tipe = fields.Selection([('plastik', 'Plastik'),('kayu', 'Kayu'),], string='tipe')
    stok = fields.Integer(string='Stok')
    harga = fields.Integer(string='Harga Sewa Per Unit')