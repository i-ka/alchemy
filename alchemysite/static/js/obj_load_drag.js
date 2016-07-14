$(document).ready(function() {
  $.getJSON("http://localhost:8000/alch-admin/get_categories",function(data) {
    $("[name=first_recipe_el], [name=second_recipe_el]").removeAttr("value");
	
      for (var i = 0; i < data.categories.length; i++) {
        $(".nav-tabs").append($("<li>").append($("<a>").attr("data-toggle", "tab").attr("href", "#" + data.categories[i].id).text(data.categories[i].name)));
        $(".tab-content").append($("<div>").attr("id", data.categories[i].id).addClass("tab-pane btn-group-vertical"));

        $.getJSON("http://localhost:8000/alch-admin/get-elements-by-category/" + data.categories[i].id,function(data) {
          for (var j = 0; j < data.elements.length; j++) {
            $("#1").append($("<a>").addClass("btn btn-default select").text(data.elements[j].name).attr("el_id", data.elements[j].id));
          }

          $(".select").draggable ({ revert: true, revertDuration: 0 });
          $(".select").mouseover(function() {
            $(this).attr("id", "selected").css("cursor", "move");
          }).mouseleave(function() {
            $(this).removeAttr("id","selected");
          });
        });
      }
  });
});