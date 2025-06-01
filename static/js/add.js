const form = document.getElementById('addLocForm');
const region = document.getElementById('region');
const hotelName = document.getElementById('name');
const address = document.getElementById('address');
const description = document.getElementById('description');

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

const validateInput = () => {
    const regionVal = region.value.trim();
    const nameVal = hotelName.value.trim();
    const addressVal = address.value.trim();
    const descVal = description.value.trim();

    if (regionVal === '') {
        setError(region, 'Region name is required');
    } else {
        setSuccess(region);
        var reg = true;
    }

    if (nameVal === '') {
        setError(hotelName, 'Hotel name is required');
    } else {
        setSuccess(hotelName);
        var hotel = true;
    }

    if (addressVal === '') {
        setError(address, 'Hotel address is required');
    } else {
        setSuccess(address);
        var add = true;
    }

    if (descVal === '') {
        setError(description, 'Description is required');
    } else {
        setSuccess(description);
        var desc = true;
    }

    if (reg && hotel && add && desc) {
        form.submit();
    }
};