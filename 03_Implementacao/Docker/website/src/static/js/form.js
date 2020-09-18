function timerRemoveAlert() {
    var x = document.getElementById("alert_form");
    if(x){
        setTimeout(function(){ x.parentNode.removeChild(x); }, 3000);
    }
}

const conf_password = document.getElementById('confirm_password');
const div_conf_password = document.evaluate("//div[input[@id='confirm_password']]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; //document.querySelector('#email + span.error');
const password = document.getElementById('password_reg');
const submit_button = document.getElementById('submitreg');

conf_password.addEventListener('input', function (event) {
  if (conf_password.value == password.value && conf_password.value != "") {
    submit_button.disabled = false;
    div_conf_password.removeChild(div_conf_password.childNodes[3]);
    div_conf_password.className = 'form-group';
  } else {
    showConfPassFormError();
    submit_button.disabled = true;
  }
});

function showConfPassFormError() {

    var element_error = document.evaluate("//div[input[@id='confirm_password'] and p[@class='help-block']]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; //document.querySelector('#email + span.error');
    if(!element_error){
       var error = document.createElement("p");
       error.id = "error_config_password"
       error.className = "help-block";
       var text = document.createTextNode("Passwords must match.");
       error.appendChild(text);
       div_conf_password.appendChild(error)
    }

    div_conf_password.className = 'form-group  has-error required';

}