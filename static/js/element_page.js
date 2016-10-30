function dropsFill() {
  if ($("[name=first_recipe_el]").val() != "" && $("[name=second_recipe_el]").val() != "") {
    if ($("[name=first_recipe_el]").val() != 0 && $("[name=second_recipe_el]").val() != 0) {
      $("#drop1").text(arrElements[$("[name=first_recipe_el]").val()].name);
      $("#drop2").text(arrElements[$("[name=second_recipe_el]").val()].name);
      $("#drop1, #drop2").removeClass("btn-default").addClass("btn-info");
    } else {
      $("[name=orig_check]").attr("checked", true);
      $("#recipe").removeClass("in");
    }
  } else {
    $("[name=first_recipe_el], [name=second_recipe_el]").removeAttr("value");
  }
}

$(document).ready(function() {
  $(".errorlist").addClass("alert alert-danger");
  $("#add-category-error").hide();
  $("#modal-add-category").submit(function() {
    event.preventDefault();
    $.post($(this).attr("action"), $("#modal-add-category").serialize(), function(data) {
      var error = "noErrors";
      switch (data) {
        case "failed":
          error = "Такая категория уже существует";
          break;
        case "success":
          location.reload();
          break;
      }
      if (error != "noErrors") {
        $("#add-category-error").show().text(error);
      }
    });
  });

  $("#drop1").droppable({
    drop: function() {
      $(this).text($(".ui-draggable-dragging").text());
      $("[name=first_recipe_el]").val(arrElements[$(".ui-draggable-dragging").attr("el_id")].id);
      $(this).removeClass("btn-default").addClass("btn-info");
    }
  }).click(function() {
    $(this).text("Элемент 1");
    $("[name=first_recipe_el]").removeAttr("value");
    $(this).removeClass("btn-info").addClass("btn-default");
  });

  $("#drop2").droppable({
    drop: function() {
      $(this).text($(".ui-draggable-dragging").text());
      $("[name=second_recipe_el]").val(arrElements[$(".ui-draggable-dragging").attr("el_id")].id);
      $(this).removeClass("btn-default").addClass("btn-info");
    }
  }).click(function() {
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