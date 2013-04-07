$(document).ready(function() {
  $("#checkin").click(function() {
    var venue = $("#venue-id").val();
    console.log(venue);
    $.ajax({
          url: "/foursq_auth/_checkin/",
          type: "POST",
          dataType: "json",
          data: {
            'venue' : venue,
          },
          success: function(response) {
            console.log(response);
            if (response.length == 0) {
              $('.list').append("<h1>Sorry - no tasks for you here.</h2>");
            }
            else {
              for (var i = 0, len = response.length; i < len; i++) {
                $('.list').append("<li><div id=\"" + response[i].pk + "\"class=\"task-item\">" + "<h2 class=\"title_t\">Task: " + response[i].fields['task_title'] + "</h2>" +  "<h3 class=\"location_t\">Location: " + response[i].fields['readable_location'] + "</h3>" +  "<h4 class=\"price_t\">Price: " + response[i].fields['price'] + "</h4>" +  "<p class=\"description_t\">Description: " + response[i].fields['task_description'] + "</p>" +  "<p class=\"status_t\">Status: " + response[i].fields['status'] + "</p></div></li>"); 
              }
              $(".form").remove();
              $("#venue").remove();
            }
          },
          error: function() {
            alert("Error");
          },
      });
  });
});
