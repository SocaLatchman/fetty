const leftDropdown = document.querySelector('#left-dropdown');
const rightDropdown = document.querySelector('#right-dropdown');
const fromCurrency = document.querySelector('#from_currency');
const toCurrency = document.querySelector('#to_currency');


leftDropdown.addEventListener('change', (e) => {
    console.log(e.currentTarget.value);
    if(rightDropdown.value != '') {
           //capture both values and send them to the fetch api      
    } else {

    }
});

rightDropdown.addEventListener('change', (e) => {
    console.log(e.currentTarget.value);
    if(leftDropdown.value != '') {
       //capture both values and send them to the fetch api  
    } else {
        
    }
});


function switchCurrency(){
    //Switch to the other currency and amount
    const currencySwitcherButton = document.querySelector('#currency-switcher');
    currencySwitcherButton.addEventListener('click', () => {
         let newFromCurrency = toCurrency.value;
         let newToCurrency = fromCurrency.value;
         let firstCountryOption = leftDropdown.value;
         let secondCountryOption = rightDropdown.value;
         fromCurrency.value = newFromCurrency;
         toCurrency.value = newToCurrency;
         leftDropdown.value = secondCountryOption;
         rightDropdown.value = firstCountryOption;
         let firstCountryFlag = document.querySelector('#second-flag');
         let secondCountryFlag = document.querySelector('#first-flag');
         let firstTempFlag = firstCountryFlag.src;
         firstCountryFlag.src = secondCountryFlag.src
         secondCountryFlag.src = firstTempFlag;  
    })

}

switchCurrency();
