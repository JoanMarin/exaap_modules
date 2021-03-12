# -*- coding: utf-8 -*-
# Copyright 2018 EXA Auto Parts S.A.S Joan Marín <Github@JoanMarin>
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name':
    "CRM Lead Activity",
    'version':
    "11.0.1.0.0",
    "website":
    "https://github.com/exaap/exaap_modules",
    "author":
    "EXA Auto Parts Github@exaap, "
    "Joan Marín Github@JoanMarin, "
    "Alejandro Olano Github@alejo-code",
    'category':
    "CRM",
    'summary':
    "View crm_activity_log",
    'license':
    'LGPL-3',
    'data': [
        'report/crm_activity_report_views.xml',
        'views/crm_lead_views.xml',
        'wizard/crm_activity_log_views.xml',
    ],
    'demo': [],
    'depends': ['crm'],
    'images': [],
    'installable':
    True,
}