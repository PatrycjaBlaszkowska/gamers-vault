const stripe = Stripe('pk_test_51PvkztJdgATrWI66IpAkKfDBE31XA5FlQ0zoMb6peQEe5oDDoIWwydWcDRFHbsbEzwKQI7hln4NEec0BUQ4lI7Jk00kg2GeFNY');
const elements = stripe.elements();
const style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

const card = elements.create('card', {style: style});
card.mount('#card-element');
