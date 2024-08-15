# Copyright (C) 2024 Dorin Hongu <dhongu(@)gmail(.)com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Romania - Mesaje SPV",
    "category": "Localization",
    "countries": ["ro"],
    "summary": "Romania - Mesaje SPV",
    "depends": ["l10n_ro_account_anaf_sync", "l10n_ro_edi", "account_edi"],
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "data/ir_cron_data.xml",
        "views/account_invoice.xml",
        "views/message_spv_view.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "l10n_ro_message_spv/static/src/js/message_spv.esm.js",
            "l10n_ro_message_spv/static/src/js/message_spv.xml",
        ],
    },
    "license": "AGPL-3",
    "version": "17.0.1.8.0",
    "author": "Terrabit," "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-romania",
    "installable": True,
    "development_status": "Beta",
    "maintainers": ["dhongu"],
}