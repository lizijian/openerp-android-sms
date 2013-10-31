# -*- encoding: utf-8 -*-

{
    'name': 'OpenERP 短信模块',
    'version': '0.2',
    'category': 'Generic Modules/Messages',
    'description': u"""
        Android 短信模块
    """,
    'author': 'mrshelly',
    # 'website': 'https://github.com/mrshelly/openerp-android',
    'depends': ['base'],
    'init_xml': [
    ],
    'data': [
        'security/android_security.xml',
        'security/ir.model.access.csv',
        'wizard/send_sms.xml',
        'view/android_device_view.xml',
        'view/message_view.xml',
    ],
    'demo_xml': [],
    'installable': True,
    'active': False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
