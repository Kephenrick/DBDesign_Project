const form = document.getElementById('registerForm');
const username = document.getElementById('username');
const phone = document.getElementById('phone');
const password = document.getElementById('password');

form.addEventListener('submit', e => {
    e.preventDefault();

    validateInput();
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

const isPhoneValid = phone => {
    const re = /^08\d{8,11}$/;
    return re.test(String(phone).toLowerCase());
}

const validateInput = () => {
    const usernameVal = username.value.trim();
    const phoneVal = phone.value.trim();
    const passVal = password.value.trim();

    if (usernameVal === '') {
        setError(username, 'Username is required');
    } else {
        setSuccess(username);
        var user = true;
    }

    if (phoneVal === '') {
        setError(phone, 'Phone number is required');
    } else if (!isPhoneValid(phoneVal)) {
        setError(phone, 'Invalid phone number');
    } else {
        setSuccess(phone);
        var pho = true;
    }

    if (passVal === '') {
        setError(password, 'Password is required');
    } else if (passVal.length < 5) {
        setError(password, 'Password must be at least 5 characters long');
    } else {
        setSuccess(password);
        var pas = true;
    }

    if (user && pho && pas) {
        form.submit();
    }
};