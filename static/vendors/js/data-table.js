(function($) {
    'use strict';
    $(function() {
      $('#order-listing').DataTable({
        "aLengthMenu": [
          [5, 10, 15, -1],
          [5, 10, 15, "Hotu"]
        ],
        "iDisplayLength": 10,
        "language": {
          info: "Hatudu liña _START_ to'o _END_ husi liña _TOTAL_",
          lengthMenu: "Hatudu liña _MENU_",
          search: "",
          infoFiltered:   "(filtra husi totál entrada _MAX_)",
          loadingRecords: "Karega hela...",
          processing: "Prosesa hela...",
          zeroRecords: "La hetan entrada ruma",
          paginate: {
            next: "Tuirmai",
            previous: "Anteriór"
          }
        }
      });
      $('#order-listing').each(function() {
        var datatable = $(this);
        // SEARCH - Add the placeholder for Search and Turn this into in-line form control
        var search_input = datatable.closest('.dataTables_wrapper').find('div[id$=_filter] input');
        search_input.attr('placeholder', 'Buka');
        search_input.removeClass('form-control-sm');
        // LENGTH - Inline-Form control
        var length_sel = datatable.closest('.dataTables_wrapper').find('div[id$=_length] select');
        length_sel.removeClass('form-control-sm');
      });
    });
  })(jQuery);