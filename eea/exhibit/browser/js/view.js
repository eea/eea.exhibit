jQuery(document).ready(function(){
  var onExhibitTabClick = function(settings){
    var css = jQuery(settings.tab).attr('class');
    if(css.indexOf('tab-daviz') !== -1){
      jQuery('.daviz-facets').show();
    }else{
      jQuery('.daviz-facets').hide();
    }

    // Refresh timeline
    if(css.indexOf('timeline') !== -1){
      try{
        var timeline = Timeline.getTimelineFromID(0);
        var now = new Date();
        timeline.layout();
        timeline.getBand(0).scrollToCenter(now);
      }catch(timeError){
        if(window.console !== undefined){
          console.log(timeError);
        }
      }
    }

    // Refresh map
    if(css.indexOf('daviz-map') !== -1){
      try{
        var _map = exhibit.getComponent('daviz-map')._map;
        google.maps.event.trigger(_map, 'resize');
      }catch(mapError){
        if(window.console !== undefined){
          console.log(mapError);
        }
      }
    }

  };

  // Events
  jQuery(document).bind('eea-daviz-tab-click', function(evt, settings){
    onExhibitTabClick(settings);
  });

  var index = 0;
  var api = jQuery("ul.chart-tabs").data('tabs');
  if (!api) {
    return;
  }
  jQuery.each(api.getTabs(), function(idx, tab){
    if(jQuery(tab).attr('href') == window.location.hash){
      index = idx;
      return false;
    }
  });

  // Call for first tab
  onExhibitTabClick({
      api: api,
      tab: api.getTabs()[index],
      index: index
  });

  jQuery(window).on('exhibitStatePushed', function(evt, location_hash) {
    document.location.hash = location_hash;
    delete document.location_hash;
  });

});
