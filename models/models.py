# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TodoApp(models.Model):
    _name = "todo.app"
    _description = "Gestion de Notas"

    name = fields.Char(string="T")
    price = fields.Char(string="")
