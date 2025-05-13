import frappe
from erpnext.stock.doctype.quality_inspection.quality_inspection import QualityInspection 

class CustomQualityInspection(QualityInspection):
    def validate(self):
        super().validate() 
        if self.reference_type == "Stock Entry":
            se = frappe.get_doc("Stock Entry", self.reference_name)
            if se.work_order :
                frappe.db.set_value("Work Order", se.work_order, "status", "Quality Inspected")
