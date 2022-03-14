from odoo import api, fields, models


class Order(models.Model):
    _name = 'wedding.order'
    _description = 'New Description'

    orderdetail_ids = fields.One2many(
        comodel_name='wedding.orderdetail',
        inverse_name='order_id', 
        string='Orde Detail')
    name = fields.Char(string='Kode order', required=True)



class OrderDetail(models.Model):
    _name = 'wedding.orderdetail'
    _description = 'New Description'


    order_id = fields.Many2one(comodel_name='wedding.order', string='Order')
    
    name = fields.Selection([
        ('panggung', 'panggung'),
        ('kursi tamu', 'kursi tamu')], string='name')
