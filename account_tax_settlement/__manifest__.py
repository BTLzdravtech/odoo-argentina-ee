{
    'name': 'Tax Settlement',
    'version': "17.0.1.3.0",
    'category': 'Accounting',
    'sequence': 14,
    'summary': '',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'LGPL-3',
    'images': [
    ],
    'depends': [
        # por ahora agregamos esta dep para permitir vincular a reportes
        'account_reports',
    ],
    'data': [
        'wizards/account_tax_settlement_wizard_view.xml',
        'wizards/download_files_wizard.xml',
        'views/account_move_line_view.xml',
        'views/account_move_view.xml',
        'views/account_journal_view.xml',
        'views/account_journal_dashboard_view.xml',
        'views/account_report_view.xml',
        'security/ir.model.access.csv',
        'data/account_report_data.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
