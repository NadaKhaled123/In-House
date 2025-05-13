import frappe
from erpnext.stock.doctype.delivery_note.delivery_note import DeliveryNote 

class CustomDeliveryNote(DeliveryNote):
   def on_submit(self):
        super().on_submit()
        for dn_item in self.get("items", []):
            so_name = dn_item.against_sales_order
            so_detail = dn_item.so_detail 
            if not so_name or not so_detail:
                continue
            so_item = frappe.db.get_value(
                "Sales Order Item",
                so_detail,
                ["qty", "delivered_qty"],
                as_dict=True
            )
            if so_item and so_item.delivered_qty >= so_item.qty:
                work_orders = frappe.get_all(
                    "Work Order",
                    filters={"sales_order": so_name},
                    fields=["name"]
                )
                for wo in work_orders:
                    frappe.db.set_value(
                        "Work Order",
                        wo.name,
                        "status",
                        "Shipped"
                    )
