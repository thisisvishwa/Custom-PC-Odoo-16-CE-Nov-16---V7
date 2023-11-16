```python
from odoo import http
from odoo.http import request

class SavedPCBuildsController(http.Controller):

    @http.route('/pc_builds/save', type='json', auth='user')
    def save_pc_build(self, **kwargs):
        pc_build_id = kwargs.get('pc_build_id')
        if not pc_build_id:
            return {'error': 'PC build ID is required'}
        pc_build = request.env['pc_builds'].browse(int(pc_build_id))
        if not pc_build.exists():
            return {'error': 'PC build not found'}
        saved_pc_build = request.env['saved_pc_builds'].create({
            'user_id': request.uid,
            'pc_build_id': pc_build.id,
        })
        return {'success': 'PC build saved successfully', 'saved_pc_build_id': saved_pc_build.id}

    @http.route('/pc_builds/retrieve', type='json', auth='user')
    def retrieve_pc_build(self, **kwargs):
        saved_pc_build_id = kwargs.get('saved_pc_build_id')
        if not saved_pc_build_id:
            return {'error': 'Saved PC build ID is required'}
        saved_pc_build = request.env['saved_pc_builds'].browse(int(saved_pc_build_id))
        if not saved_pc_build.exists() or saved_pc_build.user_id.id != request.uid:
            return {'error': 'Saved PC build not found'}
        return {'success': 'PC build retrieved successfully', 'pc_build': saved_pc_build.pc_build_id.read()[0]}

    @http.route('/pc_builds/delete', type='json', auth='user')
    def delete_pc_build(self, **kwargs):
        saved_pc_build_id = kwargs.get('saved_pc_build_id')
        if not saved_pc_build_id:
            return {'error': 'Saved PC build ID is required'}
        saved_pc_build = request.env['saved_pc_builds'].browse(int(saved_pc_build_id))
        if not saved_pc_build.exists() or saved_pc_build.user_id.id != request.uid:
            return {'error': 'Saved PC build not found'}
        saved_pc_build.unlink()
        return {'success': 'PC build deleted successfully'}
```