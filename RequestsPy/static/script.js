$(document).ready(function() {
    $("#submit-btn").click(function() {
        var name = $("#name").val();
        var age = $("#age").val();
        var gender = $("#gender").val();
        var spends = $("#spends").val();

        // Basic validation
        if (name.trim() === "" || age === "" || gender === "" || spends === "") {
            alert("Please fill in all fields.");
            return; // Don't submit the form
        }
        $.post("/register_client", $("#client-form").serialize(), function(response) {
            if (response === "Client registered successfully!") {
                $("#result").html(response).css("color", "green"); // Success message in green
                updateClientList();
            } else {
                $("#result").html(response).css("color", "red"); // Error message in red
            }
        }).fail(function() {
            $("#result").html("An error occurred during registration.").css("color", "red");
            $("#result").html(response);
            updateClientList(); // Function to fetch and update the client list
        });
    });

    function updateClientList() {
        $.get("/get_clients", function(data) {
            // Construct HTML list items for each client and append to #client-list
            let clientListHTML = "<ul>";
            for (let client of data) {
                clientListHTML += `<li>${client.name}, ${client.age}, ${client.gender}, Spent: $${client.spends}</li>`;
            }
            clientListHTML += "</ul>";
            $("#client-list").html(clientListHTML);
        });
    }

    // Initial update of the client list on page load
    updateClientList();
});
