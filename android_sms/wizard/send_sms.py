# -*- encoding: utf-8 -*-
from  osv import osv, fields
from tools.translate import _


class send_sms(osv.osv_memory):
    '''
    Send Sms
    '''
    _name = 'android.send_sms'
    _description = 'Send Sms'
    _columns = {
        'target_no': fields.char(u'Target No', size=20, required=True),
        'sms_simcard_id': fields.many2one('sim.card', 'SMS SimCard'),
        'msg_body': fields.text(u'Message Body', size=20, required=True),
    }

    def send_sms(self, cr, uid, ids, context=None):
        sim_card_obj = self.pool.get('sim.card')
        objs = self.browse(cr, uid, ids, context)
        for obj in objs:
            octx = context
            octx['sms_no'] = obj.target_no
            octx['sms_msg'] = obj.msg_body
            res = sim_card_obj.send_sms(cr, uid,obj.sms_simcard_id and [obj.sms_simcard_id.id] or [], octx)
            if not res:
                raise osv.except_osv('Send Error:', 'Send Error.')


send_sms()

