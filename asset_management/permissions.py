import frappe

PRIVILEGED_ROLES = ("System Manager", "Manager", "Device Team")


def _privileged(user):
    return any(r in frappe.get_roles(user) for r in PRIVILEGED_ROLES)


# Asset Request — employees see only their own
def asset_request_query(user):
    user = user or frappe.session.user
    if _privileged(user):
        return ""
    return "`tabAsset Request`.`requester` = {0}".format(frappe.db.escape(user))


def asset_request_has_permission(doc, ptype=None, user=None):
    user = user or frappe.session.user
    if _privileged(user):
        return True
    if ptype == "create":
        return True
    return doc.requester == user


# Assignment — employees see only what's assigned to them
def assignment_query(user):
    user = user or frappe.session.user
    if _privileged(user):
        return ""
    return "`tabAssignment`.`assigned_to` = {0}".format(frappe.db.escape(user))


def assignment_has_permission(doc, ptype=None, user=None):
    user = user or frappe.session.user
    if _privileged(user):
        return True
    if ptype == "create":
        return True
    return doc.assigned_to == user