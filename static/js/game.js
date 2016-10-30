function addElement(name, mixable) {
  if (!name) { // add element from list
    $("#board").append($("<a>")
      .attr("el_id", $(".ui-draggable-dragging").attr("el_id"))
      .css("left", $(".ui-draggable-dragging").css("left"))
      .css("top", $(".ui-draggable-dragging").css("top"))
      .text($(".ui-draggable-dragging").text()));
  } else { // add element after mixing
    $("#board").append($("<a>")
      .attr("el_id", arrElements.length)
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
        first_element: arrElements[mixable.attr("el_id")].id,
        second_element: arrElements[mixed.attr("el_id")].id,
        csrfmiddlewaretoken: getCookie("csrftoken")
      }, onAjaxSuccess);

      function onAjaxSuccess(data) {
        var elementData = $.parseJSON(data);
        if (elementData.success) {
          $("#lastElems").text(mixed.text() + " + " + mixable.text() + " = " + elementData.newElement.name);
          addElement(elementData.newElement.name, mixable);
          mixable.remove();
          mixed.remove();
          if (!arrElements[elementData.newElement.id]) { // TODO: check somehow if element is new or was opened before
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