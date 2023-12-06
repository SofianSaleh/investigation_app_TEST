import frappe
from frappe.utils import compare

previous = frappe.utils.compare


def before(doc, event):
    if doc.grand_total < 0:
        frappe.utils.compare = monkey


def after(doc, event):
    frappe.utils.compare = previous


def monkey(val1, condition, val2, fieldtype: str | None = None):
    from frappe.utils.data import operator_map, cast

    # print(val1, condition, val2, type(val1) is float, 'test')
    ret = False
    if type(val1) is float:
        if val1 < 0:
            return True

    if fieldtype:
        val1 = cast(fieldtype, val1)
        val2 = cast(fieldtype, val2)
    if condition in operator_map:
        ret = operator_map[condition](val1, val2)

    return ret
    print()
    return False
