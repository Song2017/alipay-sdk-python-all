#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppContentItem import AppContentItem


class AlipayOpenAppAppcontentItemQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppAppcontentItemQueryResponse, self).__init__()
        self._items = None
        self._total = None

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, AppContentItem):
                    self._items.append(i)
                else:
                    self._items.append(AppContentItem.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppAppcontentItemQueryResponse, self).parse_response_content(response_content)
        if 'items' in response:
            self.items = response['items']
        if 'total' in response:
            self.total = response['total']