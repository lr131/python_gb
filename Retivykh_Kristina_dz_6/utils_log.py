import re

REGEXP_IP = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
REGEXP_REQUEST_TYPE = r'\b(?:[A-Z]){3,4}\b'
REGEXP_RESOURCE = r'(?:/\w+)+\b'


def get_log(log_filename):
    """Возвращает список кортежей вида
    (<remote_addr>, <request_type>, <requested_resource>)"""
    with open(log_filename, 'r', encoding='utf-8') as file_logs:
        for line_log in file_logs:
            match_ip = re.search(REGEXP_IP, line_log)
            match_req_type = re.search(REGEXP_REQUEST_TYPE, line_log)
            match_resource = re.search(REGEXP_RESOURCE,
                                       line_log[match_req_type.end() + 1:])
            yield (match_ip[0] if match_ip else None,
                   match_req_type[0] if match_req_type else None,
                   match_resource[0] if match_resource else None)


def get_spamer_info(log_filename):
    """возвращает кортеж вида <адрес спамера>,
    <количество отправленных им запросов>"""
    logs = get_log("nginx_logs.txt")
    data = {}
    for log in logs:
        data.setdefault(log[0], 0)
        data[log[0]] += 1
    return sorted(data.items(), key=lambda item: item[1], reverse=True)[0]