import frappe
from erpnext.manufacturing.doctype.work_order.work_order import WorkOrder 
from frappe.utils import flt

class CustomWorkOrder(WorkOrder):
	def validate(self):
		super().validate()
		if self.docstatus == 0 and self.status != "New":
			self.status =""
			self.status = "New"
			
	def on_submit(self):
		super().on_submit()
		if self.docstatus == 1:
			if self.status != "Stopped":
				self.status = "Order Confirmed"
