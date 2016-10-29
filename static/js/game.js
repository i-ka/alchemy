function addElement(id, name, mixable) {
  if (!id) {
    $("#board").append($("<a>")
      .attr("el_id", $(".ui-draggable-dragging").attr("el_id"))
      .css("left", $(".ui-draggable-dragging").css("left"))
      .css("top", $(".ui-draggable-dragging").css("top"))
      .text($(".ui-draggable-dragging").text()));
  } else {
    $("#board").append($("<a>")
      .attr("el_id", id)
      .css("left", mixable.css("left"))
      .css("top", mixable.css("top"))
      .text(name)
      .effect("fade"));
  }

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
          addElement(elementData.newElement.id, elementData.newElement.name, mixable);
          mixable.remove();
          mixed.remove();
          if (!arrElements[elementData.newElement.id]) {
            dataUpdate();
          }
        } else {
          mixable.effect("highlight", { color: "red" });
          mixed.effect("highlight", { color: "red" });
        }
      }
    }
  }).click(function() {
    $("#lastElems").html("<b>" + arrElements[$(this).attr("el_id")].name + "</b> - " + arrElements[$(this).attr("el_id")].description);
  });
}

$(document).ready(function() {
  $("#board").droppable({
    accept: ".tab-pane a",
    drop: function() {
      addElement();
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