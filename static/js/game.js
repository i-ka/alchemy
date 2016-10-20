$(document).ready(function() {
  $("#board").droppable({
    accept: ".tab-pane a",
    drop: function() {
      $(this).append($("<a>")
      .attr("el_id", $(".ui-draggable-dragging").attr("el_id"))
      .css("left", $(".ui-draggable-dragging").css("left"))
      .css("top", $(".ui-draggable-dragging").css("top"))
      .text($(".ui-draggable-dragging").text()));

      $("#board a").addClass("btn btn-default").draggable({
        containment: "parent",
        stack: ".btn"
      }).droppable({
        greedy: true,
        drop: function() {
          var mixable = $(this);
          var mixed = $(".ui-draggable-dragging");
          $.post("/check_elements/", {
            first_element: mixable.attr("el_id"),
            second_element: mixed.attr("el_id"),
            csrfmiddlewaretoken: getCookie("csrftoken")
          }, onAjaxSuccess);

          function onAjaxSuccess(data) {
            var elementData = $.parseJSON(data);
            if (elementData.success) {
              $("#lastElems").text(mixed.text() + " + " + mixable.text() + " = " + elementData.newElement.name);
              mixable.text(elementData.newElement.name).attr("el_id", elementData.newElement.id).effect("highlight").width("auto");
              mixed.remove();
              if ($(".tab-content [el_id = " + elementData.newElement.id + "]").length == 0) {
                dataUpdate();
              }
            } else {
              mixable.effect("highlight", { color: "red" });
              mixed.effect("highlight", { color: "red" });
            }
          }
        }
      }).click(function() {
        $("#lastElems").text(arrElements[$(this).attr("el_id")].description);
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