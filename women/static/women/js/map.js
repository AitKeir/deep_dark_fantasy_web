$(function () {

  /* 2. INITIALIZE THE FILE UPLOAD COMPONENT */
//  $("#fileupload").fileupload({
//    dataType: 'json',
//    done: function (e, data) {  /* 3. PROCESS THE RESPONSE FROM THE SERVER */
//      if (data.result.form_is_valid) {
//        $("#gallery tbody").prepend(
//          "<tr><td><a href='" + data.result.url + "'>" + data.result.name + "</a></td></tr>"
//        )
//      }
//    }
//  });

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-map").modal("show");
      },
      success: function (data) {
        $("#modal-map .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
//      data: form.serialize(),
      data: new FormData(this),
      type: form.attr("method"),
      dataType: 'json',
      processData: false,
      contentType: false,
      success: function (data) {
        if (data.form_is_valid) {
          $("#map-table tbody").html(data.html_book_list);
          $("#modal-map").modal("hide");
        }
        else {
          $("#modal-map .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  var openFile = function () {
    $("#id_map").click();
  };

  /* Binding */

  // Create map
  $(".js-create-map").click(loadForm);
  $("#modal-map").on("submit", ".js-map-create-form", saveForm);

  // Update map
  $("#map-table").on("click", ".js-update-map", loadForm);
  $("#modal-map").on("submit", ".js-map-update-form", saveForm);

  // Delete book
  $("#map-table").on("click", ".js-delete-map", loadForm);
  $("#modal-map").on("submit", ".js-map-delete-form", saveForm);

      /* 1. OPEN THE FILE EXPLORER WINDOW */
  $("#modal-map").on("click", ".js-upload-photos", openFile);
});