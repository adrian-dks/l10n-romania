# Copyright (C) 2022 Dakai Soft
# -*- coding: utf-8 -*-
from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    stock_valuation_ids = fields.One2many("stock.valuation.layer", "stock_move_line_id")
