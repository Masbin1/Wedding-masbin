from odoo import api, fields, models


class Order(models.Model):
    _name = 'wedding.order'
    _description = 'New Description'

    orderdetail_ids = fields.One2many(
        comodel_name='wedding.orderdetail',
        inverse_name='order_id', 
        string='Orde Detail')
    name = fields.Char(string='Kode order', required=True)
    total = fields.Char(compute='_compute_total', string='total', store=True)
    
    @api.depends('orderdetail_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['wedding.orderdetail'].search([('order_id','=',record.id)]).mapped('harga'))
            record.total = a

class OrderDetail(models.Model):
    _name = 'wedding.orderdetail'
    _description = 'New Description'


    order_id = fields.Many2one(comodel_name='wedding.order', string='Order')
    panggung_id = fields.Many2one(comodel_name='wedding.panggung', string='Panggung')
    name = fields.Selection([
        ('panggung', 'panggung'),
        ('kursi tamu', 'kursi tamu')], string='name')
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    qty = fields.Integer(string='Quantity')
    harga_satuan = fields.Char(compute='_compute_harga_satuan', string='Harga Satuan')
    
    @api.depends('panggung_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.panggung_id.harga
    
    
    @api.depends('qty','harga_satuan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.panggung_id.harga * record.qty
