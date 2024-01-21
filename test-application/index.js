$(document).ready(function () {
    // Attach keyup event handler to the input field
    $('#searchInput').keyup(function () {
        // Check if the length of the entered text is at least 4 characters
        if ($(this).val().length >= 4) {
            // Make Ajax call
            $.ajax({
                url: 'http://127.0.0.1:5000/predict', // Replace with your server endpoint
                method: 'POST', // Use POST or GET as needed
                contentType: 'application/json', 
                data: JSON.stringify({ text: $(this).val() }), // Pass the entered text as a parameter
                success: function (data) {
                    // Handle the success response from the server
                    $('#searchResults').html(data.predicted_category);
                },
                error: function (xhr, status, error) {
                    // Handle errors
                    console.error(xhr.responseText);
                }
            });
        } else {
            // Clear search results if the entered text is less than 4 characters
            $('#searchResults').empty();
        }
    });
});