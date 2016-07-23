$(document).ready(function() {
  $("[name=first_recipe_el], [name=second_recipe_el]").removeAttr("value");
  $("#drop1").droppable({
    drop: function() {
      $(this).text($("#selected").text());
      $("[name=first_recipe_el]").val($("#selected").attr("el_id"));
      $(this).removeClass("btn-default").addClass("btn-info");
    }
  });
  $("#drop2").droppable({
    drop: function() {
      $(this).text($("#selected").text());
      $("[name=second_recipe_el]").val($("#selected").attr("el_id"));
      $(this).removeClass("btn-default").addClass("btn-info");
    }
  });
  $("#drop1").click(function() {
    $(this).text("Элемент 1");
    $("[name=first_recipe_el]").removeAttr("value");
    $(this).removeClass("btn-info").addClass("btn-default");
  });
  $("#drop2").click(function() {
    $(this).text("Элемент 2");
    $("[name=second_recipe_el]").removeAttr("value");
    $(this).removeClass("btn-info").addClass("btn-default");
  });

  $("[name=orig_check]").click(function() {
    $("[name=first_recipe_el]").val("0");
    $("[name=second_recipe_el]").val("0");
    $("#drop1").text("Элемент 1");
    $("#drop2").text("Элемент 2");
    $("#drop1, #drop2").removeClass("btn-info").addClass("btn-default");
  });
});