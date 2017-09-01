import binascii
import json
import socket
import ssl
import struct

from pyfcm import FCMNotification

from easy_push.apn import pack_payload, send_apn_push


def push_to_apn(device_token: str, cert_file: str, title: str = None, message: str = None, data: dict = None, sound: str = 'Default', badge: int = 1, in_sandbox: bool = False):
    host = ('gateway.sandbox.push.apple.com', 2195) if in_sandbox else ('gateway.push.apple.com', 2195)

    payload = {
        'aps': {
            'alert': {'title': title, 'body': message, 'data': data},
            'sound': sound,
            'badge': badge,
            'content-available': 1 if data else 0
        },
    }

    data = json.dumps(payload).encode()

    device_token = device_token.replace(' ', '')
    byte_token = binascii.unhexlify(device_token)

    the_format = '!BH32sH%ds' % len(data)
    the_notification = struct.pack(the_format, 0, 32, byte_token, len(data), data)

    ssl_sock = ssl.wrap_socket(
        socket.socket(socket.AF_INET, socket.SOCK_STREAM),
        certfile=cert_file
    )
    ssl_sock.connect(host)

    ssl_sock.write(the_notification)

    ssl_sock.close()


def push_to_fcm(device_token: str, fcm_key: str, title: str = None, message: str = None, data: dict = None, sound: str = None, badge: int = None):
    fcm_push_service = FCMNotification(api_key=fcm_key)

    fcm_push_service.notify_single_device(
        registration_id=device_token,
        message_title=title,
        message_body=message,
        data_message=data,
        sound=sound,
        badge=badge
    )
