from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    dimensions = fields.Char(string="Dimensions")
    materials = fields.Char(string="Materials")


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    mecanization = fields.Boolean(string="Mecanization")
    welding = fields.Boolean(string="Welding")
    painting = fields.Boolean(string="Painting")
    assembly = fields.Boolean(string="Assembly")
    payed_shipping = fields.Boolean(string="Payed Shipping")
