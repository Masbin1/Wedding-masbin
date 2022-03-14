from importlib.metadata import requires
from odoo import api, fields, models


class Panggung(models.Model):
    _name = 'wedding.panggung'
    _description = 'Panggung Deskripsi'

    name = fields.Char(string='Nama', required=True)
    pelaminan_id = fields.Many2one(
        comodel_name='wedding.pelaminan', 
        string='Tipe Pelaminan', 
        required=True,
        domain=[('harga','>','900000')]
        )
    kursipengantin_id = fields.Many2one(
        comodel_name='wedding.kursipengantin', 
        string='Kursi Pengantin',
        required=True,)
    
    bunga = fields.Selection(string='Bunga', selection=[('bunga hidup', 'bunga hidup'), ('bunga mati', 'bunga mati'),])
    accesories = fields.Char(string='Accessories Pelaminan')
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    
    @api.depends('pelaminan_id','kursipengantin_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.pelaminan_id.harga + record.kursipengantin_id.harga

    stok = fields.Integer(string='Stok Paket Panggung')
    des_pelaminan = fields.Char(compute='_compute_des_pelaminan', string='Deskripsi Pelaminan')
    
    @api.depends('pelaminan_id')
    def _compute_des_pelaminan(self):
        for record in self:
            record.des_pelaminan = record.pelaminan_id.deskripsi
    
    des_kursipengantin = fields.Char(compute='_compute_des_kursipengantin', string='Deskripsi Kursi Pengantin')
    
    @api.depends('kursipengantin_id')
    def _compute_des_kursipengantin(self):
        for record in self:
            record.des_kursipengantin = record.kursipengantin_id.deskripsi