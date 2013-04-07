$(document).ready(function() {
  $("#submit").click(function() {
    var readable_location = $("#venue-name").val();
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
            'readable_location' : readable_location,
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
