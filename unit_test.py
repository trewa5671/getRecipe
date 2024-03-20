import pytest
from uuid import uuid4
from time import sleep
from datetime import datetime
from main import root, get_list
import json
import asyncio
from fastapi import Query


def test_root_get():
    res = asyncio.run(root())
    assert 'title' in res.keys()
    assert (type(res['title']) == str)


def test_list_get():
    res = asyncio.run(get_list(q=[1208]))
    res = res[0]
    assert (res['title'] == 'Beer Braised BBQ Pork Butt')
