//var password = document.getElementById("pass")
//  , confirm_password = document.getElementById("confirm_password");
//
//function validatePassword(){
//  if(password.value != confirm_password.value) {
//    confirm_password.setCustomValidity("Passwords Don't Match");
//  } else {
//    confirm_password.setCustomValidity('');
//  }
//}
//
//password.onchange = validatePassword;
//confirm_password.onkeyup = validatePassword;

function Validate() {
        var password = document.getElementById("pass").value;
        var confirmPassword = document.getElementById("confirm_password").value;
        if (password != confirmPassword) {
            alert("Passwords do not match.");
            return false;
        }
        return true;
    }