import frappe
from frappe.model.document import Document


class Employee(Document):
    def after_insert(self):
        if not self.email:
            return

        if not frappe.db.exists("User", self.email):
            user = frappe.new_doc("User")

            user.email = self.email
            user.first_name = self.name1
            user.full_name = self.name1   # ← add this

            user.send_welcome_email = 0
            user.new_password = "Dec?12345"

            user.append("roles", {
                "role": "Employee"
            })

            user.insert(ignore_permissions=True)