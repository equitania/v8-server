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

import cStringIO
import os
import base64
#from PIL import Image
import PIL

import datetime
from itertools import islice
import json
import xml.etree.ElementTree as ET

import logging
import re

import werkzeug.utils
import urllib2
import werkzeug.wrappers
from PIL import Image

import openerp
from openerp.addons.web.controllers.main import WebClient
from openerp.addons.web import http
from openerp.http import request, STATIC_CACHE
from openerp.tools import image_save_for_web, eq_image_save_for_web, image_resize_image, eq_image_resize_image

logger = logging.getLogger(__name__)

# Completely arbitrary limits
MAX_IMAGE_WIDTH, MAX_IMAGE_HEIGHT = IMAGE_LIMITS = (1024, 768)
LOC_PER_SITEMAP = 45000
SITEMAP_CACHE_TIME = datetime.timedelta(hours=12)


import re
import json
import openerp
from openerp import http
from openerp.http import request
import logging
from openerp.addons.website.controllers.main import Website as controller

from PIL import Image

_logger = logging.getLogger(__name__)


#class WebsiteFile(openerp.addons.website.controllers.main.Website):
class WebsiteFile(controller):
            
    @http.route('/website/attach', type='http', auth='user', methods=['POST'], website=True)
    def attach(self, func, upload=None, url=None, disable_optimization=None, optimization_600=None, optimization_1024=None, optimization_600_to_jpeg=None, optimization_1024_to_jpeg=None):
        Attachments = request.registry['ir.attachment']

        website_url = message = None
        if not upload:
            website_url = url
            name = url.split("/").pop()
            attachment_id = Attachments.create(request.cr, request.uid, {
                'name': name,
                'type': 'url',
                'url': url,
                'res_model': 'ir.ui.view',
            }, request.context)
        else:
            try:
                image_data = upload.read()
                image = Image.open(cStringIO.StringIO(image_data))
                w, h = image.size
                if w*h > 42e6: # Nokia Lumia 1020 photo resolution
                    raise ValueError(
                        u"Image size excessive, uploaded images must be smaller "
                        u"than 42 million pixel")
                
                if not disable_optimization and image.format in ('PNG', 'JPEG'):        # optimization is NOT disabled               
                    #print "# DEFAULT: optimize image #"                                        
                    image_data = eq_image_save_for_web(image, None, None, True)
                    # finally save our attachment
                    attachment_id = Attachments.create(request.cr, request.uid, {
                        'name': upload.filename,
                        'datas': image_data.encode('base64'),
                        'datas_fname': upload.filename,
                        'res_model': 'ir.ui.view',
                    }, request.context)                
                elif disable_optimization == "1":
                    #print "# DEFAULT - disabled optimization #"
                    attachment_id = Attachments.create(request.cr, request.uid, {
                        'name': upload.filename,
                        'datas': image_data.encode('base64'),
                        'datas_fname': upload.filename,
                        'res_model': 'ir.ui.view',
                    }, request.context)
                else:
                    #print "* disable_optimization: ", disable_optimization
                    convert_to_jpeg = False
                    if "_to_jpeg" in disable_optimization:
                        convert_to_jpeg = True         
                        disable_optimization = disable_optimization.replace("_to_jpeg", "")                       
                    
                    #print "EQUITANIA - optimization"
                    image_data = eq_image_save_for_web(image, None, None, convert_to_jpeg)
                    encoded_image = base64.b64encode(image_data)                                                # encode image to base64
                    if disable_optimization == "600":                                            
                        image_data = eq_image_resize_image(encoded_image, (600, 600), "base64", None, False)       # resize image                        
                    elif disable_optimization == "1024":
                        image_data = eq_image_resize_image(encoded_image, (1024, 1024), "base64", None, False)       # resize image                    
                
                    
                    # finally save our attachment
                    attachment_id = Attachments.create(request.cr, request.uid, {
                        'name': upload.filename,
                        'datas': image_data,
                        'datas_fname': upload.filename,
                        'res_model': 'ir.ui.view',
                    }, request.context)

                
                [attachment] = Attachments.read(request.cr, request.uid, [attachment_id], ['website_url'], context=request.context)
                website_url = attachment['website_url']
            except Exception, e:
                _logger.exception("Failed to upload image to attachment")
                message = unicode(e)

        return """<script type='text/javascript'>
            window.parent['%s'](%s, %s);
        </script>""" % (func, json.dumps(website_url), json.dumps(message))
        
        
        
    def _find_website_filename(self, filename):
        name = ext = ''
        res = re.match('(.*)(\.[^.]+)', filename)
        if res:
            name = res.group(1)
            ext = res.group(2)
        else:
            name = filename

        pattern = '%s-[0-9]+%s' % (name, ext)

        request.cr.execute("""
        SELECT count(*)
        FROM ir_attachment
        WHERE datas_fname SIMILAR TO %s
        """, (pattern,))

        count = request.cr.fetchone()[0]

        return '%s-%s%s' % (name, count+1, ext)

    @http.route('/website/attach_file', type='http', auth='user', methods=['POST'], website=True)
    def attach_file(self, func, upload=None, overwrite=False):
        
        #print "**** attach_file: ", attach_file
        
        filename = website_file_url = message = None
        try:
            file_data = upload.read().encode('base64')
            filename = upload.filename or 'undefined'
            attachment = request.env['ir.attachment'].search([
                ('website_file', '=', True),
                ('datas_fname', '=', filename)])
            if attachment:
                attachment = attachment[0]
                if overwrite:
                    #print 'overwrite attachment',
                    attachment.datas = file_data
                else:
                    filename = self._find_website_filename(filename)
                    #print 'new filename', filename
                    attachment = None

            if not attachment:
                attachment = request.env['ir.attachment'].create({
                    'name': filename,
                    'datas': file_data,
                    'datas_fname': filename,
                    'website_file': True,
                })
                #print 'create attachment', attachment.id, filename

            website_file_url = attachment.website_file_url
        except Exception, e:
            _logger.exception("Failed to upload file to attachment")
            message = unicode(e)

        return """<script type='text/javascript'>
            window.parent['%s'](%s, %s, %s);
        </script>""" % (func,
                        json.dumps(filename),
                        json.dumps(website_file_url),
                        json.dumps(message))
