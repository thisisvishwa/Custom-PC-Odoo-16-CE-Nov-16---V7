```python
from odoo import models, fields

class SavedPCBuilds(models.Model):
    _name = 'saved.pc.builds'
    _description = 'Saved PC Builds'

    user_id = fields.Many2one('res.users', string='User', required=True)
    build_id = fields.Many2one('pc.builds', string='PC Build', required=True)
    saved_timestamp = fields.Datetime(string='Saved Timestamp', default=fields.Datetime.now)
```