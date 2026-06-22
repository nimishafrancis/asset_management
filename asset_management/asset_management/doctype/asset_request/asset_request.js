// Copyright (c) 2026, Asset and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Asset Request", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Asset Request", {
    onload(frm) {
        if (frm.is_new() && !frm.doc.requester) {
            frm.set_value("requester", frappe.session.user);
        }
    },
    refresh(frm) {
        const can_assign =
            frappe.user.has_role("Device Team") || frappe.user.has_role("System Manager");
        if (frm.doc.status === "Approved" && can_assign) {
            frm.add_custom_button("Assign Asset", () => open_assign_dialog(frm));
        }
    },
});

function open_assign_dialog(frm) {
    const d = new frappe.ui.Dialog({
        title: "Assign Asset",
        fields: [
            {
                fieldname: "asset",
                label: "Asset",
                fieldtype: "Link",
                options: "Asset",
                reqd: 1,
                get_query() {
                    return {
                        filters: {
                            asset_name: frm.doc.asset_name,
                            status: "Available",
                        },
                    };
                },
            },
        ],
        primary_action_label: "Create Assignment",
        primary_action(values) {
            frappe.db
                .insert({
                    doctype: "Assignment",
                    asset_request: frm.doc.name,
                    assigned_to: frm.doc.requester,
                    date_requested: frm.doc.request_date,
                    asset: values.asset,
                })
                .then(() => {
                    frappe.show_alert({ message: __("Assignment created"), indicator: "green" });
                    d.hide();
                    frm.reload_doc();
                });
        },
    });
    d.show();
}


