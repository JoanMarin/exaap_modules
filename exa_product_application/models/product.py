from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    apllication_ids = fields.Many2many(comodel_name="product.application",
                                       string="Product Application")