function elementLoad(categoryId) {
  var request;
  if (document.getElementById("board")) {
    request = "/get-open-elements-by-category/";
  } else {
    request = "/get-elements-by-category/";
  }
  $.getJSON( request + categoryId,function(elementData) {
    for (var j = 0; j < elementData.elements.length; j++) {
      $("#" + categoryId).append($("<a>").addClass("btn btn-default select").text(elementData.elements[j].name).attr("el_id", elementData.elements[j].id));
      $(".select").draggable({ helper: "clone" });
    }
  });
}

$(document).ready(function() {
  $.getJSON("/get_categories/",function(categoryData) {
    for (var i = 0; i < categoryData.categories.length; i++) {
      $(".nav-pills").append($("<li>").append($("<a>").attr("data-toggle", "pill").attr("href", "#" + categoryData.categories[i].id).text(categoryData.categories[i].name)));
      $(".tab-content").append($("<div>").attr("id", categoryData.categories[i].id).addClass("tab-pane fade"));
      elementLoad(categoryData.categories[i].id);
    }
  });
});