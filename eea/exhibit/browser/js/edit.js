if(window.DavizEdit === undefined){
  var DavizEdit = {'version': 'eea.exhibit'};
}

DavizEdit.Events = DavizEdit.Events || {};
DavizEdit.Events.exhibit = {
    initialized: 'exhibit-initialized'
};

DavizEdit.Exhibit = function(context, options){
  var self = this;
  self.context = context;

  self.settings = {
    more: 'Show advanced settings',
    less: 'Hide advanced settings'
  };

  if(options){
    jQuery.extend(self.settings, options);
  }

  self.initialize();
};

DavizEdit.Exhibit.prototype = {
  initialize: function(){
    var self = this;
    jQuery('div[id*="ex_"]', self.context).wrapAll(
      '<div class="eea-exhibit-group-advanced" />'
    );

    self.advanced = jQuery('.eea-exhibit-group-advanced', self.context).hide();
    jQuery('<a>')
      .attr('href', '#')
      .addClass('btn')
      .addClass('btn-block')
      .addClass('btn-large')
      .addClass('disabled')
      .addClass('btn-advanced-settings')
      .html(self.settings.more)
      .click(function(){
        if(self.advanced.is(':visible')){
          self.advanced.slideUp('slow');
          jQuery(this).html(self.settings.more);
        }else{
          self.advanced.slideDown('slow');
          jQuery(this).html(self.settings.less);
        }
        return false;
      }).insertBefore(self.advanced);
  }
};

jQuery.fn.EEAExhibit = function(options){
  return this.each(function(){
    var context = jQuery(this);
    var view = new DavizEdit.Exhibit(context, options);
    context.data('EEAExhibit', view);
  });
};

function addTutorials(){
    jQuery(".daviz-edit-fieldset:has(div[id*=ex_])").find("eea-tutorial").remove();
    jQuery(".daviz-edit-fieldset:has(div[id*=ex_])").prepend(
        jQuery("<div>")
            .addClass("eea-tutorial")
            .css("float","left")
            .css("margin-left","0")
            .css("display", "block")
            .css("margin-bottom", "20px")
            .css("margin-top", "10px")
            .css("font-size", "16px")
            .attr("tutorial","exhibit")
            .attr("message", "Configure exhibit visualization or"));
}

jQuery(document).ready(function(){
  // On init
  addTutorials();
  jQuery('.daviz-edit-fieldset:has(div[id*=ex_])').EEAExhibit();
  jQuery('.daviz-facet-edit:has(div[id*=ex_])').EEAExhibit({
    more: 'More options',
    less: 'Less options'
  });

  // On refresh
  jQuery(document).bind(DavizEdit.Events.views.refreshed, function(evt, data){
    addTutorials();
    jQuery('.daviz-edit-fieldset:has(div[id*=ex_])').EEAExhibit();
  });

  jQuery(document).bind(DavizEdit.Events.facet.refreshed, function(evt, data){
    jQuery('.daviz-facet-edit:has(div[id*=ex_])').EEAExhibit({
      more: 'More options',
      less: 'Less options'
    });
  });
});
