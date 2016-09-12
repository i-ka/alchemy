$(document).ready(function() {
  $(".search").keyup(function() {
    var searchTerm = $(".search").val();
    var listItem = $(".results tbody").children("tr");
    var searchSplit = searchTerm.replace(/ /g, "'):contains('")

    $.extend($.expr[":"], {
      "contains": function(elem, i, match, array) {
        return (elem.textContent || elem.innerText || "").toLowerCase().indexOf((match[3] || "").toLowerCase()) >= 0;
      }
    });

    $(".results tbody tr").not(":contains('" + searchSplit + "')").each(function(e) {
      $(this).attr("visible", "false");
    });

    $(".results tbody tr:contains('" + searchSplit + "')").each(function(e) {
      $(this).attr("visible", "true");
    });

    var result = $(".results tbody tr[visible='true']").length;
    $(".counter").text("Найдено: " + result);

    if (result == "0") {
      $(".no-result").show();
    } else {
      $(".no-result").hide();
    }
  });
});