import requests
import base64
from time import sleep
import asyncio
from PIL import Image
from io import BytesIO
import asyncio
import aiohttp
import time

from colorama import Fore as f
from datetime import datetime as dt

def get_time():
    now = dt.now()
    return f"{now.hour}:{now.minute}:{now.second}.{str(now.microsecond)[:3]}"

def logs(msg):
    print(f"{f.BLUE}kandinsky{f.RESET} - {f.LIGHTYELLOW_EX}logs{f.RESET} {get_time()}: {msg}")

def info(msg):
    print(f"{f.BLUE}kandinsky{f.RESET} {get_time()} - [{f.LIGHTMAGENTA_EX}INFO{f.RESET}]: {msg}")

def success(msg):
    print(f"{f.BLUE}kandinsky{f.RESET} {get_time()} - [{f.LIGHTGREEN_EX}SUCCESS{f.RESET}]: {msg}")

def failed(msg):
    print(f"{f.BLUE}kandinsky{f.RESET} {get_time()} - [{f.LIGHTRED_EX}FAILED{f.RESET}]: {msg}")

def error(msg):
    print(f"{f.BLUE}kandinsky{f.RESET} {get_time()} - [{f.LIGHTRED_EX}ERROR{f.RESET}]: {msg}")

AUTH = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJUeUFOUUV0TkFsZ0pjaWNfcE01ZTBwV3pWbXUyNG1zV0dLa2h1OXZpbzFFIn0.eyJleHAiOjE2OTg1MDU2OTcsImlhdCI6MTY5NzIwOTY5NywiYXV0aF90aW1lIjoxNjk3MjA5Njk2LCJqdGkiOiI5ZmQ3OTlkYS1iNWE4LTRiY2QtYjY4Ny1hZTFkN2QxNGY0OTciLCJpc3MiOiJodHRwczovL2F1dGguZnVzaW9uYnJhaW4uYWkvcmVhbG1zL0ZCIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6IjU5MTg1NjkxLWJhZDAtNDcyNy1hYzhmLTlhMTgxMTAzOWU5ZSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImZ1c2lvbi13ZWIiLCJzZXNzaW9uX3N0YXRlIjoiMjJmZmI1YzgtZDE1NS00NjRiLThkOGItYmE4YmI0NzRiODk4IiwiYWNyIjoiMCIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsImRlZmF1bHQtcm9sZXMtZmIiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJzaWQiOiIyMmZmYjVjOC1kMTU1LTQ2NGItOGQ4Yi1iYThiYjQ3NGI4OTgiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiemVuYWZleUBldWd3LnJ1IiwiZW1haWwiOiJ6ZW5hZmV5QGV1Z3cucnUifQ.CuZfjyrHVUOArreJQacXATTGY2l8MuEKm9djhQArkA9vv_CdOMKsXB_pjV0sGpBVsVJ70HcuEMeV0LwYt4LaLRUpvB_87bifiyyN577V2K4N_eb3sdlEML0fTxGdkakp-l_SCb34nsLBLtTLrwW_Nm8TVo2ivSrAyVOMO7wjpRwAtm5QTGXgStlvxKuELzCHj9hjUBlZ6SUTS945dlxV7MoS0LzxP5Aliwk8qDnhHFEFzQfoa2wqBWSU_jPmg5_AAdcMv7T7uOcPAO8AGbMGlI15tcr0siw4akUXuD74frHGoA2vS9FyfKZ2UYXZMFIzw0NvOuUgWjCYomIUfFUBLQ",


class AsyncKandinsky:
    def __init__(self, auth_token=AUTH):
        info("Initialized Kandinsky")
        self.headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
            "authorization": f"Bearer {auth_token}",
            "content-type": "multipart/form-data; boundary=----WebKitFormBoundarykLPJ6w7kP3NfRN6K",
            "sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "Referer": "https://fusionbrain.ai/",
            "Referrer-Policy": "strict-origin-when-cross-origin"
          }
        self.base = "https://api.fusionbrain.ai/web/api/v1/text2image"

    async def _arequest(self, method, url, data=None):
        async with aiohttp.ClientSession() as s:
            async with s.request(method, url, data=data, headers=self.headers) as r:
                if r.status not in [200, 201]:
                    error(f"Status: {r.status}, detailed: {await r.text()}")
                    raise Exception("Caught error(r.status not in [200, 201])")

                return await r.json(content_type=None)

    async def create(self, prompt, negative="badly drawn", width=768, height=768, style="ANIME"):
        logs(f'"create" request with params: [{prompt}, {negative}, {width}, {height}, {style}]')
        data = "------WebKitFormBoundarykLPJ6w7kP3NfRN6K\r\nContent-Disposition: form-data; name=\"params\"; filename=\"blob\"\r\nContent-Type: application/json\r\n\r\n{{\"type\":\"GENERATE\",\"style\":\"{style}\",\"width\":{width},\"height\":{height},\"negativePromptDecoder\":\"{negative}\",\"generateParams\":{{\"query\":\"{prompt}\"}}}}\r\n------WebKitFormBoundarykLPJ6w7kP3NfRN6K--\r\n".format(style=style, prompt=prompt, width=width, height=height, negative=negative)
        return await self._arequest("post", f"{self.base}/run?model_id=1", data)

    async def check(self, uuid):
        logs(f'"check" request with params: [{uuid}]')
        return await self._arequest("get", f"{self.base}/status/{uuid}")

    async def wait(self, job):
        logs("Awaiting result...")
        result = job

        while result['status'] != "DONE":
            result = await self.check(job['uuid'])
            await asyncio.sleep(0.5)

        return result['images'][0]

    async def load(self, image_data):
        logs("Loading result image...")
        return BytesIO(base64.b64decode(image_data))

class Kandinsky:
    def __init__(self, auth_token=AUTH):
        info("Initialized Kandinsky")
        self.headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
            "authorization": f"Bearer {auth_token}",
            "content-type": "multipart/form-data; boundary=----WebKitFormBoundarykLPJ6w7kP3NfRN6K",
            "sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "Referer": "https://fusionbrain.ai/",
            "Referrer-Policy": "strict-origin-when-cross-origin"
          }
        self.base = "https://api.fusionbrain.ai/web/api/v1/text2image"

    def _request(self, method, url, data=None):
        r = requests.request(method, url, data=data, headers=self.headers)
        if r.status_code not in [200, 201]:
            error(f"Status: {r.status_code}, detailed: {r.text}")
            raise Exception("Caught error(r.status not in [200, 201])")

        return r.json(content_type=None)

    def create(self, prompt, negative="badly drawn", width=768, height=768, style="ANIME"):
        logs(f'"create" request with params: [{prompt}, {negative}, {width}, {height}, {style}]')
        data = "------WebKitFormBoundarykLPJ6w7kP3NfRN6K\r\nContent-Disposition: form-data; name=\"params\"; filename=\"blob\"\r\nContent-Type: application/json\r\n\r\n{{\"type\":\"GENERATE\",\"style\":\"{style}\",\"width\":{width},\"height\":{height},\"negativePromptDecoder\":\"{negative}\",\"generateParams\":{{\"query\":\"{prompt}\"}}}}\r\n------WebKitFormBoundarykLPJ6w7kP3NfRN6K--\r\n".format(style=style, prompt=prompt, width=width, height=height, negative=negative)
        return self._request("post", f"{self.base}/run?model_id=1", data)

    def check(self, uuid):
        logs(f'"check" request with params: [{uuid}]')
        return self._request("get", f"{self.base}/status/{uuid}")

    def wait(self, job):
        logs("Awaiting result...")
        result = job

        while result['status'] != "DONE":
            result = self.check(job['uuid'])
            time.sleep(0.5)

        return result['images'][0]

    def load(self, image_data):
        logs("Loading result image...")
        return BytesIO(base64.b64decode(image_data))
