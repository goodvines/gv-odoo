from odoo import api, SUPERUSER_ID


def migrate(cr, version):

    cr.execute("""
        update ir_ui_view v
        set active = false
        where
        v.id in (3322,)
    """)
