$(document).ready(function() {
  console.log("once");
  $("#submit").click(function() {
    console.log("hello");
    var readable_location = $("#venue-name").val();
    var venue = $("#venue-id").val();
    var price = $("#price"). val();
    var description = $("textarea#description").val();
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
            $('.list').empty();
            for (var i = 0, len = response.length; i < len; i++) {
              $('.list').append("<li data-role=\"listview\"><div id=\"" + response[i].pk + "\"class=\"task-item\">" + "<a href=\"#\" id=\"" + response[i].pk + "\" class=\"title_t\">Task: " + response[i].fields['task_title'] + "</a></h2>" +  "<h3 class=\"location_t\">Location: " + response[i].fields['readable_location'] + "</h3>" +  "<h4 class=\"price_t\">Price: " + response[i].fields['price'] + "</h4>" +  "<p class=\"description_t\">Description: " + response[i].fields['task_description'] + "</p>" +  "<p class=\"status_t\">Status: " + response[i].fields['status'] + "</p></div></li>"); 
            }
            $("#venue").val("");
            $("#venue-name").val("");
            $("#venue-id").val("");
            $("#price").val("");
            $("#description").val("");
            $("#title").val("");
            $('.title_t').off();
            $(".title_t").on("click", function(event){
              event.preventDefault();
              console.log("hello");
              var task_id = this.id;
              console.log(task_id);
              $theClickedObject = $(this);
              $.post('/foursq_auth/_finishtask/', { task_id : task_id }, function(response) {
                console.log(response);
                $theClickedObject.css( "background-color", "red" );
                window.location = response;
              });
              return false;
              });
          },
          error: function() {
            alert("Error");
          },
      });
  });
});
