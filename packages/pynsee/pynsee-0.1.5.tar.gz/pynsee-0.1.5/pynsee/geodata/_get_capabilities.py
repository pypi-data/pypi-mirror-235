# -*- coding: utf-8 -*-

import os
import requests
import tempfile
import urllib3
from functools import lru_cache


@lru_cache(maxsize=None)
def _get_capabilities(key, version="1.0.0", service="wmts", tweak=""):

    service_upper = service.upper()

    link = "https://wxs.ign.fr/{}/geoportail/{}{}?SERVICE={}&VERSION={}&REQUEST=GetCapabilities".format(
        key, tweak, service, service_upper, version
    )

    try:
        proxies = {"http": os.environ["http_proxy"], "https": os.environ["https_proxy"]}
    except:
        proxies = {"http": "", "https": ""}
    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    results = requests.get(link, proxies=proxies, verify=False)

    raw_data_file = tempfile.mkdtemp() + "\\" + "raw_data_file"

    with open(raw_data_file, "wb") as f:
        f.write(results.content)
        f.close()

    return raw_data_file
