function submitToGoogleForms(firstName, lastName, favoriteColor) {
    document.getElementById('firstNameField').value = firstName;
    document.getElementById('lastNameField').value = lastName;
    if(favoriteColor === "Vert") {
        document.getElementById('colorGreen').checked = true;
    } else if(favoriteColor === "Bleu") {
        document.getElementById('colorBlue').checked = true;
    }
    
    // Soumettre le formulaire
    document.getElementById('hiddenForm').submit();
}