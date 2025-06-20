# Copyright (c) 2025, aavatto and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from frappe import _

class New_client(Document):
    pass
@frappe.whitelist()
def create_user_account(name):
    # Fetch the Client document using the name passed from JS
    doc = frappe.get_doc("New_client", name)
    print(doc.name,'-name------')
    if not doc.email:
        frappe.throw(_("Client does not have an email."))

    # Check if user already exists
    if frappe.db.exists("User", doc.email):
        frappe.throw(_("A user with this email already exists."))

    # Create new User
    user = frappe.new_doc("User")
    user.email = doc.email
    user.first_name = doc.client_name
    user.send_welcome_email = 1
    user.append("roles", {"role": "Client"})
    user.save(ignore_permissions=True)
    frappe.db.commit()
    perm = frappe.new_doc("User Permission")
    
    perm.user = user.name
    perm.allow = "New_client"
    perm.for_value = doc.name
    perm.apply_to_all_doctypes = 1
    perm.save()
    frappe.db.commit()
    return _("User created successfully.")


