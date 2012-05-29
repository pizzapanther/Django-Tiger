
$(document).ready(function() {
  $('#id_stripe_name').removeAttr("name");
  $('#id_stripe_number').removeAttr("name");
  $('#id_stripe_cvc').removeAttr("name");
  $('#id_stripe_month').removeAttr("name");
  $('#id_stripe_year').removeAttr("name");
  
  $("#payment-form").submit(function(event) {
    $('input[type="submit"]').attr("disabled", "disabled");
    $('button[type="submit"]').attr("disabled", "disabled");
    
    Stripe.createToken({
      name: $('#id_stripe_name').val(),
      number: $('#id_stripe_number').val(),
      cvc: $('#id_stripe_cvc').val(),
      exp_month: $('#id_stripe_month').val(),
      exp_year: $('#id_stripe_year').val()
    }, stripeResponseHandler);

    // prevent the form from submitting with the default action
    return false;
  });
});

function stripeResponseHandler(status, response) {
  if (response.error) {
    alert(response.error.message);
    $('input[type="submit"]').removeAttr("disabled");
    $('button[type="submit"]').removeAttr("disabled");
  }
  
  else {
    $("#id_token").val(response['id']);
    $("#id_name").val(response.card.name);
    $("#id_last4").val(response.card.last4);
    $("#id_ctype").val(response.card.type);
    $("#id_exp_month").val(response.card.exp_month);
    $("#id_exp_year").val(response.card.exp_year);
    
    $("#payment-form").get(0).submit();
  }
}