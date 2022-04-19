(function($) {
    'use strict';
    $(function() {
      

        $('form').on('submit', function() {
            $('#addEpisodeModal').modal('toggle')
          });
          
          $('#id_condition, #id_arrival_mode, #id_main_illness_problem, #id_referal').select2({
              dropdownParent: $('#episodeModalLabel'),
              language: {
                  noResults: function (params) {
                    return "Laiha Rejistu.";
                  }
                }
          });
  
          $('#id_onset, #id_category').select2({
            dropdownParent: $('#pills-condition'),
            language: {
                noResults: function (params) {
                  return "Laiha Rejistu.";
                }
              }
          });
  
          $(function() {
            $('[data-toggle="datepicker"]').datepicker({
              autoclose: true,
              todayHighlight: true,
              autoHide: true,
              zIndex: 2048,
              container: '.modal-body',
            });
          });


    });
})(jQuery);