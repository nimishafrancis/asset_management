# Copyright (c) 2026, Asset and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AssetRequest(Document):
    def before_insert(self):
        if not self.requester:
            self.requester = frappe.session.user