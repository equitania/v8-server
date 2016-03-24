MyOdoo
----

MyOdoo ist ein "Fork" von Odoo, einem Browser gestützten Open Source Projekt für ERP, Warenwirtschaft, Lagerverwaltung, Webshop, CMS Anwendungen mit über 5.000 Zusatzmodule.

MyOdoo ist für den deutschsprachigen Raum optimiert. Deshalb werden nur die Sprachen Deutsch und Englisch unterstützt.
Die deutschen Sprachpakete unterscheiden sich in Details von den Standardpaketen, da diese aus unserer Sicht teilweise falsch, mißverständlich oder gar nicht übersetzt sind.

**Bugfixes & Änderungen abweichend vom Hauptfork Stand März 2016**

- /odoo/openerp/tools/misc.py -> Beschränkung der Sprachen auf Deutsch & Englisch

- /odoo/openerp/addons/base/res/res_config.py -> Erweiterung der Rechte-Gruppen um einen Managed Admin

- /odoo/addons/web/static/src/js/search.js -> Fehlerbeseitigung in der Suche

- /odoo/addons/web/static/lib/underscore.string/lib.underscore.string.js -> Fehlerbeseitigung

- /odoo/addons/website_sale_options/__openerp__.py -> Fehlerbeseitigung

- addons/website/data/data.xml -> Website Menü-Eintrag Kontakt wird beim Update nicht mehr geändert

- addons/web/static/src/js/view_form.js -> Positionenrn. un Verkaufsaufträgen werden jetzt richtig hochgezählt

- addons/website_event/data/event_data.xml -> Website Menü-Eintrag Veranstaltung wird beim Update nicht mehr geändert

- addons/website_sale/data/data.xml -> Website Menü-Eintrag Shop wird beim Update nicht mehr geändert



Unser Fork wird regelmäßig mit dem Hauptodoo Fork abgeglichen.

`Aktuelle Buildversion: 160302`

`Letzer Abgleich: 22.03.2016`

Dieser Fork obliegt der <a href="http://www.gnu.org/licenses/licenses.html">GNU Affero General Public License</a> wie das Ursprungssystem <a href="https://www.odoo.com">Odoo</a> selbst.


Mit MyOdoo starten 
-------------------------
Für eine Installation .

Dazu haben wir einige Installationsskripte vorbereitet.

Vorbereitung von Debian 8 oder Ubuntu:

	https://github.com/equitania/odoo-addons/blob/8.0/scripts/prepare-odoo-server-debian8.sh

Zur Installation des Servers:

	https://github.com/equitania/odoo-addons/blob/8.0/scripts/install-odoo-server-debian8.sh


Weitere Informationen unter <a href="https://www.myoodoo.de">Myodoo.de</a>




