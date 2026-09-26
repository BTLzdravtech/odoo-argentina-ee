from odoo import api, models


class AccountPartialReconcile(models.Model):
    _inherit = "account.partial.reconcile"

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        returns = res.mapped("debit_move_id.move_id.closing_return_id") | res.mapped(
            "credit_move_id.move_id.closing_return_id"
        )
        returns = returns.filtered(lambda account_return: account_return.company_id.country_id.code == "AR")
        if returns:
            returns._update_payment_state()
        return res

    def unlink(self):
        returns = self.mapped("debit_move_id.move_id.closing_return_id") | self.mapped(
            "credit_move_id.move_id.closing_return_id"
        )
        returns = returns.filtered(lambda account_return: account_return.company_id.country_id.code == "AR")
        res = super().unlink()
        if returns:
            returns._update_payment_state()
        return res
