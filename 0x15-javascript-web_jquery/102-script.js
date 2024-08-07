$(document).ready(function () {
    $('#btn_translate').click(function () {
      const languageCode = $('#language_code').val();
      $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode })
        .done(function (data) {
          $('#hello').text(data.hello);
        })
        .fail(function () {
          $('#hello').text('Error fetching translation.');
        });
    });
  });
