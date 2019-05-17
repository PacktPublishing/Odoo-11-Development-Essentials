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
	address_for_printing = fields.Char('Printing Address')
	address = fields.Char('Full Address', compute='_calculate_address')
	

	def print_name(self):
		print("Name of record: %s" %self.name)
		return True 

	api.depends('country_id','city','street')
	def _calculate_address(self):
		full_address = self.country_id.name + ' ,' + self.city + ' ,' + self.street
		self.address = full_address

	@api.model
	@api.onchange('name')
	def return_full_address(self):
		if self.name and self.address:
			self.address_for_printing ='customer: ' + self.name + ' ' + self.address
	
	@api.model
	def create(self, values):
		if 'name' in values:
			values['name'] = values['name'].upper()
			new_rec = super(PhoneBook, self).create(values)
			return new_rec

	@api.multi
	def write(self, values, context = None):
		if 'name' in values:
			values['name'] = values['name'].upper()
			old_rec = super(PhoneBook, self).write(values)
		else:
			old_rec = super(PhoneBook, self).write(values)
		return True

	@api.multi
	def unlink(self):
		for rec in self:
			if rec.name == 'JOHN':
				raise NameError('Record with name JOHN cannot be deleted')















	

	

	 
		
	