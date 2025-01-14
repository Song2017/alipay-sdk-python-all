#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemCreateExtInfo(object):

    def __init__(self):
        self._action_link = None
        self._shop_id = None

    @property
    def action_link(self):
        return self._action_link

    @action_link.setter
    def action_link(self, value):
        self._action_link = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_link:
            if hasattr(self.action_link, 'to_alipay_dict'):
                params['action_link'] = self.action_link.to_alipay_dict()
            else:
                params['action_link'] = self.action_link
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemCreateExtInfo()
        if 'action_link' in d:
            o.action_link = d['action_link']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


