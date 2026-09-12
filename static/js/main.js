const leftDropdown = document.querySelector('#left-dropdown');
const rightDropdown = document.querySelector('#right-dropdown');
const fromCurrency = document.querySelector('#from_currency');
const toCurrency = document.querySelector('#to_currency');





function swapFlag(selectedDropdown) {
     //Use currency code to retrieve the appropriate flag
     const currencyOptions = selectedDropdown.closest('.currency-options');
     fetch(`http://127.0.0.1:5555/currency-code/${selectedDropdown.value}`)
     .then(response => response.json())
     .then(result => currencyOptions.querySelector('img').src=`static/images/flags/${result['data']}`); 
}


// function getCurrencyDetails(currencyAmount){
      
// }




function swapCurrency(){
    //Swap to the currency details
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

leftDropdown.addEventListener('change', (e) => { swapFlag(e.currentTarget) });
rightDropdown.addEventListener('change', (e) => { swapFlag(e.currentTarget) });
fromCurrency.addEventListener('mouseout', (e) => { getCurrencyDetails(e.currentTarget) });
toCurrency.addEventListener('mouseout', (e) => { getCurrencyDetails(e.currentTarget) });
swapCurrency();
