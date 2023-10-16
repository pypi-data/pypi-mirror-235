import requests
from pydantic import BaseModel
from modelhub.common.types import TextGenerationOutput
from typing import Optional, Dict, List, Any
import json


class ModelhubClient(BaseModel):
    user_name: str
    user_password: str
    host: str
    supported_models: List[str] = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.host = self.host.rstrip("/")
        try:
            self.supported_models = self._get_supported_models()
        except:
            raise ValueError(f"Failed to connect to {self.host}")

    def _get_supported_models(self) -> List[str]:
        response = requests.get(
            self.host + "/models",
        )
        return response.json()["models"]

    def get_supported_params(self, model: str) -> List[str]:
        response = requests.get(
            self.host + "/models/" + model,
        )
        return response.json()["params"]

    def chat(
        self, prompt: str, model: str, parameters: Dict[str, Any] = {}
    ) -> TextGenerationOutput:
        response = requests.post(
            self.host + "/chat",
            json={
                "prompt": prompt,
                "model": model,
                "parameters": parameters,
                "auth": {
                    "user_name": self.user_name,
                    "user_password": self.user_password,
                },
            },
        )
        return response.json()

    def stream_chat(
        self, prompt: str, model: str, parameters: Dict[str, Any] = {}
    ) -> Any:
        for token in requests.post(
            self.host + "/chat",
            json={
                "prompt": prompt,
                "model": model,
                "parameters": parameters,
                "auth": {
                    "user_name": self.user_name,
                    "user_password": self.user_password,
                },
                "stream": True,
            },
            stream=True,
        ).iter_lines(delimiter=b"\r\n\r\n"):
            if token:
                yield json.loads(token[5:])

    def get_embeddings(
        self, prompt: str, model: str, parameters: Dict[str, Any] = {}
    ) -> Any:
        response = requests.post(
            self.host + "/embedding",
            json={
                "prompt": prompt,
                "model": model,
                "parameters": parameters,
                "auth": {
                    "user_name": self.user_name,
                    "user_password": self.user_password,
                },
            },
        )
        return response.json()
