         var notResponded = true;
          var thePlayer = jwplayer("myPlayer").setup({
                playlist: [
                             {
                                file:"{{generateQuestion.targetGestureVideo}}", 
                                image:"{{robothead_small_image}}",
                              },

                  ],
                  width: "100%",
              aspectratio: "595:576",
              stretching: "exactfit",
              autostart: true,
              events:{ 
                  onTime: function(event) {                 
                  },
                  onPlaylistComplete:function(){
                    // user timed out, disable choices, timedOut
                    console.log("enable buttons");
                    $("#nextBtn").removeClass("disabled");

                    if (notResponded){
                      var postdata={
                      'choice': 'noResponseRequired',
                      'target':"{{generateQuestion.targetGesture}}",
                      'phase': "{{phase}}",
                      'section': "{{section}}",
                      }
                      $.post('{% url 'exercises:userResponse' %}',postdata);
                    }
                    
                    
                  },
                  onPlaylistItem:function(index, playlist){
                    if (index["index"] == 0){
                      $("#trainingBtn").html("{{generateQuestion.targetGesture}}")

                    };
                  
                  }
                }
              }); 
            //stop player manual controls
              thePlayer.setControls(false);

        $(document).ready(function () {



          $.getScript("/static/js/setcsrf.js", function(){

             console.log("setcrsf.js loaded");

          });


        });