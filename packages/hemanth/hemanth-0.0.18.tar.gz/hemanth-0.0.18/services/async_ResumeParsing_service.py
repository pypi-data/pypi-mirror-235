import json
from typing import *

import httpx

from ..api_config import APIConfig, HTTPException
from ..models import *


async def parseByStream(
    Authorization: str, data: ResumeRequest, api_config_override: Optional[APIConfig] = None
) -> ResumeResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/parse"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
        "Authorization": Authorization,
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request("post", httpx.URL(path), headers=headers, params=query_params, json=data.dict())

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return ResumeResponse(**response.json()) if response.json() is not None else ResumeResponse()


async def parseByFile(
    Authorization: str, data: ResumeFileRequest, api_config_override: Optional[APIConfig] = None
) -> ResumeResponse:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/v1/parse/file"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
        "Authorization": Authorization,
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    async with httpx.AsyncClient(base_url=base_path, verify=api_config.verify) as client:
        response = await client.request(
            "post",
            httpx.URL(path),
            headers=headers,
            params=query_params,
        )

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return ResumeResponse(**response.json()) if response.json() is not None else ResumeResponse()
