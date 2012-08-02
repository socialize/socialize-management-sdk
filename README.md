Socialize Management Python SDK
====================

How to use
----------

    python setup.py build
    python setup.py install

We currently doesn't have automatic process for requesting a management consumer key.

Feel free to ask for it at http://support.getsocialize.com/

This SDK is a work in progress. Below are the implemented endpoints.
 

Management API:

    /v1/smart_alert
        - GET list of developer smart_alert
        - POST sent new smart alert

    /v1/smart_alert/<id>
        - GET smart_alert by id
    
Example:
    
    from socialize_management_sdk import client
    m = client.Management('<management-consumer-key>', 'management-consumer-secret')

    
    # to send smart alert 
    resp = m.post_smart_alert( 'hello test sending notification from management sdk yet', <application-id> ) 
    # response object is a dictionary of current status
    print resp
    {'android': {
        'under_quota': True, 
        'will_cause_quota_overflow': False
        },
    'ios': {
        'under_quota': True,
        'will_cause_quota_overflow': False},
        'smart_alert_id': 1597
        }

    # to get all history smart alert objects
    resp = m.get_smart_alerts()
    # return an object list of of smart alert

        users             
        created           
        subscription_type 
        id                
        meta              
        device_tokens     
        message           

    # to get smart alert by id 
    resp = m.get_smart_alert_by_id(<smart_alert_id>)
    # return single objects of smart alert                    
