<script>


(function($) {

    $('.datepicker').datepicker();

    $("#weather").on('submit', function(e) {

      e.preventDefault();
      var postUrl = $(this).attr('action');

      var data = {
        start_date: $(this).find('#start_date').val(),
        end_date: $(this).find('#end_date').val(),
        location: $(this).find('#location').val(),
      };

      if (data['location'].length > 1) {

        $.ajax({
          type: "GET",
          url: postUrl,
          data: data,
          beforeSend: function() {
            $('.detail').html("<h2>Starting</h2>");
            $('.week-container').html("")
            $('.day-container').html("")
            $('.error').html("");
          },
          success: function(data) {
            var n = String(data).search("Please be more specific");
                $('.error').html("<h2>Please be more specific </h2>");
            if (n !=-1){
            } else {

                $('.error').html("<h2>Success</h2>");
                $('.error').append(data);
                //console.log(data)
                $('.error').append("<img src='" + data['image_src'] + "' />");

                $('.week-container').append('<canvas id="weekly"></canvas>');
                var ctx = document.getElementById('weekly');
                var myRadarChart = new Chart(ctx, {
                    type: 'line',
                      data: {
                        labels: data['week_data']['labels'],
                        datasets: [

                            {
                            data: data['week_data']['humidity'],
                            label: "humidity",
                            borderColor: "#3e95cd",
                            fill: false
                          }, {
                            data: data['week_data']['temp_min'],
                            label: "Temp Min",
                            borderColor: "#3cba9f",
                            fill: false
                          }, {
                            data: data['week_data']['temp_max'],
                            label: "Temp Max",
                            borderColor: "#e8c3b9",
                            fill: false
                          }
                        ]
                      },
                    options: {
                        title: {
                          display: true,
                          text: 'Projections for the next two days'
                        }
                      }
                });
                $('.day-container').append('<canvas id="2days"></canvas>');
                var average_hum = [];
                average_hum.fill(20, 0, 24);

                var ctx = document.getElementById('2days');
                var myRadarChart = new Chart(ctx, {
                    type: 'line',
                      data: {
                        labels: data['days_data']['labels'],
                        datasets: [

                            {
                            data: data['days_data']['humidity'],
                            label: "humidity",
                            borderColor: "#3e95cd",
                            fill: false
                          }, {
                            data: data['days_data']['temp_data'],
                            label: "Temp",
                            borderColor: "#e8c3b9",
                            fill: false
                          }, {
                            data: data['chart_average_daily_humidity'],
                            label: "Average Humidity",
                            borderColor: "#3cba9f",
                            fill: false
                          }, {
                            data: data['chart_average_daily_temp'],
                            label: "Average Temperature",
                            borderColor: "#3cba9f",
                            fill: false
                          }
                        ]
                      },
                    options: {
                        title: {
                          display: true,
                          text: 'Projection for the week'
                        }
                      }
                });
                $('.week-container').append("<h2>Humidity Average : "+ data['weekly_humidity'] +"</h2>")
                $('.week-container').append("<h2>Average Temp: "+ data['average_temp'] +"</h2>")
                $('.day-container').append("<h2>Humidity Average : "+ data['average_daily_humidity'] +"</h2>")
                $('.day-container').append("<h2>Average Temp: "+ data['average_daily_temp'] +"</h2>")
             }
          },
          error: function(xhr) {

            console.log(xhr)
            $('.error').html("<h2>Error</h2><p>" + xhr.responseText + "</p>");
          },
          complete: function() {
            $('.error').append("<p>Process complete</p>");
          }
        });
      } else {
        $('.detail').html("<h2>Error</h2><p>Please give at least a location!</p>");
      }
      return false;
    });

} (jQuery) );

</script>