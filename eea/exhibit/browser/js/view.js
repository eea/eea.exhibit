jQuery(document).ready(function(){
  var onExhibitTabClick = function(settings){
    var css = jQuery(settings.tab).attr('class');
    if(css.indexOf('tab-daviz') !== -1){
      jQuery('.daviz-facets').show();
    }else{
      jQuery('.daviz-facets').hide();
    }
  };

  // Events
  jQuery(document).bind('eea-daviz-tab-click', function(evt, settings){
    onExhibitTabClick(settings);
  });

  // Call for first tab
  var api = jQuery("ul.chart-tabs").data('tabs');
  onExhibitTabClick({
      api: api,
      tab: api.getTabs()[0],
      index: 0
  });

});
