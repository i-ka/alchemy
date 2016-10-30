var arrElements = [];

function elementLoad(categoryId, isLast) {
  var request;
  if (document.getElementById("board")) {
    request = "/get-open-elements-by-category/";
  } else {
    request = "alch-admin/get-elements-by-category/";
  }
  $.getJSON(request + categoryId,function(elementData) {
    if (elementData.elements.length == 0) {
        if (document.getElementById("board")) {
          $("#" + categoryId).text("Пока нет открытых элементов").addClass("alert errorlist alert-info text-center");
        } else {
          $("#" + categoryId).text("В категории нет элементов").addClass("alert errorlist alert-info text-center");
        }
    } else {
      $("#" + categoryId).text("").removeClass("alert errorlist alert-info text-center");
    }
    for (var j = 0; j < elementData.elements.length; j++) {
      arrElements.push(elementData.elements[j]);  // TODO: it shouldn't push element if it already exists
      $("#" + categoryId).append($("<a>").addClass("btn btn-default select").text(elementData.elements[j].name).attr("el_id", arrElements.length - 1));
      $(".select").draggable({ helper: "clone" }).click(function() {
        $("#lastElems").html("<b>" + arrElements[$(this).attr("el_id")].name + "</b> - " + arrElements[$(this).attr("el_id")].description);
      });
    }
    if (isLast && !document.getElementById("board")) {
      dropsFill();
    }
  });
}

function dataUpdate() {
  $(".select").remove();
  $.getJSON("/get_categories/",function(categoryData) {
    for (var i = 0; i < categoryData.categories.length; i++) {
      elementLoad(categoryData.categories[i].id);
    }
  });
}

$(document).ready(function() {
  $.getJSON("/get_categories/",function(categoryData) {
    for (var i = 0; i < categoryData.categories.length; i++) {
      $(".nav-pills").append($("<li>").append($("<a>").attr("data-toggle", "pill").attr("href", "#" + categoryData.categories[i].id).text(categoryData.categories[i].name)));
      $(".tab-content").append($("<div>").attr("id", categoryData.categories[i].id).addClass("tab-pane fade"));
      elementLoad(categoryData.categories[i].id, i == categoryData.categories.length - 1);
    }
  });
});