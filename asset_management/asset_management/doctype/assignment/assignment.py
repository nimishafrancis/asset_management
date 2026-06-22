# Copyright (c) 2026, Asset and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today


class Assignment(Document):
    def before_validate(self):
        if self.asset_request:
            req = frappe.db.get_value(
                "Asset Request", self.asset_request,
                ["requester", "request_date"], as_dict=True,
            )
            if req:
                self.assigned_to = self.assigned_to or req.requester
                self.date_requested = self.date_requested or req.request_date
        if not self.date_issued:
            self.date_issued = today()
        if self.is_new():
            status = frappe.db.get_value("Asset", self.asset, "status")
            if status != "Available":
                frappe.throw(f"Asset {self.asset} isn't available (status: {status}).")

    def after_insert(self):
        frappe.db.set_value("Asset", self.asset, {"status": "Assigned", "assigned_to": self.assigned_to})
        frappe.db.set_value("Asset Request", self.asset_request, "status", "Fulfilled")