const leftDropdown = document.querySelector('#left-dropdown');
const rightDropdown = document.querySelector('#right-dropdown');

leftDropdown.addEventListener('change', (e) => {
    console.log(e.currentTarget.value);
});

// leftDropdown.addEventListener('click', () => {

// });

rightDropdown.addEventListener('change', (e) => {
    console.log(e.currentTarget.value);
});

