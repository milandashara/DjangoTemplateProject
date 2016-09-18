// Full featured example







$("[data-toggle='confirmation']").popConfirm({
    //title: "Really ?",
    //content: "I have warned you !",
    placement: "top" // (top, right, bottom, left)
//     onConfirm: function show_in_progress() {
//     $('#progress').show();
// } // show on confirm
});

// $('[data-toggle="confirmation"]').confirmation({
//     placement: "top",
//     onConfirm: function() { 
//     document.getElementById('progress').className = 'show';
//     alert(document.getElementById('progress'));  }
// });

// $("#primary_radio_btn").click(function () {
// 
//     $("#replicate_token_to_slave").show();
//      return true;
//  }
// );
// 
// $("#secondary_radio_btn").click(function () {
// 
//     $("#replicate_token_to_slave").hide();
//      return true;
//  }
// );

$("#use_tls").click(function() {
   if ($("#use_tls").is(":checked"))
       $("#smtp_auth").prop('disabled', false);
    else {
       $("#smtp_auth").prop('checked', false);
       $("#smtp_auth").prop('disabled', true);
       $("#smtp_username").val("");
       $("#smtp_password").val("");
       $("#smtp_username").prop('required', false);
       $("#smtp_password").prop('required', false);
       $("#username_div").removeClass('has-error has-danger');
       $("#password_div").removeClass('has-error has-danger');
       $("#smtp_username").prop('disabled', true);
       $("#smtp_password").prop('disabled', true);
   }
});

$("#smtp_auth").click(function() {
   if ($("#smtp_auth").is(":checked")) {
       $("#smtp_username").prop('disabled', false);
       $("#smtp_password").prop('disabled', false);
       $("#smtp_username").prop('required', true);
       $("#smtp_password").prop('required', true);
   }
    else {
       $("#smtp_username").val("");
       $("#smtp_password").val("");
       $("#smtp_username").prop('required', false);
       $("#smtp_password").prop('required', false);
       $("#username_div").removeClass('has-error has-danger');
       $("#password_div").removeClass('has-error has-danger');
       $("#smtp_username").prop('disabled', true);
       $("#smtp_password").prop('disabled', true);
   }
});

$(function () {
  $('[data-toggle="tooltip"]').tooltip();
});


// $('#form_id').submit(function () {
//     $('#progress').show(); 
//     //return true;
// });

// function show_in_progress() {
//     $('#progress').show();
// }

//during full page reload hide it.
// $('#progress').hide();


