openerp.eq_myodoo_backend_theme = function (instance) {

    var QWeb = instance.web.qweb,
        _t = instance.web._t;

    instance.web.Client.include({
        
        show_annoucement_bar: function() {
            return;
        },
        
        bind_events: function () {
            var self = this;
            this._super();
            
            var root = self.$el.parents();
            var elem_sm = $("<button id='leftbar_toggle' type='button' class='navbar-toggle left'><span class='icon-bar'></span><span class='icon-bar'></span></button>");
            elem_sm.prependTo(root.find('.navbar-header'));

            self.$el.on('click', '#leftbar_toggle', function () {
                var leftbar = root.find('.oe_leftbar');
                if (leftbar.css('display') == 'none') {
                    leftbar.removeClass("hide");
                    leftbar.addClass("show");
                } else {
                    leftbar.removeClass("show");
                    leftbar.addClass("hide");
                }
            });
        }
    });
    
    instance.web.Menu.include({
        reflow: function(behavior) {
            var self = this;
            var $more_container = this.$('#menu_more_container').hide();
            var $more = this.$('#menu_more');
            var $systray = this.$el.parents().find('.oe_systray');
    
            $more.children('li').insertBefore($more_container);  // Alles aus dem Mehr-Menü ziehen
    
            // 'all_outside' beahavior sollte alle Elemente anzeigen, Also den Mehr-button verstecken und schließen
            if (behavior === 'all_outside') {
                // Show list of menu items
                self.$el.show();
                this.$el.find('li').show();
                $more_container.hide();
                return;
            }
    
            // Alle Menü Elemente ausblenden
            var $toplevel_items = this.$el.find('li').not($more_container).not($systray.find('li')).hide();
            // Zeige die Liste der Menüeinträge, da diese Einträge bis jetzt noch unsichtbar sind
            self.$el.show();
            $toplevel_items.each(function() {
                var remaining_space = self.$el.parent().width() - $more_container.outerWidth() - 75;
                self.$el.parent().children(':visible').each(function() {
                    remaining_space -= $(this).outerWidth();
                });
    
                if ($(this).width() >= remaining_space) {
                    return false; // Das aktuelle Element wird dem more_container angehängt
                }
                $(this).show(); // Zeige das aktuelle Element in der Menü-Leiste
            });
            $more.append($toplevel_items.filter(':hidden').show());
            $more_container.toggle(!!$more.children().length);
            // Übermenüpunkt ausblenden wenn es nur einen gibt
            var $toplevel = self.$el.children("li:visible");
            if ($toplevel.length === 1) {
                $toplevel.hide();
            }
        },
        
        open_menu: function(id) {
            var self = this;

            var root = self.$el.parents();
            var oe_main_menu_placeholder = root.find('#oe_main_menu_placeholder');
            
            if (oe_main_menu_placeholder.hasClass("in")) {
                oe_main_menu_placeholder.removeClass("in");
            }
            
            this._super(id);
        }
            
    });

}