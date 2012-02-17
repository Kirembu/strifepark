/* Fluid Theme v1.0, June 22nd 2009, Metalab Design http://www.metalabdesign.com */

$(document).ready(function() {
	$("a[rel='external']").attr('target','_blank');			//open rel=external links in new window/tab
	$("a.zoomlink").fancybox({'zoomSpeedIn': 300, 'zoomSpeedOut': 300, 'overlayShow': true, 'centerOnScroll': false }); 
	$("ol.notes li:last-child").addClass("fp"); 			// Works around issue where note about initial post ("X posted this") has the class of "reblog" 
	$("ol.notes li").append("<div class='note-icon'></div><div class='li-bottom'></div>")  		// Manipulate the notes list because Tumblr doesn't let us customize the markup
	
	var start_page = $("#hidden_navinfo .startpage").text();	
	var next_page = parseInt(start_page) + 1;
	var total_pages = $("#hidden_navinfo .totalpages").text();	
	var loading_next_page = false;
	var new_posts = "";
	
	if ((ajax_loader === true) && 
		(navigator.userAgent.toLowerCase().match(/iPhone/i) != "iphone" ) && 
		(navigator.userAgent.toLowerCase().match(/iPod/i) != "ipod" ) )	{
			$("#classic-pagination").hide(); // Hide classic prev/next navigation
			$("#load-more-posts").show();	 // Show ajax load new post button
			$("#load-more-posts").bind("click", function(){  newPosts(); });  // Load new posts on click
			$("#load-more-posts .spinner").css({'background-image' : 'url(http://static.tumblr.com/xsp9wak/pmaklokn9/new-spinner-still.png)'});
	}		
	
	function newPosts(){
		if ( (next_page <= total_pages) && (! loading_next_page) ){
			loading_next_page = true;
			$("#load-more-posts .spinner").css({'background-image' : 'url(http://static.tumblr.com/xsp9wak/8aUkloi38/new-spinner.gif)'}); //animate the spinner
			jQuery.get("/page/" + next_page + "?cb="+ Math.random(), function(data){
				new_posts = data.split('<!-- posts-start -->')[1].split('<!-- posts-end -->')[0];
				$("#posts").append(new_posts);
				next_page++;
				loading_next_page = false;
				$("#load-more-posts .spinner").css({'background-image' : 'url(http://static.tumblr.com/xsp9wak/pmaklokn9/new-spinner-still.png)'});	 //freeze the spinner
				if (next_page > total_pages) { $("#load-more-posts").fadeOut(300); }  // Hide the button if we run out of pages 
				$("a.zoomlink").fancybox({'zoomSpeedIn': 300, 'zoomSpeedOut': 300, 'overlayShow': true, 'centerOnScroll': false });  //we have to fire this after every ajax load
		  	});
		}	
	}	
});


	