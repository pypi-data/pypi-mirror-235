from odoo import api, fields, models, tools, SUPERUSER_ID
from odoo.tools.translate import _


class CrmDmsStageTeamRules(models.Model):
    _name = "crm.dms.stage.team.rules"
    _description = "CRM Rules Configuration Table for Document Stage Teams"

    crm_stage_id = fields.Many2one("crm.stage", string="CRM Stage")
    crm_team_id = fields.Many2one("crm.team", string="CRM Team")
    dms_category_id = fields.Many2one("dms.category", string="Document Category")
    is_valid = fields.Boolean("Is Valid")
    is_warning = fields.Boolean("Is Warning")
    is_block = fields.Boolean("Is Block")
