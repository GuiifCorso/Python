$(document).ready(function() {
    $("#login_btn").click(function(event) {
        event.preventDefault()
        var name = $('#log_name').val()
        var pass = $('#log_pass').val()

        if (name.trim() === "" || pass === "") {
            alert("Please fill in all fields.");
            return; // Don't submit the form
        }


        $.post("/get_login_data", $("#login_forms").serialize(), function(log_data){
            if (log_data == "Correct data") {
                $("#log_res").html("Logged successfully!").css("color", "green");
            } else {
                $("#log_res").html("Incorrect data").css("color", "red");
            }
        }).fail(function(jqXHR, textStatus, errorThrown) {
            alert("Error during login: " + textStatus);
        });

        
    })
    $("#reg_btn").click(function(event) {
        event.preventDefault()
        var name = $('#reg_name').val()
        var pass = $('#reg_pass').val()
        console.log(name, pass)
        if (name.trim() === "" || pass === "") {
            alert("Please fill in all fields.");
            return; // Don't submit the form
        }
        $.post("/get_reg_data", $("#reg_forms").serialize(), function(reg_data){
            if (reg_data == "Registered successfully") {
                $("#reg_res").html("Registered successfully!").css("color", "green");
            } else {
                $("#reg_res").html("User already registered!").css("color", "red");
            }
        }).fail(function(jqXHR, textStatus, errorThrown) {
            alert("Error during login: " + textStatus);
        });
    })
}

)