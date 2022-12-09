$(document).ready(function(){
	alert("This page has loaded!");

	//Below is code which hides a paragraph when the button is clicked
	$("button").click(function(){
        $("p").hide("slow", function(){
            alert("The paragraph is now hidden");
        });
    });
		//let width  =Math.max($(document).width(), $(window).width());
		//let height=Math.max($(document).height(), $(window).height());
		let height=$(window).height();
		let width=$(window).width();
	//Below is code which allows for the character to move - why not try craft your own version?
	$(document).keydown(function(key) {
		//document.write(Math.max($(document).height(), $(window).height()));
		//	document.write(Math.max($(document).width(), $(window).width()));

        switch(parseInt(key.which,10)) {
			// Left arrow key pressed
			case 37:
				//This if statement only checks if the current position is greater than 0 and not the new position after the key is pressed, try changing the position the if statement to check
				//the new position when keydown is pressed. You can apply these to the other cases
                if($('img').position().left > 0){                     
				    $('img').animate({left: "-=20px"}, 'fast');}

					break;
			// Up Arrow Pressed
			case 38:
				$('img').animate({top: '-=20px'},'fast');
				break;
			// Right Arrow Pressed
			case 39:
if($('img').position().left<width){ 
	//try maintain proper indentation to your code as it makes it easier to read and comprehend, this if statement should be indented to fall under case 39 as it is positioned in case 37
				$('img').animate({left: '+=20px'},'fast');}
				break;
			// Down Arrow Pressed
			case 40:
				$('img').animate({top: '+=20px'},'fast');
				break;
		}
	});
});
