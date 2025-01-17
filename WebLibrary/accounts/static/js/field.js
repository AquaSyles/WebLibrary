const textFields = document.querySelectorAll('input');
textFields.forEach(function(field) {
    field.addEventListener('keyup', increaseDarkness);
});

function increaseDarkness() {
    const button = document.querySelector('button[type="submit"]');
    filledNumber = getFilledNumber()
    
    const style1 = '#a3c9f1';
    const style2 = '#4491e3';
    const style3 = '#154f8c';

    if (filledNumber == 0) {
        button.style.background = style1;
    }

    if (filledNumber == 1) {
        button.style.background = style2;
    } else {
        button.style.background = style3;
    }
}

function getFilledNumber() {
    const textFields = document.querySelectorAll('input');
    count = -1 // because of csrf token

    textFields.forEach(function(field) {
        if (field.value.length > 0) {
            count++;
        }
    })

    return count;
}