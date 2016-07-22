function elementLoad(categoryId) {
  $.getJSON("http://localhost:8000/alch-admin/get-elements-by-category/" + categoryId,function(elementData) {
    for (var j = 0; j < elementData.elements.length; j++) {
      $("#" + categoryId).append($("<a>").addClass("btn btn-default select").text(elementData.elements[j].name).attr("el_id", elementData.elements[j].id));

      $(".select").draggable ({ revert: true, revertDuration: 0 });
      $(".select").mouseover(function() {
        $(this).attr("id", "selected").css("cursor", "move");
      }).mouseleave(function() {
        $(this).removeAttr("id","selected");
      });
    }
  });
}

$(document).ready(function() {
  $.getJSON("http://localhost:8000/alch-admin/get_categories",function(categoryData) {
    $("[name=first_recipe_el], [name=second_recipe_el]").removeAttr("value");

    for (var i = 0; i < categoryData.categories.length; i++) {
      $(".nav-tabs").append($("<li>").append($("<a>").attr("data-toggle", "tab").attr("href", "#" + categoryData.categories[i].id).text(categoryData.categories[i].name)));
      $(".tab-content").append($("<div>").attr("id", categoryData.categories[i].id).addClass("tab-pane btn-group-vertical"));

      elementLoad(categoryData.categories[i].id);
    }
  });
});