$(function () {
  $('#btn_translate').click(function () {
    const langCode = $('#language_code').val();
    const urlPath = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;
    $.get(urlPath, function (data, status) {
      if (status === 'success') {
        $('#hello').text(data.hello);
      }
    });
  });
});
