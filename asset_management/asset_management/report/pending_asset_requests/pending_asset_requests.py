# Copyright (c) 2026, Asset and contributors
# For license information, please see license.txt

# import frappe


import frappe


def execute(filters=None):
    return get_columns(), get_data()


def get_columns():
    return [
        {"label": "Request ID", "fieldname": "name", "fieldtype": "Link", "options": "Asset Request", "width": 140},
        {"label": "Requester", "fieldname": "requester", "fieldtype": "Link", "options": "User", "width": 200},
        {"label": "Asset", "fieldname": "asset_name", "fieldtype": "Data", "width": 130},
        {"label": "Urgency", "fieldname": "urgency", "fieldtype": "Data", "width": 100},
        {"label": "Request Date", "fieldname": "request_date", "fieldtype": "Date", "width": 120},
    ]


def get_data():
    return frappe.db.get_all(
        "Asset Request",
        filters={"status": "Pending Request"},
        fields=["name", "requester", "asset_name", "urgency", "request_date"],
        order_by="request_date asc",
    )