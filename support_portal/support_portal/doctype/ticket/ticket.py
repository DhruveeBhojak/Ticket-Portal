# Copyright (c) 2025, aavatto and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Ticket(Document):
    def after_insert(self):
        users = frappe.get_all("Has Role", filters={"role": "Manager","parenttype":"User"}, pluck="parent")
        for user in users:
            doc = frappe.new_doc("Notification Log")
            doc.subject = self.subject
            doc.email_content = self.description
            doc.for_user = user
            doc.type = 'Alert'
            doc.document_type = 'Ticket'
            doc.document_name = self.name
            doc.save(ignore_permissions=True)

