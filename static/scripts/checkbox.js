$(function() {
    $("#selectAll").click(function()
      {
        var checked_status = this.checked;
        $('input[name="deleteCB[]"]').each(function()
            {
              this.checked = checked_status;
            });
       });
            $("#delete_form").submit(function(e) {
          return false;       });

	var $dialog = $('<div></div>')
		.html('Item(s) have been successfully deleted')
		.dialog({
			autoOpen: false
		});
	var $dialog2 = $('<div></div>')
		.html('No checkboxes are checked!')
		.dialog({
			autoOpen: false,
			title: 'Error'
		});


     $("#deleteBtn").click(function() {
     if ($('input[type=checkbox]').is(':checked')){
        $( "#dialog-confirm" ).dialog({
                modal: false,
                      buttons: {
                            "Delete all items": function() {
                              $(this ).dialog( "close" );
                                        var data = $(":checkbox:checked").map(function(i,n)
                                              {
                                                return $(n).val();
                                            }).get();
                                                  $.post("process.php", { 'deleteCB[]': data },
                                                   function(){
                                                                $('body').load('index.php', function() {
                                                                  $dialog.dialog({title: 'Item(s) Deleted'});
                                                                  });
                                                            });
        },
        Cancel: function() {
          $( this ).dialog( "close" );
          return false;
        }
      } //end buttons
    });
    }
    else
    {
         $dialog2.dialog("open");
    }
   });
});

