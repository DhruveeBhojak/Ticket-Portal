// Copyright (c) 2025, aavatto and contributors
// For license information, please see license.txt



frappe.ui.form.on('New_client', {
    refresh: function(frm) {
        if (frm.doc.email) {
            frm.add_custom_button(__('Create User'), function() {
                frappe.call({
                    method: 'support_portal.support_portal.doctype.new_client.new_client.create_user_account',
                    args: { name: frm.doc.name },
                    callback: function(r) {
                        if (r.message) {
                            frappe.msgprint(r.message);
                            frm.reload_doc();
                        }
                    }
                });
            });
        }
    }
});