paypal.Buttons({
    createOrder: function(data, actions) {
        return actions.order.create({
          purchase_units: [{
            amount: {
              value: '5000' // Remplacez par le montant approprié
            }
          }]
        });
    },
    onApprove: function(data, actions) {
        return actions.order.capture().then(function(details) {
          alert('Transaction completed by ' + details.payer.name.given_name);
          // Ajoutez toute autre logique après le paiement ici
        });
    }
}).render('#paypal-button-container');