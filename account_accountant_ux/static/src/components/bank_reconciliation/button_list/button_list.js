/** @odoo-module **/

import { BankRecButtonList } from "@account_accountant/components/bank_reconciliation/button_list/button_list";
import { BankRecSelectCreateDialog } from "@account_accountant/components/bank_reconciliation/search_dialog/search_dialog";
import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";

patch(BankRecButtonList.prototype, {
    setup() {
        super.setup();
        const addDialog = this.addDialog;
        this.addDialog = (dialog, props, options) => {
            if (dialog === BankRecSelectCreateDialog) {
                props = {
                    ...props,
                    context: { ...props.context, search_default_same_amount: 1 },
                };
            }
            return addDialog(dialog, props, options);
        };
    },

    get buttonsToDisplay() {
        const result = super.buttonsToDisplay;
        const buttons = this.buttons || {};

        // Add reconcile button when partner and account are shown
        if (buttons?.partner && buttons?.account && buttons?.reconcile) {
            result.push({ ...buttons.reconcile, primary: true });
        }

        return result;
    },
});
