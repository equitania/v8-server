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
import re
import openerp.tools as tools
import os.path
import logging
_logger = logging.getLogger(__name__)
from openerp import SUPERUSER_ID





module_name = 'eq_myodoo_backend_theme'


class eq_theme_customization(models.TransientModel):
    _name = 'eq.theme.customization'
    _inherit = 'res.config.settings'

    def _create_odoo_log(self, cr, name, func, path, message):
        """
            Erstellt Logeintrag direkt im Odoo
            @cr: Kursor
            @message: Logeintrag mit allen Daten
        """

        logger_vals = {
            'name': name,
            'func': func,
            'path': path,
            'line': '/',
            'type': 'server',
            'level': 'INFO',
            'message': message
        }
        logging_pool = self.pool.get('ir.logging')
        logging_pool.create(cr, SUPERUSER_ID, logger_vals)

    eq_fontsize = fields.Char(string="Fontsize")
    eq_primary_color = fields.Char(string="Primary color")
    eq_highlightcolor = fields.Char(string="Highlight color")
    eq_buttoncolors = fields.Char(string="Button color")
    eq_buttonhighlights = fields.Char(string="Button highlight color")
    eq_textlinkcolor = fields.Char(string="Textlink")
    eq_mainmenu_padding = fields.Char(string="Padding")
    eq_mainmenu_fontsize = fields.Char(string="Fontsize")
    eq_submenu_padding = fields.Char(string="Padding")
    eq_submenu_fontsize = fields.Char(string="Fontsize")

    eq_theme_ribbon_name = fields.Char(string="Ribbon name")
    eq_theme_ribbon_color = fields.Char(string="Ribbon color")
    eq_theme_ribbon_background_color = fields.Char(string="Ribbon background color")

    eq_backend_theme_log = fields.Boolean('Backend Theme Log', default = False)



    @api.multi
    def get_default_eq_theme_data(self):
        """
        Load the values from ir.config_parameter
        @return:
        """
        config_parameters = self.env["ir.config_parameter"]
        eq_fontsize = config_parameters.get_param("eq_theme_fontsize")
        primary_color = config_parameters.get_param("eq_theme_primarycolor")
        eq_highlightcolor = config_parameters.get_param("eq_theme_highlightcolor")
        eq_buttoncolors = config_parameters.get_param("eq_theme_buttoncolors")
        eq_buttonhighlights = config_parameters.get_param("eq_theme_buttonhighlights")
        eq_textlinkcolor = config_parameters.get_param("eq_theme_textlinkcolor")
        eq_mainmenu_padding = config_parameters.get_param("eq_theme_mainmenu_padding")
        eq_mainmenu_fontsize = config_parameters.get_param("eq_theme_mainmenu_fontsize")
        eq_submenu_padding = config_parameters.get_param("eq_theme_submenu_padding")
        eq_submenu_fontsize = config_parameters.get_param("eq_theme_submenu_fontsize")

        eq_theme_ribbon_name = config_parameters.get_param("theme.ribbon.name")
        eq_theme_ribbon_color = config_parameters.get_param("theme.ribbon.color")
        eq_theme_ribbon_background_color = config_parameters.get_param("theme.ribbon.background.color")

        eq_backend_theme_log = config_parameters.get_param("backend.theme.log")


        return {
            'eq_fontsize': eq_fontsize,
            'eq_primary_color': primary_color,
            'eq_highlightcolor': eq_highlightcolor,
            'eq_buttoncolors': eq_buttoncolors,
            'eq_buttonhighlights': eq_buttonhighlights,
            'eq_textlinkcolor': eq_textlinkcolor,
            'eq_mainmenu_padding': eq_mainmenu_padding,
            'eq_mainmenu_fontsize': eq_mainmenu_fontsize,
            'eq_submenu_padding': eq_submenu_padding,
            'eq_submenu_fontsize': eq_submenu_fontsize,
            'eq_theme_ribbon_name': eq_theme_ribbon_name,
            'eq_theme_ribbon_color': eq_theme_ribbon_color,
            'eq_theme_ribbon_background_color': eq_theme_ribbon_background_color,
            'eq_backend_theme_log': eq_backend_theme_log,
        }


    @api.multi
    def set_eq_theme_data(self):
        """
        Write params back to ir.config_parameter and update the css for the theme
        @return:
        """
        config_parameters = self.env["ir.config_parameter"]
        for record in self:
            config_parameters.set_param("eq_theme_fontsize", record.eq_fontsize or '', )
            config_parameters.set_param("eq_theme_primarycolor", record.eq_primary_color or '', )
            config_parameters.set_param("eq_theme_highlightcolor", record.eq_highlightcolor or '', )
            config_parameters.set_param("eq_theme_buttoncolors", record.eq_buttoncolors or '', )
            config_parameters.set_param("eq_theme_buttonhighlights", record.eq_buttonhighlights or '', )
            config_parameters.set_param("eq_theme_textlinkcolor", record.eq_textlinkcolor or '', )
            config_parameters.set_param("eq_theme_mainmenu_padding", record.eq_mainmenu_padding or '', )
            config_parameters.set_param("eq_theme_mainmenu_fontsize", record.eq_mainmenu_fontsize or '', )
            config_parameters.set_param("eq_theme_submenu_padding", record.eq_submenu_padding or '', )
            config_parameters.set_param("eq_theme_submenu_fontsize", record.eq_submenu_fontsize or '', )
            config_parameters.set_param("theme.ribbon.name", record.eq_theme_ribbon_name or '', )
            config_parameters.set_param("theme.ribbon.color", record.eq_theme_ribbon_color or '', )
            config_parameters.set_param("theme.ribbon.background.color", record.eq_theme_ribbon_background_color or '', )

            config_parameters.set_param("backend.theme.log", record.eq_backend_theme_log or '', )


        self.update_data()

    def _get_root_path(self):
        """
        Find the directory for the module
        @return:
        """
        config_parameters = self.env["ir.config_parameter"]
        eq_backend_theme_log = config_parameters.get_param("backend.theme.log")
        eq_backend_theme_log = bool(eq_backend_theme_log)


        config_paths = tools.config['addons_path'].split(',')
        found_addons_path = ''
        for mod_path in config_paths:
            # find directory path/eq_myodoo_backend_theme
            mod_dir = os.path.join(mod_path, module_name)
            if os.path.isdir(mod_dir):
                found_addons_path = mod_path
                print 'found directory for module:',found_addons_path
                break

            # if mod_path.ends_with('myodoo-server/addons'):
            #     found_addons_path = mod_path

        if not found_addons_path:
            _logger.exception("Directory for module eq_myodoo_backendtheme could not be found")
            if eq_backend_theme_log == True:
                message = "Directory for module eq_myodoo_backendtheme could not be found"
                self._create_odoo_log("Directory for module eq_myodoo_backendtheme could not be found", "ERROR","eq_myodoo_backend_theme", message)
            else: pass
        return found_addons_path


    @api.model
    def update_data(self):
        """
        Replace the placeholders of the main-manual-theme-template.css with the actual parameter values
        @return:
        """

        config_parameters = self.env["ir.config_parameter"]
        eq_backend_theme_log = config_parameters.get_param("backend.theme.log")
        eq_backend_theme_log = bool(eq_backend_theme_log)


        base_path = self._get_root_path()
        if not base_path:
            base_path = 'addons/eq_myodoo_backend_theme/static/src/css/'
        else:
            base_path = os.path.join(base_path, 'eq_myodoo_backend_theme/static/src/css/')

        # print 'base_path:', base_path

        template_file = base_path + "main-manual-theme-template.css"
        target_css_file = base_path + "main-manual-theme.css"

        _logger.info("Path to Templatefile: " + target_css_file)

        if not os.path.isfile(template_file):
            _logger.exception("Theme cannot be written to file: Templatefile not found: " + template_file)
            if eq_backend_theme_log == True:
                message = "Theme cannot be written to file: Templatefile not found: " + template_file
                self._create_odoo_log("Theme cannot be written to file: Templatefile not found", "ERROR","eq_myodoo_backend_theme", message)
            else:
                pass
            return

        if not os.path.isfile(target_css_file):
            _logger.exception("Theme cannot be written to file: Targetfile for template not found: " + target_css_file)
            if eq_backend_theme_log == True:
                message = "Theme cannot be written to file: Targetfile for template not found: " + target_css_file
                self._create_odoo_log("Theme cannot be written to file: Targetfile for template not found", "ERROR","eq_myodoo_backend_theme", message)
            else:
                pass
            return

        config_params_obj = self.env['ir.config_parameter']

        theme_settings = {}
        file_content = None
        with open(template_file, "r") as myfile:
            file_content = myfile.readlines()

        if not file_content:
            # eq_log.log("Theme cannot be saved: no content in Templatefile found")
            _logger.exception("Theme cannot be saved: no content in Templatefile '" + template_file + "' found")
            if eq_backend_theme_log == True:
                message = "Theme cannot be saved: no content in Templatefile '" + template_file + "' found"
                self._create_odoo_log("Theme cannot be saved: no content in Templatefile", "ERROR", "eq_myodoo_backend_theme",message)
            else:
                pass
            return

        replace_pattern = re.compile(re.escape('start'), re.I)

        cur_param = ''
        is_in_param = False
        for line in file_content:
            line_lower = line.lower()

            if line.startswith('/*') and 'end ' in line_lower:
                is_in_param = False

            if is_in_param and cur_param and cur_param in theme_settings:
                if line.startswith('/*'):
                    continue
                theme_settings[cur_param].append(line)
            else:
                # Start tag found?
                # Example: /* primarycolor  START * /
                if line.startswith('/*') and 'start ' in line_lower:
                    cur_param = line.replace('/*', '')
                    cur_param = cur_param.replace('*/', '')
                    cur_param = re.sub(replace_pattern, '', cur_param).strip()

                    theme_settings[cur_param] = []
                    is_in_param = True

        new_theme_css = []
        for key, val in theme_settings.items():
            param_search = config_params_obj.search([('key', '=', key)])
            if param_search and param_search.value:
                param_settings = ''.join(val)
                replace_value = param_search.value
                param_settings = param_settings.replace(key, replace_value)
                new_theme_css.append(param_settings)

        try:
            with open(target_css_file, "w") as myfile:
                myfile.write('\n'.join(new_theme_css))
                if eq_backend_theme_log == True:
                    message = 'Templatepfad: '+ template_file + '\n' + 'Zielpfad: ' + target_css_file + '\n' + 'Neuer Inhalt: ' + '\n' + str(new_theme_css)
                    self._create_odoo_log("Update", "Update","eq_myodoo_backend_theme", message)
                else:
                    pass

        except Exception as ex:
            # eq_log.log("Error while writing to templatefile: " + ex.message)
            _logger.exception("Error while writing to target templatefile " + target_css_file + '; ' + ex.message)
            message = target_css_file + '; ' + ex.message
            self._create_odoo_log("Error while writing to target templatefile", "ERROR", "eq_myodoo_backend_theme", message)
