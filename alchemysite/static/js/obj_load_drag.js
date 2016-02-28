$(document).ready(function()
{
	$.getJSON("http://localhost:8000/alch-admin/get-elements-by-category/1",function(data)
	{
		$("[name=first_recipe_el]").removeAttr("value");
		$("[name=second_recipe_el]").removeAttr("value");
		$(".tabs_caption").append($("<li>").text("data.category.name"));
		$(".tabs").append($("<div>").addClass("tabs_content"));
		for(var i=0;i<data.elements.length;i++)
		{
			$(".tabs_content").append($("<div>").addClass("select").text(data.elements[i].name).attr("el_id",data.elements[i].id));
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