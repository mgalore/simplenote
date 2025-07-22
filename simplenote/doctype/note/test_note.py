# Copyright (c) 2025, Your Name and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase

class TestNote(FrappeTestCase):
	def test_note_creation(self):
		"""Test basic note creation"""
		note = frappe.get_doc({
			"doctype": "Note",
			"title": "Test Note",
			"content": "This is a test note content",
			"tags": "test, sample"
		})
		note.insert()
		
		# Check if note was created successfully
		self.assertEqual(note.title, "Test Note")
		self.assertEqual(note.content, "This is a test note content")
		self.assertEqual(note.tags, "test, sample")
		self.assertEqual(note.created_by, frappe.session.user)
		
		# Clean up
		note.delete()
	
	def test_tag_cleanup(self):
		"""Test that tags are cleaned up properly"""
		note = frappe.get_doc({
			"doctype": "Note",
			"title": "Tag Test Note",
			"content": "Testing tag cleanup",
			"tags": " TEST , Sample , Another Tag "
		})
		note.insert()
		
		# Check if tags were cleaned up
		self.assertEqual(note.tags, "test, sample, another tag")
		
		# Clean up
		note.delete()
	
	def test_title_required(self):
		"""Test that title is required"""
		note = frappe.get_doc({
			"doctype": "Note",
			"content": "This note has no title"
		})
		
		# Should raise an error
		with self.assertRaises(frappe.ValidationError):
			note.insert()