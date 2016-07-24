$(document).ready(function() {
  $("#board").droppable({
    accept: ".tab-pane a",
    drop: function() {
      $(this).append($("<a>").attr("el_id", $(".ui-draggable-dragging").attr("el_id")).addClass("btn btn-default").text($(".ui-draggable-dragging").text()).draggable({
      containment: "parent",
      stack: ".btn"
      }));
    }
  });
});