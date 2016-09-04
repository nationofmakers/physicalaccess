# -*- coding: utf-8 -*-
from openerp import http

class DefaultDataDemo(http.Controller):
    @http.route('/physical_access_control/physical_access_control/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/physical_access_control/physical_access_control/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('physical_access_control.listing', {
            'root': '/physical_access_control/physical_access_control',
            'objects': http.request.env['physical_access_control.physical_access_control'].search([]),
        })

    @http.route('/physical_access_control/physical_access_control/objects/<model("physical_access_control.physical_access_control"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('physical_access_control.object', {
            'object': obj
        })