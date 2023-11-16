```python
from odoo import http
from odoo.http import request

class PCBuildPreviewController(http.Controller):

    @http.route('/pc_build_preview/', auth='user', website=True)
    def pc_build_preview(self, **kwargs):
        user = request.env.user
        pc_build = request.env['pc_builds'].sudo().search([('user_id', '=', user.id)], order='create_date desc', limit=1)
        if not pc_build:
            return request.redirect('/pc_builds/')
        return request.render('custom_pc_v8_nov_16.pc_build_preview', {
            'pc_build': pc_build,
        })

    @http.route('/pc_build_preview/update/', auth='user', type='json')
    def update_pc_build(self, **kwargs):
        user = request.env.user
        pc_build = request.env['pc_builds'].sudo().search([('user_id', '=', user.id)], order='create_date desc', limit=1)
        if not pc_build:
            return {'error': 'No PC build found.'}
        pc_build.write(kwargs)
        return {'success': 'PC build updated successfully.'}

    @http.route('/pc_build_preview/preview/', auth='user', type='json')
    def preview_pc_build(self, **kwargs):
        user = request.env.user
        pc_build = request.env['pc_builds'].sudo().search([('user_id', '=', user.id)], order='create_date desc', limit=1)
        if not pc_build:
            return {'error': 'No PC build found.'}
        return {'pc_build': pc_build.read()[0]}
```