$(document).ready(function () {
  $.getJSON("http://localhost:8000/api/json_displaycategory", function (data) {
    $("#category_id").append($("<option>").text("-Select Category-"));
    data.map((item) => {
      $("#category_id").append(
        $("<option>").text(item.categoryname).val(item.id)
      );
    });
  });

  $("#category_id").change(function () {
    $.getJSON("http://localhost:8000/api/jsondisplaysubcategory",{'cid':$('#category_id').val()}, function (data) {
      $("#subcategory_id").empty()
      $("#subcategory_id").append($("<option>").text("-Select Brand-"));
      data.map((item) => {
        $("#subcategory_id").append(
          $("<option>").text(item.subcategory_name).val(item.id)
        );
      });
    });

  });

  $(function() {
    $( "#model_year" ).datepicker();
});

  

  
});
