$(document).ready(function()
{
	$.getJSON("http://127.0.0.1:8000/alch-admin/get-elements-by-category/1",function(data)
	{
		$("[name=first_recipe_el]").removeAttr("value");
		$("[name=second_recipe_el]").removeAttr("value");

		for(var i=0;i<data.elements.length;i++)
		{
			$("#list").append($("<div>").addClass("select").text(data.elements[i].name).attr("el_id",data.elements[i].id));
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

	$("#drop1").droppable
	({
		drop:function()
		{
			$(this).text($("#selected").text());
			$("[name=first_recipe_el]").val($("#selected").attr("el_id"));
			$(this).css("box-shadow", "inset 0 0 8px 1px #F5F6CE");
		}
	});
	
	$("#drop2").droppable
	({
		drop:function()
		{
			$(this).text($("#selected").text());
			$("[name=second_recipe_el]").val($("#selected").attr("el_id"));
			$(this).css("box-shadow", "inset 0 0 8px 1px #F5F6CE");
		}
	});

	$("#drop1").click(function()
	{
		$(this).text("Элемент 1");
		$("[name=first_recipe_el]").removeAttr("value");
		$(this).css("box-shadow", "");
	});	
	$("#drop2").click(function()
	{
		$(this).text("Элемент 2");
		$("[name=second_recipe_el]").removeAttr("value");
		$(this).css("box-shadow", "");
	});

});		