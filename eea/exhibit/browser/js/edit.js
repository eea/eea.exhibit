if(window.DavizEdit === undefined){
  var DavizEdit = {'version': 'eea.exhibit'};
  DavizEdit.Events = {};
}

DavizEdit.Events.exhibit = {
    initialized: 'exhibit-initialized'
};

DavizEdit.Exhibit = function(context, options){
  var self = this;
  self.context = context;

  self.settings = {
  };

  if(options){
    jQuery.extend(self.settings, options);
  }

  self.initialize();
};

DavizEdit.Exhibit.prototype = {
  initialize: function(){
    var self = this;
    jQuery('div[id*=ex_]', self.context).wrapAll(
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
      .html('Advanced settings')
      .click(function(){
        if(self.advanced.is(':visible')){
          self.advanced.slideUp('slow');
          jQuery(this).html('Advanced settings');
        }else{
          self.advanced.slideDown('slow');
          jQuery(this).html('Basic settings');
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


jQuery(document).ready(function(){
  // On init
  jQuery('.daviz-edit-fieldset:has(div[id*=ex_])').EEAExhibit();

  // On refresh
  jQuery(document).bind(DavizEdit.Events.views.refreshed, function(evt, data){
    jQuery('.daviz-edit-fieldset:has(div[id*=ex_])').EEAExhibit();
  });

});
