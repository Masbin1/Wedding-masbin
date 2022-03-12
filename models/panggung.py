from odoo import api, fields, models


class Panggung(models.Model):
    _name = 'wedding.panggung'
    _description = 'Panggung Deskripsi'

    name = fields.Char(string='Name')
    pelaminan = fields.Many2one(comodel_name='wedding.pelaminan', string='Tipe Pelaminan')
    bunga = fields.Selection(string='Bunga', selection=[('bunga hidup', 'bunga hidup'), ('bunga mati', 'bunga mati'),])
    accesories = fields.Char(string='Accessories Pelaminan')
    harga = fields.Char(compute='_compute_harga', string='Harga')
    
    @api.depends('')
    def _compute_harga(self):
        for record in self:
            record.harga = harga.pelaminan.harga
