# Copyright (c) 2025, aavatto and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Task_assign(Document):
    def on_update(self):
        if self.ticket_id and self.status:
            frappe.db.set_value("Ticket", self.ticket_id, "status", self.status)

