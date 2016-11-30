## Modul website

#### 30.11.2016
#### Version 1.1.4
##### CHG
- Änderung des Timeouts für den Sliders von 10 Sek auf 5 Sek

#### 14.11.2016
#### Version 1.1.3
##### CHG
- Übersetzung korrigiert (Foie > Folie) 

#### 10.11.2016
#### Version 1.1.1
##### CHG
- Der "Automatic Footer" wird nun nichtmehr im "Anpassen"-Dropdown von der Website mit aufgelistet

#### 26.09.2016
#### Version 1.0.25
##### FIX
- HREFLANG wurde nun in der IF Abfrage angepasst, so dass es nur greift bei mehrsprachigen Websites. Der Druck wurde geprüft.

#### 23.09.2016
#### Version 1.0.23
##### FIX
- Anpassung vom 15.09.2016 rückgängig gemacht, nun können Angebote wieder gedruckt werden (SEO: hreflang if-abfrage auskommentiert damit die hreflang wieder funktioniert).

#### 15.09.2016
#### Version 1.0.21
##### FIX
- SEO: hreflang if-abfrage auskommentiert damit die hreflang wieder funktioniert

#### 11.05.2016
#### Version 1.0.18
##### ADD
- Das Meta-Tag <meta name="robots" content="index,follow" /> wird nun gesetzt, wenn das Flag "Suchmaschinen davon abhalten, diese Webseite zu indexieren [eq_website_customerportal] " in den Einstellungen nicht gesetzt ist.

#### 11.05.2016
#### Version 1.0.17
##### FIX
- Durch die Google Indexierung wurde im Backend ein Fehler verursacht, welcher das Laden von E-Mail Vorlagen nicht mehr ermöglicht hat. Dies wurde nun behoben.

#### 11.05.2016
#### Version 1.0.16
##### Änderung
- Es wird nun überprüft ob das Modul eq_website_customerportal installiert ist, um dann mit Hilfe des Flags zur Google Indexierung bei Aktivierung den Meta-Tag <meta name="robots" content="noindex,nofollow" /> zu setzen.

#### 22.04.2016
#### Version 1.0.15
##### Änderung
- Übersetzungen

#### 21.04.2016
#### Version 1.0.14
##### Änderung
- Mediacenter
1. Größenangaben der Buttons verbessert (statische Größen entfernt)
2. Ansicht der Bildmengen von 80 auf 12 verringert (12 Bilder wie in der standard Ansicht)
3. Die Höhe der Listenansicht der Bilder ist nun dynamisch anhand des ModalPopup-Inhaltes

#### 20.04.2016
#### Version 1.0.13
##### Änderung
- Mediacenter, Icon "Delete" auf der Listview Ansicht auf default "Papierkorb" geändert

#### 20.04.2016
#### Version 1.0.12
##### Erweiterung
- Mediacenter, In dem Listview kann man ab jetzt Bilder anwählen und sie werden automatisch übernommen

#### 20.04.2016
#### Version 1.0.11
##### Erweiterung
- Mediacenter, beide Listviews (Bilder und Dateien) wurde um Sortierung in der Spalte "Letzte Änderung" erweitert

#### 20.04.2016
#### Version 1.0.10
##### Erweiterung
- Mediacenter, beide Listviews (Bilder und Dateien) wurde um Sortierung (im Moment nur in der Spalte Dateiname) erweitert 

#### 20.04.2016
#### Version 1.0.9
##### Änderung
- Mediacenter, Listviews -> max. Anzahl der Zeile pro Seite auf 80 gesetzt

#### 20.04.2016
#### Version 1.0.8
##### Erweiterung
- Mediacenter um diese Features erweitert:
1. Beide Listviews (Bilder und Dateien) zeigen max. 80 Zeilen auf einer Seite
2. Die Ansicht "Images-ListView" wurde um eigene Logik für Pager erweitert
3. Pager für die Ansicht "Images-NormalView" wurde angepasst, damit die Logik von der Ansicht "Images-ListView" getrennt ist
4. Dateigröße ist ab jetzt immer in KB ein diesem Format angezeigt 95,22 KB
5. Beide ListViews haben jetzt eine Spalte "Letzte Änderung"

#### 18.04.2016
#### Version 1.0.7
##### Erweiterung
- Kern um Ivan's (Fileupload) und Sody's (Paging für jede Seite im Kontext) Anpassungen erweitert

#### 18.04.2016
#### Version 1.0.6
##### Änderung
- MediaCenter - Paging für Bilder verbessert. Ab jetzt funktioniert es korrekt mit Kontext jeder Seite

#### 15.04.2016
#### Version 1.0.5
##### Änderung
- Migration der Funktionalität vom eq_website_customerportal in Kern

#### 15.04.2016
#### Version 1.0.4
##### Änderung
- Änderung der kontextbezogene Suche + Änderung der Defaultansicht

#### 15.04.2016
#### Version 1.0.3
##### Erweiterung
- Mediacenter, Neue Buttons für "Normalview" und "Listview" zusammen mit der Basis für Korrektur fürs Paging

#### 15.04.2016
#### Version 1.0.2
##### Erweiterung
- Mediacenter, kontextbezogene Bildsuche auf im Normalview und Listview und Anzeige der Treffersuche verbesser. Ab jetzt wird immer die aktuelle ansicht (view) korrekt angezeigt und Benutzer wird nicht mehr zurück auf Normalview umgeleitet

#### 15.04.2016
#### Version 1.0.1
##### Erweiterung
- Mediacenter, Bildupload um Listview erweitert