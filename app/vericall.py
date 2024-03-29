from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import requests


class VeriCall:
    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        retries: int = 3,
        timeout: float = 1.00,
    ):
        self.host = host
        self.session = requests.Session()
        self.session.headers.update(
            {"Content-Type": "application/json", "Accept": "application/json"}
        )
        self.session.auth = (username, password)
        self.timeout = timeout
        self.url = f"https://{self.host}/"
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=0.1,
            status_forcelist=(429, 500, 502, 504),
            method_whitelist=("POST",),
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("https://", adapter)

    def request(self, payload: dict):
        resp = self.session.post(self.url, json=payload, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()


def score(vericall: VeriCall, payload: dict):
    resp = vericall.request(payload=payload)
    return resp
