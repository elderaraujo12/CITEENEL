 /* scripts seção faq */
 $(document).ready(function () {

    $('.btn-plus').on('click', function() {
      $(this).parent('div').parent('div').parent('div').find('.issue-content').show('slow');
      $(this).hide();
      $(this).siblings('.btn-less').show();
    });

    $('.btn-less').on('click', function() {
      $(this).parent('div').parent('div').parent('div').find('.issue-content').hide('slow');
      $(this).hide();
      $(this).siblings('.btn-plus').show();
    })

  });