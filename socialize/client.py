from base import ObjectBase ,CollectionBase
import json

class SmartAlert(object):
    '''
        Smart Alert structure
        {
            u'users': u'[]', 
            u'created': u'2012-06-26T22:24:03',
            u'subscription_type': u'entity_notification',
            u'id': u'1060',
            u'meta': u'{ 
                    "entity_id": "2519382", 
                     "url": ""
                     }',
            u'device_tokens': u'[]',
            u'message': u'test notification ',
            u'resource_uri': u'/management/v1/smart_alert/1060/'
        }
    '''
    def __init__(self, smart_alert={}):
        self.users                      =smart_alert.get('users',[])
        self.created                    =smart_alert.get('created','') 
        self.subscription_type          =smart_alert.get('subscription_type','')
        self.id                         =int(smart_alert.get('id',0))
        self.meta                       =smart_alert.get('meta','')
        self.device_tokens              =smart_alert.get('device_tokens',[])
        self.message                    =smart_alert.get('message','')
        
    def __repr__(self):
        return json.dumps( self.__dict__, indent=3 )


class Management(ObjectBase,CollectionBase):
    '''
        Interface for management API
    '''
    def __init__(self, consumer_key, consumer_secret, host='http://api.getsocialize.com', ):
        self.consumer_key= consumer_key
        self.consumer_secret = consumer_secret
        self.host = host

    def get_smart_alerts(self, params={}):
        meta , resp= self._find(endpoint= 'smart_alert',
                params = params
                )
        return [ SmartAlert(i) for i in resp]

    def get_smart_alert_by_id(self, id, params={}):
        resp= self._findOne(endpoint= 'smart_alert',
                item_id = id,
                params = params
                )
        return SmartAlert( resp )
        

    def post_smart_alert(self, 
                message,
                application_id,
                user_id_list = None,
                url = None,
                device_list = None,
                entity_id = None,
                subscription = None,
                broadcast_user_set = None):
        '''
            set notifications enabled to True or False
            return True when success else raise exception
            users must be a list of integer
            subscription type [optional] by default is "developer_notification"
        '''

        payload = { 'message': message,
                    'application_id':application_id
                }
        
        if broadcast_user_set:
            payload.update({"broadcast_user_set" : broadcast_user_set})
             
        if type(user_id_list)==list:
            user_id_list = [ int(u) for u in user_id_list ]
            payload.update({ "users": user_id_list })
        if url:
            payload.update({ "url": url })
        if device_list:
            payload.update({ "devices": device_list })
        if entity_id:
            payload.update({ "entity_id": entity_id })
        if subscription:
            payload.update({ "subscription": subscription})
        if url:
            payload.update({"url":url})
        
        resp= self._post(endpoint= 'smart_alert',
                payload=payload)
        return SmartAlert( resp )

if __name__ == '__main__':
    m  = Management( 'a020d83a-e88c-49ed-afa5-54ab9567308f' ,'489409c1-d4f1-41d8-a6a8-337b5c53edf6' )
    #resp = m.send_smart_alert( 'hello test sending notification from management sdk yet', 421945 ) 
    resp = m.get_smart_alerts()
    #resp = m.get_smart_alert_by_id(1060)
    #print resp

    print resp




