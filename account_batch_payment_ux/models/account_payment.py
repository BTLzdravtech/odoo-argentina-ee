from odoo import models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    def unlink(self):
        ar_batches = self.mapped("batch_payment_id").filtered(lambda batch: batch.company_id.country_id.code == "AR")
        if ar_batches:
            ar_batches.verify_unlinked_payments_from_batch()
        return super().unlink()
