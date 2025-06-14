const form = document.getElementById('addForm');
const checkin = document.getElementById('checkin');
const checkout = document.getElementById('checkout');

form.addEventListener('submit', e => {
    e.preventDefault();

    dateValidate();
});

const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success');
};

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};

const dateValidate = () => {
    const checkinDate = new Date(checkin.value);
    const checkoutDate = new Date(checkout.value);
    const today = new Date();

    if (checkinDate < today){
        setError(checkout, 'Check in cannot be before today');
    } else if (checkoutDate < today){
        setError(checkout, 'Check out cannot be before today');
    } else if (checkinDate > checkoutDate){
        setError(checkout, 'Check out date should be after check in date');
    } else{
        setSuccess(checkout);
        form.submit();
    }
};