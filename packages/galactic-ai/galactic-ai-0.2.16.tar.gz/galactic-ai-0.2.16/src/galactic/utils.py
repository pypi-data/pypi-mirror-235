import logging
import requests
import pandas as pd
from dataclasses import dataclass

logger = logging.getLogger("galactic")


@dataclass
class MessageConfig:
    """
    This is the MessageConfig class. It contains the configuration for how a chat message is laid out.
    """

    role_field: str
    content_field: str
    user_role: str
    assistant_role: str
    system_role: str


OPENAI_MESSAGE_CONFIG = MessageConfig(
    role_field="role",
    content_field="content",
    user_role="user",
    assistant_role="assistant",
    system_role="system",
)

SHAREGPT_MESSAGE_CONFIG = MessageConfig(
    role_field="from",
    content_field="value",
    user_role="human",
    assistant_role="gpt",
    system_role="system",
)


def byte_len(x: str):
    return len(x.encode("utf-8"))


def handle_redirects(url: str):
    # handle 308 redirects, pandas burps on them
    res = requests.head(url)
    if res.status_code == 308:
        url = res.headers["Location"]
    elif res.status_code != 200:
        raise ValueError(
            f"Could not read dataset from {url}. Status code: {res.status_code}."
        )
    return url


def read_csv(path: str):
    # if it's remote, follow the redirect first
    if path.startswith("http"):
        path = handle_redirects(path)
    # try to read it
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        logger.warning(
            "Unable to parse CSV file. Falling back to latin-1 encoding."
        )
        df = pd.read_csv(path, encoding="latin-1")
        return df


def read_jsonl(path: str):
    # if it's remote, follow the redirect first
    if path.startswith("http"):
        path = handle_redirects(path)
    # try to read it
    df = pd.read_json(path, lines=True, orient="records")
    return df
