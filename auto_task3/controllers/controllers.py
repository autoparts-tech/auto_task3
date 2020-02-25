# -*- coding: utf-8 -*-
from odoo import http

# class AutoTask3(http.Controller):
#     @http.route('/auto_task3/auto_task3/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/auto_task3/auto_task3/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('auto_task3.listing', {
#             'root': '/auto_task3/auto_task3',
#             'objects': http.request.env['auto_task3.auto_task3'].search([]),
#         })

#     @http.route('/auto_task3/auto_task3/objects/<model("auto_task3.auto_task3"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('auto_task3.object', {
#             'object': obj
#         })