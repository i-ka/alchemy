$(document).ready(function()
{
    $("#head_btn").click(function(){
        $("#header").slideToggle("slow");
        $(this).toggleClass("active");
        return false;
    });
	
	$("#el_btn").click(function(){
		$(".tabs").slideToggle("slow");
		$(this).toggleClass("active");
		return false;
    });
    	
});		