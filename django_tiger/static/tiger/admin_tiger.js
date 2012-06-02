function refund_charge (url, cents) {
  var x = cents / 100;
  var amt = prompt("Enter Refund Amount", x.toFixed(2));
  
  if (amt != null && amt != "") {
    amt = parseFloat(amt) * 100;
    location.href = url + '?amt=' + amt;
  }
}