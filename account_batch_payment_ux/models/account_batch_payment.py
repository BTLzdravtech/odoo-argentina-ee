from odoo import _, models
from odoo.exceptions import RedirectWarning, UserError


class AccountBatchPayment(models.Model):
    _inherit = "account.batch.payment"

    def verify_unlinked_payments_from_batch(self):
        """Protect payments linked to non-draft Argentine batches."""
        ar_batches = self._origin.filtered(lambda batch: batch.company_id.country_id.code == "AR")
        if ar_batches.filtered(lambda batch: batch.state != "draft"):
            raise UserError(
                _("You are not allowed to delete payments from a batch payment if the batch is not on draft state.")
            )

    def unlink(self):
        """Prevent deleting non-draft Argentine batch payments."""
        ar_batches = self.filtered(lambda batch: batch.company_id.country_id.code == "AR")
        if ar_batches.filtered(lambda batch: batch.state != "draft"):
            raise UserError(_("You are not allowed to delete a batch payment if is not on draft state."))
        return super().unlink()

    def action_reset_to_draft(self):
        """Reset unmatched Argentine batch payments to draft."""
        ar_batches = self.filtered(lambda batch: batch.company_id.country_id.code == "AR")
        matched_entries = ar_batches.payment_ids.filtered("is_matched")
        if matched_entries:
            error_msg = "The following payments are reconciled and cannot be reset to draft state: \n"
            for entry in matched_entries:
                error_msg += f"{entry.name} \n"
            action_error = {
                "view_mode": "list",
                "name": _("Matched Entries"),
                "res_model": "account.bank.statement.line",
                "type": "ir.actions.act_window",
                "domain": [("id", "in", matched_entries.mapped("reconciled_statement_line_ids").ids)],
                "views": [
                    (self.env.ref("account_accountant.view_bank_statement_line_kanban_bank_rec_widget").id, "kanban"),
                    (self.env.ref("account_accountant.view_bank_statement_line_tree_bank_rec_widget").id, "list"),
                ],
            }
            raise RedirectWarning(error_msg, action_error, _("Show matched entries"))
        ar_payments = ar_batches.payment_ids
        if ar_payments.move_id:
            ar_payments.move_id.is_move_sent = False
        ar_payments.unmark_as_sent()
        return True
