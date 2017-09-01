import binascii
import json
import socket
import ssl
import struct


def pack_payload(title, message, data=None, sound='Default', badge=1):
    return {
        'aps': {
            'alert': {'title': title, 'body': message, 'data': data},
            'sound': sound,
            'badge': badge,
            'content-available': 1
        },
    }


def send_apn_push(token, payload, cert_file, in_sandbox):
    the_host = ('gateway.sandbox.push.apple.com', 2195) if in_sandbox else ('gateway.push.apple.com', 2195)

    data = json.dumps(payload).encode()

    device_token = token.replace(' ', '')
    byte_token = binascii.unhexlify(device_token)

    the_format = '!BH32sH%ds' % len(data)
    the_notification = struct.pack(the_format, 0, 32, byte_token, len(data), data)

    ssl_sock = ssl.wrap_socket(
        socket.socket(socket.AF_INET, socket.SOCK_STREAM),
        certfile=cert_file
    )
    ssl_sock.connect(the_host)

    ssl_sock.write(the_notification)

    ssl_sock.close()
