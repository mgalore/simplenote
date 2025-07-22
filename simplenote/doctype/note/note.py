# Copyright (c) 2025, Your Name and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Note(Document):
	def before_insert(self):
		"""Set created_by and creation_date before inserting"""
		self.created_by = frappe.session.user
		self.creation_date = frappe.utils.now()
		
	def before_save(self):
		"""Set modified_by and modified_date before saving"""
		self.modified_by = frappe.session.user
		self.modified_date = frappe.utils.now()
		
	def validate(self):
		"""Validate the note data"""
		if not self.title:
			frappe.throw("Title is required")
			
		# Clean up tags - remove extra spaces and convert to lowercase
		if self.tags:
			tags = [tag.strip().lower() for tag in self.tags.split(',') if tag.strip()]
			self.tags = ', '.join(tags)
	
	def get_permission_query_conditions(user):
		"""Return permission query conditions for the user"""
		if not user:
			user = frappe.session.user
			
		# Users can only see their own notes
		return f"(`tabNote`.created_by = '{user}')"
	
	def has_permission(doc, user):
		"""Check if user has permission to access this note"""
		if not user:
			user = frappe.session.user
			
		# Users can only access their own notes
		return doc.created_by == user