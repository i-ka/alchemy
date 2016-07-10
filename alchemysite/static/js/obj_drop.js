$(document).ready(function()
{
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
	
	$("[name=orig_check]").click(function()
	{
		$("#recipe").slideToggle("fast");
		$("[name=first_recipe_el]").val("0");
		$("[name=second_recipe_el]").val("0");
		$("#drop1").text("Элемент 1");
		$("#drop2").text("Элемент 2");
		$("#drop1, #drop2").css("box-shadow", "");
	});
	
});		