from erpnext.stock.doctype.stock_entry.stock_entry import StockEntry
import frappe

class CustomStockEntry(StockEntry):
    def validate(self):
        super().validate()
        # If this is a raw-material draft transfer, mark the related Work Order as Not Started
        if self.purpose == "Material Transfer for Manufacture" and self.docstatus == 0 :
            frappe.db.set_value(
                "Work Order",
                self.work_order,
                "status",
                "Not Started"
            )
    def on_submit(self):
            super().on_submit()
            # After finishing manufacture in the factory, set Work Order status to In Factory
            if self.purpose == "Manufacture" and self.work_order:
                frappe.db.set_value(
                    "Work Order",
                    self.work_order,
                    "status",
                    "In Factory"
                )
            # Once the finished goods are transferred out of the factory,
            # update the Work Order status to In Warehouse
            if self.purpose == "Material Transfer" and self.work_order and self.docstatus == 1:
                frappe.db.set_value(
                    "Work Order",
                    self.work_order,
                    "status",
                    "In Warehouse"
                )
