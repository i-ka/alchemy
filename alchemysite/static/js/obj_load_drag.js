$(document).ready(function()
{
	$.getJSON("http://localhost:8000/alch-admin/get-elements-by-category/1",function(data)
	{
		$("[name=first_recipe_el]").removeAttr("value");
		$("[name=second_recipe_el]").removeAttr("value");
		$(".nav-tabs").append($("<li>").addClass('active').append($("<a>").attr('data-toggle', 'tab').attr('href', '#getCatName').text('getCatName')));
		$(".tab-content").append($("<div>").attr('id', 'getCatName').addClass("tab-pane in active btn-group-vertical"));
		for (var i = 0; i < data.elements.length; i++) {
			$("#getCatName").append($("<a>").addClass("btn btn-default select").text(data.elements[i].name).attr("el_id",data.elements[i].id));
		}
		$(".select").draggable
		({
			revert: true,
			revertDuration: 0
		});
		$(".select").mouseover(function()
		{
			$(this).attr("id","selected").css("cursor","move");
		}).mouseleave(function()
		{
			$(this).removeAttr("id","selected");
		}); 	
	});
	
});		