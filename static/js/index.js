function redirectTo(action) {
    var isLoggedIn = true; // Change this based on your actual logic

    if (isLoggedIn) {
        if (action === 'create_test') {
            // var button = document.getElementById("createTestButton");
            // if (button) {
            //     button.style.backgroundColor = "#A446E2"; // Change color on click
            // }
            window.location.href = '/create_test'; // Redirect to create_test URL
        } else if (action === 'create_questionnaire') {
            // var button = document.getElementById("createQuestionnaireButton");
            // if (button) {
            //     button.style.backgroundColor = "#A446E2"; // Change color on click
            // }
            window.location.href = '/blog'; // Redirect to blog page
        }
    } else {
        window.location.href = '/login'; // Redirect to the login page
    }
}
