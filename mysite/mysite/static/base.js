
    function openCommentBox() {
        if (document.getElementById('CommentForm').checkValidity()) {
            commboxdiv = document.getElementById("id_comment_space")
            closeCommentModal(); // Close the modal
            commboxdiv.innerHTML = ""
            console.log("ok")
        } else {
            invalid = document.getElementById("id_invalid_fields")
            invalid.innerHTML = "Please answer all the questions."
            invalid.classList.add("alert", "alert-danger");
        }
    }


    function checkWordleGuess() {
        var guessInput = document.getElementById("wordleInput");
        var guess = guessInput.value.trim().toLowerCase();

        if (guess.length !== 5) {
            var result = document.getElementById("wordleResult");
            result.innerHTML = "Please enter a 5-letter word.";
            result.classList.add("alert", "alert-danger");
        } else {
            // Perform wordle guess validation and processing here
        }
    }
    function closeWordleModal() {
        $('#wordleModal').modal('hide'); // Close the Wordle modal
        document.getElementById('wordleInput').value = ""; // Reset the input field
        document.getElementById('wordleResult').innerHTML = ""; // Clear the result message
    }