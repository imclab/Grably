$(document).ready(function() {
  $("#checkin").click(function() {
    var venue = $("#venue-id").val();
    console.log(venue);
    $.ajax({
          url: "/foursq_auth/_add_task/",
          type: "POST",
          dataType: "json",
          data: {
            'task_id' : task_id
          },
          success: function(response) {
              console.log("hellod");
            console.log(response);
            if (response.length == 0) {
              $('.list').append("<h1>Sorry - no tasks for you here.</h2>");
            }
            else {
              for (var i = 0, len = response.length; i < len; i++) {
                $('.list').append("<li><div id=\"" + response[i].pk + "\"class=\"task-item\">" + "<a class=\"title_t\"  id=\"" + response[i].pk + "\"href=\"#\">Task: " + response[i].fields['task_title'] + "</a>" +  "<h3 class=\"location_t\">Location: " + response[i].fields['readable_location'] + "</h3>" +  "<h4 class=\"price_t\">Price: " + response[i].fields['price'] + "</h4>" +  "<p class=\"description_t\">Description: " + response[i].fields['task_description'] + "</p>" +  "<p class=\"status_t\" id=\"" + response[i].pk + "\">Status: " + response[i].fields['status'] + "</p></div></li>"); 
              }
              $(".form").remove();
              $("#venue").remove();
            }
            $('.title_t').off();
            $(".title_t").on("click", function(event){
              event.preventDefault();
              console.log("hello");
              var task_id = this.id;
              $theClickedObject = $(this);
              $.post('/foursq_auth/_finishtask/', { task_id : task_id }).done(function(response) {
                console.log(response)
                $theClickedObject.css( "background-color", "red" );
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
