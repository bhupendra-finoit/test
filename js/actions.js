$(document).ready(function () {   

//hide homepage intro
$('#intro_hide').click(function() {
      $('#main_info').slideUp('slow', function() {
        // Animation complete
      });
    });
	
			
			
//show-hide cart
$(".icon_bag").click(function(e) {          
				e.preventDefault();
                $("#cart_box").toggle();
				$(".icon_bag").toggleClass("icon_active_bag");
            });
			
			
			$("div#cart_box").mouseup(function() {
				return false;
			});
			$(document).mouseup(function(e) {
				if($(e.target).parent("a.icon_bag").length==0) {
					$(".icon_bag").removeClass("icon_active_bag");
					$("#cart_box").hide();
				}
			});	
$(".close_cart").click(function(){
		$("#cart_box").hide();
	});	
	
	//hide cart on pressing esc key
	$(document).keydown( function( e ) {
  	if( e.which == 27) {  // escape, close box
     	$("#cart_box").hide();
   		}
 	}); 





//show-hide product info details
$(".pd_info_details").click(function(e) {          
				e.preventDefault();
                $("#product_info_box").toggle();
			});
			
			
			$("div#product_info_box").mouseup(function() {
				return false;
			});
			$(document).mouseup(function(e) {
				if($(e.target).parent("a.pd_info_details").length==0) {
					$("#product_info_box").hide();
				}
			});	
$(".close_sh_btn").click(function(){
		$("#product_info_box").hide();
	});	






//show-hide button
$(".sh_btn").click(function(e) {          
				e.preventDefault();
                $("#hide_product_page").toggle();
			});
			
			
			$("div#hide_product_page").mouseup(function() {
				return false;
			});
			$(document).mouseup(function(e) {
				if($(e.target).parent("a.sh_btn").length==0) {
					$("#hide_product_page").hide();
				}
			});	
$(".close_sh_btn").click(function(){
		$("#hide_product_page").hide();
	});	





//help content box for bid type
//show-hide button
$(".help_icon").click(function(e) {          
				e.preventDefault();
                $("#help_content_box").toggle();
			});
			
			
			$("div#help_content_box").mouseup(function() {
				return false;
			});
			$(document).mouseup(function(e) {
				if($(e.target).parent("a.help_icon").length==0) {
					$("#help_content_box").hide();
				}
			});	
$(".close_sh_btn").click(function(){
		$("#help_content_box").hide();
	});	





//hide_product on product_page 
$(".hide_slide_action2").click(function(e) {          
				e.preventDefault();
                $("#hide_product_page").toggle();
			});
			
			
			$("div#hide_product_page").mouseup(function() {
				return false;
			});
			$(document).mouseup(function(e) {
				if($(e.target).parent("a.hide_slide_action2").length==0) {
					$("#hide_product_page").hide();
				}
			});	
$(".close_sh_btn").click(function(){
		$("#hide_product_page").hide();
	});	





//submit offer form error on product_page 
//show-hide button
$(".so_form").click(function(e) {          
				e.preventDefault();
                $("#form_error_box").toggle();
			});
			
			
			$("div#form_error_box").mouseup(function() {
				return false;
			});
			$(document).mouseup(function(e) {
				if($(e.target).parent("a.so_form").length==0) {
					$("#form_error_box").hide();
				}
			});	
$(".close_sh_btn").click(function(){
		$("#form_error_box").hide();
	});	







//share box show-hide
$("#share_link, #share_link2").click(function(e) {          
				e.preventDefault();
                $("#share_box").toggle();
			});
			
			
			$("div#share_box").mouseup(function() {
				return false;
			});
			$(document).mouseup(function(e) {
				if($(e.target).parent("a#share_link").length==0) {
					$("#share_box").hide();
				}
			});	
$(".close_sh_btn").click(function(){
		$("#share_box").hide();
	});	
	


//product page interaction for color values
$('#color_attr2 li').click(function() { 
		//remove class active_pa_color from any li element inside #color_attr
		$('#color_attr2 li').removeClass("active_pa_color").addClass("inactive_pa");
		//apply class="active_pa_color" to this element
		$(this).removeClass("inactive_pa").addClass("active_pa_color");
		var title = $(this).attr("title");
		//add selected color value to #active_color_value span
		$('#active_color_value').replaceWith( "<span id=\"active_color_value\">"+ title +"</span>" );
		//replace hidden field with the selected value
		$('#product_color_input').replaceWith( "<input id=\"product_color_input\" type=\"hidden\" value=\""+ title +"\">" );

});


//product page interaction for size values
$('#size_attr2 li').click(function() { 
		//remove class active_pa_color from any li element inside #color_attr
		$('#size_attr2 li').removeClass("active_pa_size").addClass("inactive_pa");
		//apply class="active_pa_color" to this element
		$(this).removeClass("inactive_pa").addClass("active_pa_size");
		var title = $(this).attr("title");
		//add selected color value to #active_color_value
		$('#active_size_value').replaceWith( "<span id=\"active_size_value\">"+ title +"</span>" );
		$('#product_size_input').replaceWith( "<input id=\"product_size_input\" type=\"hidden\" value=\""+ title +"\">" );

});


//login page interaction to show-hide content
	//on clicking #show_login show #login_form and #reg_suggest && hide #login_instruction and #registration_form
	$('#show_login, #reg_now').click(function() { 
			//show #login_form and #reg_suggest
			$('#login_form').toggle();
			$('#reg_suggest').toggle();
			//hide #login_instruction and #registration_form
			$('#login_instruction').toggle();
			$('#registration_form').toggle();
	
	});

	
		
	
//show-hide shipping address form depending on user's selection	
	$('#sa_ba, #sa_ba_label').click(function(){
		// If checked
        if ($("#sa_ba").is(":checked"))
        {
            //hide shipping address
            $("#shipping_address_form").hide();
        }
        else
        {     
            //otherwise, show it
            $("#shipping_address_form").show();
        }
	});

//show hide reply box when reply comment button is clicked
	$(".reply_icon").click(function(){
		//hide any existing reply box and show all the hidden reply icon
		$(".reply_box").remove();
		$(".reply_icon").show();
		//insert the form html next to this button
		$(this).after('<div class=\"reply_box\"><form action=\"\" method=\"post\"><textarea class=\"comment_reply\"></textarea><div><input class=\"black_button button left\" type=\"submit\" value=\"Post Reply\" /><span class=\"hide_reply_box\">Cancel</span></div></form></div>');
		//hide this button
		$(this).hide();
	});
	//on clicking hide_reply_box, hide reply box and show reply button
	$(".hide_reply_box").live('click', function(){
		//e.stopPropagation();
		$(".reply_icon").show();
		$(".reply_box").remove();
	});
	
});
