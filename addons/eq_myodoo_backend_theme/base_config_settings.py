# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo Addon, Open Source Management Solution
#    Copyright (C) 2014-now Equitania Software GmbH(<http://www.equitania.de>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api, _

class eq_base_config_settings(models.Model):
    _inherit = 'base.config.settings'


    @api.multi
    def action_open_theme_customization(self):
        """
        Opens the form for changing the theme
        @return:
        """

        # res = self._context.copy()
        config_form = self.env.ref('eq_myodoo_backend_theme.eq_theme_customization_form')

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'eq.theme.customization',
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': config_form.id,
            'target': 'new',
            'flags': {'initial_mode': 'edit'},
            'context': "{}",
        }