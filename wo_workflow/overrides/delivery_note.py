import frappe
from erpnext.stock.doctype.delivery_note.delivery_note import DeliveryNote 

class CustomDeliveryNote(DeliveryNote):
   def on_submit(self):
        super().on_submit()

        # For each fully delivered Sales Order item linked to a Work Order,
        # update that Work Order's status to Shipped

        for dn_item in self.get("items", []):
            so_name = dn_item.against_sales_order
            so_detail = dn_item.so_detail 
            if not so_name or not so_detail:
                continue

            # Retrieve the ordered vs delivered quantities from the Sales Order Item
            so_item = frappe.db.get_value(
                "Sales Order Item",
                so_detail,
                ["qty", "delivered_qty"],
                as_dict=True
            )
            # Retrieve the ordered vs delivered quantities from the Sales Order Item
            if so_item and so_item.delivered_qty >= so_item.qty:
                work_orders = frappe.get_all(
                    "Work Order",
                    filters={"sales_order": so_name},
                    fields=["name"]
                )
                # Mark each Work Order as Shipped
                for wo in work_orders:
                    frappe.db.set_value(
                        "Work Order",
                        wo.name,
                        "status",
                        "Shipped"
                    )
