$(document).ready(function()
{	$(".tabs").on("mouseover", function(){
		$("ul.tabs_caption").each(function()
		{
			$(this).find("li").each(function(i)
			{
				$(this).click(function()
				{
					$(this).addClass("active").siblings().removeClass("active").closest("div.tabs").find("div.tabs_content").removeClass("active").eq(i).addClass("active");
				});
			});
		});
	});
});