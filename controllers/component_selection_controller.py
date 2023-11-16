```python
from odoo import http
from odoo.http import request

class ComponentSelectionController(http.Controller):

    @http.route('/pc_builder/select_components', type='http', auth='user')
    def select_components(self, **kwargs):
        pc_components = request.env['pc.components'].search([])
        return request.render('custom_pc_v8_nov_16.component_selection_template', {'pc_components': pc_components})

    @http.route('/pc_builder/update_build', type='json', auth='user')
    def update_build(self, **kwargs):
        pc_build = request.env['pc.builds'].browse(kwargs.get('build_id'))
        pc_build.write({
            'component_ids': [(6, 0, kwargs.get('component_ids'))]
        })
        return {'status': 'success', 'message': 'Build updated successfully'}

    @http.route('/pc_builder/preview_build', type='http', auth='user')
    def preview_build(self, **kwargs):
        pc_build = request.env['pc.builds'].browse(kwargs.get('build_id'))
        return request.render('custom_pc_v8_nov_16.pc_build_preview_template', {'pc_build': pc_build})
```