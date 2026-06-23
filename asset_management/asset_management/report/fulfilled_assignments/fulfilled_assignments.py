# Copyright (c) 2026, Asset and contributors
# For license information, please see license.txt

# import frappe



import frappe


def execute(filters=None):
    return get_columns(), get_data()


def get_columns():
    return [
        {"label": "Assignment", "fieldname": "name", "fieldtype": "Link", "options": "Assignment", "width": 140},
        {"label": "Asset (Serial)", "fieldname": "asset", "fieldtype": "Link", "options": "Asset", "width": 160},
        {"label": "Category", "fieldname": "asset_name", "fieldtype": "Data", "width": 120},
        {"label": "Model", "fieldname": "model", "fieldtype": "Data", "width": 150},
        {"label": "Assigned To", "fieldname": "assigned_to", "fieldtype": "Link", "options": "User", "width": 200},
        {"label": "Request", "fieldname": "asset_request", "fieldtype": "Link", "options": "Asset Request", "width": 140},
        {"label": "Requested", "fieldname": "request_date", "fieldtype": "Date", "width": 110},
        {"label": "Issued", "fieldname": "date_issued", "fieldtype": "Date", "width": 110},
    ]


def get_data():
    return frappe.db.sql(
        """
        SELECT
            asg.name,
            asg.asset,
            a.asset_name,
            a.model,
            asg.assigned_to,
            asg.asset_request,
            asg.request_date,
            asg.date_issued
        FROM `tabAssignment` asg
        LEFT JOIN `tabAsset` a ON a.name = asg.asset
        ORDER BY asg.date_issued DESC
        """,
        as_dict=True,
    )