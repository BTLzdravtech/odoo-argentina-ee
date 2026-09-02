from odoo import models
from odoo.addons.account.models.account_move import AccountMove as AccountMoveOriginal


class AccountMove(models.Model):
    _inherit = "account.move"

    def action_open_business_doc(self):
        self.ensure_one()
        if self.company_id.country_id.code == "AR" and self.statement_line_id and self.payment_ids:
            return AccountMoveOriginal.action_open_business_doc(self)
        return super().action_open_business_doc()
