#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@author      : JohnnyLeaf
@file        : __init__.py.py
@time        : 2020/12/28
@description : None
"""
from fastapi import APIRouter
from .index import router as index


router = APIRouter()
router.include_router(index, prefix="/index", tags=["主页"])
