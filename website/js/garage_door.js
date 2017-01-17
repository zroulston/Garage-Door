function actuateDoor(door){
        var data_string = '{"door" : "'+ door +'", "auth_key" : "14ba5723f2cd11983f7eeeac09601bA8", "is_test" : "False", "user": "zach", "get_image": "False"}'
        $.ajax({
                type: "POST",
                url: "/garage_door", 
                data: data_string,
                error: function( error ){
                        $('#response').html(alert(JSON.stringify(error)))
                	}
    	});
};
