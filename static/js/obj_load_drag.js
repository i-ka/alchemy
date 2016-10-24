var arrElements = [];

function elementLoad(categoryId, isLast) {
  var request;
  if (document.getElementById("board")) {
    request = "/get-open-elements-by-category/";
  } else {
    request = "alch-admin/get-elements-by-category/";
  }
  $.getJSON( request + categoryId,function(elementData) {
    for (var j = 0; j < elementData.elements.length; j++) {
      arrElements[elementData.elements[j].id] = {
        id: elementData.elements[j].id,
        name: elementData.elements[j].name,
        first_recipe_el: elementData.elements[j].first_recipe_el,
        second_recipe_el: elementData.elements[j].second_recipe_el,
        description: elementData.elements[j].description,
        category: elementData.elements[j].category.id
      }
      $("#" + categoryId).append($("<a>").addClass("btn btn-default select").text(elementData.elements[j].name).attr("el_id", elementData.elements[j].id));
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