#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@author      : JohnnyLeaf
@file        : index.py
@time        : 2020/12/28
@description : None
"""
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.core import get_settings


router = APIRouter()
settings = get_settings()
templates = Jinja2Templates(directory=settings.BASE_DIR + "/templates")


@router.get("/", summary="主页", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
