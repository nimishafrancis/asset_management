# Copyright (c) 2026, Asset and contributors
# For license information, please see license.txt

# import frappe



import frappe


def execute(filters=None):
    return get_columns(), get_data()


def get_columns():
    return [
        {"label": "Serial No", "fieldname": "name", "fieldtype": "Link", "options": "Asset", "width": 160},
        {"label": "Category", "fieldname": "asset_name", "fieldtype": "Data", "width": 130},
        {"label": "Model", "fieldname": "model", "fieldtype": "Data", "width": 160},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 130},
        {"label": "Assigned To", "fieldname": "assigned_to", "fieldtype": "Link", "options": "User", "width": 200},
    ]


def get_data():
    return frappe.db.get_all(
        "Asset",
        fields=["name", "asset_name", "model", "status", "assigned_to"],
        order_by="status asc, asset_name asc",
    )