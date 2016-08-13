function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

$(document).ready(function() {
  $("#board").droppable({
    accept: ".tab-pane a",
    drop: function() {
      $(this).append($("<a>").attr("el_id", $(".ui-draggable-dragging").attr("el_id")).css("left", $(".ui-draggable-dragging").css("left")).css("top", $(".ui-draggable-dragging").css("top")).text($(".ui-draggable-dragging").text()));
      $("#board a").addClass("btn btn-default").draggable({
        containment: "parent",
        stack: ".btn"
      }).droppable({
        greedy: true,
        drop: function() {
          $(this).addClass("mixable");
          $(".ui-draggable-dragging").addClass("mixed");

          $.post(
            "/check_elements/",
            {
              first_element: $(".mixable").attr("el_id"),
              second_element: $(".mixed").attr("el_id"),
              csrfmiddlewaretoken: getCookie("csrftoken")
            },
            onAjaxSuccess
          );

          function onAjaxSuccess(data) {
            var elementData = $.parseJSON(data);
            if (elementData.success) {
              $(".mixable").text(elementData.newElement.name).attr("el_id", elementData.newElement.id).effect("highlight").removeClass("mixable");
              $(".mixed").remove();
              if ($(".tab-content [el_id = "+ elementData.newElement.id +"]").length == 0) {
                dataUpdate();
              }
            } else {
              $(".mixable").effect("highlight", {color: "red"}).removeClass("mixable");
              $(".mixed").effect("highlight", {color: "red"}).removeClass("mixed");
            }
          }
        }
      });
    }
  });
  $("#clearall").click(function() {
    $("#board a").fadeTo(1000, 0, function() {
      $("#board a").remove();
    });
  }).droppable({
    greedy: true,
    drop: function() {
      $(".ui-draggable-dragging").remove();
    }
  });
});