import json
import hashlib
import time
import socket
import requests
import urllib3
import os
import random
import datetime
import base64
import ping3
import uuid

import mecord.pb.uauth_common_pb2 as uauth_common_pb2
import mecord.pb.uauth_ext_pb2 as uauth_ext_pb2
import mecord.pb.common_ext_pb2 as common_ext_pb2
import mecord.pb.aigc_ext_pb2 as aigc_ext_pb2
import mecord.pb.rpcinput_pb2 as rpcinput_pb2
from mecord import store 
from mecord import utils 
from mecord import taskUtils 
from mecord import constant 

# def resolve_dns_with_ali(domain):
#     for url in ["https://dns.alidns.com/resolve", "https://alidns_ip/resolve", "http://dns.alidns.com/resolve", "http://alidns_ip/resolve"]:
#         params = {
#             "name": domain,
#             "type": 1,
#             "short": 1,
#             # "uid": "35396342",
#         }
#         response = requests.get(url, params=params)
#         if response.status_code == 200:
#             return response.json()
        
# def resolve_dns_with_tencent(domain):
#     for url in ["http://119.29.29.98/d?"]:
#         params_str = f"dn={domain}"
#         response = requests.get(url, params=params)
#         if response.status_code == 200:
#             return response.json()

# domain = "api.mecordai.com"
# addresses = resolve_dns(domain)
# print(f"The resolved IP addresses for {domain} are: {addresses}")
