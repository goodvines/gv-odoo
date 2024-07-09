from odoo import api, SUPERUSER_ID


def migrate(cr, version):

    cr.execute("""
        update ir_ui_view v
        set set inherit_id = NULL, mode='primary', active = false
        where
        v.id in (3322,)
    """)
