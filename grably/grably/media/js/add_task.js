$(document).ready(function() {
  $("#submit").click(function() {
    var venue = $("#venue-id").val();
    var price = $("#price"). val();
    var description = $("#description").val();
    var task_id = "empty";
    var title_task = $("#title").val();
    $.ajax({
          url: "/foursq_auth/_add_task/",
          type: "POST",
          dataType: "json",
          data: {
            'venue' : venue,
            'price' : price,
            'description' : description,
            'id' : task_id,
            'title' : title_task,
          },
          success: function(response) {
            console.log(response);
          },
          error: function() {
            alert("Error");
          },
      });
  });
});
