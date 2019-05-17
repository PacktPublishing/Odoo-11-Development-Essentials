# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PhoneBook(models.Model):
	_name = 'phone.book'
	_description = "Phone Book"

	name = fields.Char(string = "Name", required = True)
	related_partner = fields.Many2one('res.partner', string = "Related Partner")
	date_of_joining = fields.Date(string = "Date of Joining")
	category_id = fields.Many2many('res.partner.category', string = "Tags")
	city = fields.Char(string = "City", required = True)
	street = fields.Char(string = "Street", required = True)
	country_id = fields.Many2one('res.country', string = "Country", required = True)
	