import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)


@openupgrade.migrate()
def migrate(env, version):
    cr = env.cr

    _logger.info("START add tax_state to account_move_line")
    openupgrade.add_columns(env, [
        ("account_move_line", "tax_state", "selection"),
    ])
    _logger.info("END add tax_state to account_move_line")