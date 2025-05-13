frappe.listview_settings['Work Order'] = {
  get_indicator: function (doc) {
    if (doc.status == 'New') {
      return [__('New'), 'blue', 'status,=,New'];
    }
    else if (doc.status == 'Order Confirmed') {
      return [__('Order Confirmed'), 'light-blue', 'status,=,Order Confirmed'];
    }
    else if (doc.status == 'Not Started') {
      return [__('Not Started'), 'orange', 'status,=,Not Started'];
    }
    else if (doc.status == 'In Process') {
      return [__('In Process'), 'purple', 'status,=,In Process'];
    }
    else if (doc.status == 'In Factory') {
      return [__('In Factory'), 'teal', 'status,=,In Factory'];
    }
    else if (doc.status == 'Quality Inspected') {
      return [__('Quality Inspected'), 'yellow', 'status,=,Quality Inspected'];
    }
    else if (doc.status == 'In Warehouse') {
      return [__('In Warehouse'), 'green', 'status,=,In Warehouse'];
    }
    else if (doc.status == 'Shipped') {
      return [__('Shipped'), 'gray', 'status,=,Shipped'];
    }
    return [__(doc.status), 'black', `status,=,${doc.status}`];
  }
};
