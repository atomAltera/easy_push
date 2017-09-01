from pyfcm import FCMNotification

from easy_push.apn import pack_payload, send_apn_push


def push_to_apn(device_token, cert_file, title=None, message=None, data=None, sound='Default', badge=1, in_sandbox=False):
    payload = pack_payload(title, message, data, sound, badge)
    send_apn_push(device_token, payload, cert_file, in_sandbox)


def push_to_fcm(device_token, gcm_key, title=None, message=None, data=None, sound=None, badge=None):
    fcm_push_service = FCMNotification(api_key=gcm_key)

    fcm_push_service.notify_single_device(
        registration_id=device_token,
        message_title=title,
        message_body=message,
        data_message=data,
        sound=sound,
        badge=badge
    )
