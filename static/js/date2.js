const form = document.getElementById('updateForm');
const checkin = document.getElementById('checkin2').value;
const checckout = document.getElementById('checkout2').value;

form.addEventListener('submit', e => {
    e.preventDefault();

    dateValidate();
});

const setError = (element, message) => {
    const inputBox = element.parentElement;
    const errorDisplay = inputBox.querySelector('.error');

    errorDisplay.innerText = message;
    inputBox.classList.add('error');
    inputBox.classList.remove('success');
};

const setSuccess = element => {
    const inputBox = element.parentElement;
    const errorDisplay = inputBox.querySelector('.error');

    errorDisplay.innerText = '';
    inputBox.classList.add('success');
    inputBox.classList.remove('error');
};

const dateValidate = () => {
    const checkinDate = new Date(checkin.value);
    const checkoutDate = new Date(checckout.value);

    if (checkinDate > checkoutDate){
        setError(checkout, 'test');
    } else{
        setSuccess(checkout);
        form.submit();
    }
};