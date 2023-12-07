import frappe
from frappe.utils import compare

previous = frappe.utils.compare


def before(doc, event):
    if doc.grand_total < 0:
        frappe.utils.compare = patched_compare


def after(doc, event):
    frappe.utils.compare = previous


def patched_compare(val1, condition, val2, fieldtype: str | None = None):
    from frappe.utils.data import operator_map, cast

    pattern = f'{condition} {val2} {type(val1)}'
    aob_search = ">= 0.0 <class 'float'>"
    if aob_search in pattern.lower():
        print(val1)
        return True
    ret = False

    if fieldtype:
        val1 = cast(fieldtype, val1)
        val2 = cast(fieldtype, val2)
    if condition in operator_map:
        ret = operator_map[condition](val1, val2)

    return ret
    print()
    return False

# def patched_validate_value():
#     pass
