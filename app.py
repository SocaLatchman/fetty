from flask import Flask, render_template
from dotenv import load_dotenv
from decimal import Decimal
import os, random, requests

load_dotenv('.env')
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') 


def get_random_image():
    '''
    Get all the images from a directory, iterate over them and if its a
    hidden file skip it. If its not, append it the file name to a list
    and return a random item from the list.
    '''
    image_list = []
    img_dir = os.getcwd() + "/static/images/giphy"
    with os.scandir(img_dir) as images:
        for image in images:
            if image.name.startswith('.'):
                continue
            else:
                image_list.append(image.name)
    return random.choice(image_list)


def get_country_data():
    '''Retrieve data by their currency codes '''
    result = []
    countries = [
        {"currency_code": "AED", "country": "United Arab Emirates", "flag": "uae.png"},
        {"currency_code": "AFN", "country": "Afghanistan", "flag": "afghanistan.png"},
        {"currency_code": "ALL", "country": "Albania", "flag": "albania.png"},
        {"currency_code": "AMD", "country": "Armenia", "flag": "armenia.png"},
        {"currency_code": "ANG", "country": "Curaçao", "flag": "curacao.png"},
        {"currency_code": "AOA", "country": "Angola", "flag": "angola.png"},
        {"currency_code": "ARS", "country": "Argentina", "flag": "argentina.png"},
        {"currency_code": "AUD", "country": "Australia", "flag": "australia.png"},
        {"currency_code": "AWG", "country": "Aruba", "flag": "aruba.png"},
        {"currency_code": "AZN", "country": "Azerbaijan", "flag": "azerbaijan.png"},
        {"currency_code": "BAM", "country": "Bosnia and Herzegovina", "flag": "bosnia-herzegovonia.png"},
        {"currency_code": "BBD", "country": "Barbados", "flag": "barbados.png"},
        {"currency_code": "BDT", "country": "Bangladesh", "flag": "bangladesh.png"},
        {"currency_code": "BGN", "country": "Bulgaria", "flag": "bulgaria.png"},
        {"currency_code": "BHD", "country": "Bahrain", "flag": "bahrain.png"},
        {"currency_code": "BIF", "country": "Burundi", "flag": "burundi.png"},
        {"currency_code": "BMD", "country": "Bermuda", "flag": "bermuda.png"},
        {"currency_code": "BND", "country": "Brunei", "flag": "brunei.png"},
        {"currency_code": "BOB", "country": "Bolivia", "flag": "bolivia.png"},
        {"currency_code": "BRL", "country": "Brazil", "flag": "brazil.png"},
        {"currency_code": "BSD", "country": "Bahamas", "flag": "bahamas.png"},
        {"currency_code": "BTN", "country": "Bhutan", "flag": "bhutan.png"},
        {"currency_code": "BWP", "country": "Botswana", "flag": "botswana.png"},
        {"currency_code": "BYN", "country": "Belarus", "flag": "belarus.png"},
        {"currency_code": "BZD", "country": "Belize", "flag": "belize.png"},
        {"currency_code": "CAD", "country": "Canada", "flag": "canada.png"},
        {"currency_code": "CDF", "country": "Congo (Democratic Republic)", "flag": "dr-congo.png"},
        {"currency_code": "CHF", "country": "Switzerland", "flag": "switzerland.png"},
        {"currency_code": "CLP", "country": "Chile", "flag": "chile.png"},
        {"currency_code": "CNH", "country": "China (Offshore)", "flag": "china.png"},
        {"currency_code": "CNY", "country": "China", "flag": "china.png"},
        {"currency_code": "COP", "country": "Colombia", "flag": "colombia.png"},
        {"currency_code": "CRC", "country": "Costa Rica", "flag": "costa-rica.png"},
        {"currency_code": "CUC", "country": "Cuba (Convertible)", "flag": "cuba.png"},
        {"currency_code": "CUP", "country": "Cuba", "flag": "cuba.png"},
        {"currency_code": "CVE", "country": "Cape Verde", "flag": "cape-verde.png"},
        {"currency_code": "CZK", "country": "Czech Republic", "flag": "czech-republic.png"},
        {"currency_code": "DJF", "country": "Djibouti", "flag": "djibouti.png"},
        {"currency_code": "DKK", "country": "Denmark", "flag": "denmark.png"},
        {"currency_code": "DOP", "country": "Dominican Republic", "flag": "dominican-republic.png"},
        {"currency_code": "DZD", "country": "Algeria", "flag": "algeria.png"},
        {"currency_code": "EGP", "country": "Egypt", "flag": "egypt.png"},
        {"currency_code": "ERN", "country": "Eritrea", "flag": "eritrea.png"},
        {"currency_code": "ETB", "country": "Ethiopia", "flag": "ethiopia.png"},
        {"currency_code": "EUR", "country": "Eurozone", "flag": "eu.png"},
        {"currency_code": "FJD", "country": "Fiji", "flag": "fiji-islands.png"},
        {"currency_code": "GBP", "country": "United Kingdom", "flag": "uk.png"},
        {"currency_code": "GEL", "country": "Georgia", "flag": "georgia.png"},
        {"currency_code": "GHS", "country": "Ghana", "flag": "ghana.png"},
        {"currency_code": "GMD", "country": "Gambia", "flag": "gambia.png"},
        {"currency_code": "GNF", "country": "Guinea", "flag": "guinea.png"},
        {"currency_code": "GTQ", "country": "Guatemala", "flag": "guatemala.png"},
        {"currency_code": "GYD", "country": "Guyana", "flag": "guyana.png"},
        {"currency_code": "HKD", "country": "Hong Kong", "flag": "hk.png"},
        {"currency_code": "HNL", "country": "Honduras", "flag": "honduras.png"},
        {"currency_code": "HTG", "country": "Haiti", "flag": "haiti.png"},
        {"currency_code": "HUF", "country": "Hungary", "flag": "hungary.png"},
        {"currency_code": "IDR", "country": "Indonesia", "flag": "indonesia.png"},
        {"currency_code": "ILS", "country": "Israel", "flag": "israel.png"},
        {"currency_code": "INR", "country": "India", "flag": "india.png"},
        {"currency_code": "IQD", "country": "Iraq", "flag": "iraq.png"},
        {"currency_code": "IRR", "country": "Iran", "flag": "iran.png"},
        {"currency_code": "ISK", "country": "Iceland", "flag": "iceland.png"},
        {"currency_code": "JMD", "country": "Jamaica", "flag": "jamaica.png"},
        {"currency_code": "JOD", "country": "Jordan", "flag": "jordan.png"},
        {"currency_code": "JPY", "country": "Japan", "flag": "japan.png"},
        {"currency_code": "KES", "country": "Kenya", "flag": "kenya.png"},
        {"currency_code": "KGS", "country": "Kyrgyzstan", "flag": "kyrgyzstan.png"},
        {"currency_code": "KHR", "country": "Cambodia", "flag": "cambodia.png"},
        {"currency_code": "KMF", "country": "Comoros", "flag": "comoros.png"},
        {"currency_code": "KPW", "country": "North Korea", "flag": "north-korea.png"},
        {"currency_code": "KRW", "country": "South Korea", "flag": "south-korea.png"},
        {"currency_code": "KWD", "country": "Kuwait", "flag": "kuwait.png"},
        {"currency_code": "KZT", "country": "Kazakhstan", "flag": "kazakhstan.png"},
        {"currency_code": "LAK", "country": "Laos", "flag": "laos.png"},
        {"currency_code": "LBP", "country": "Lebanon", "flag": "lebanon.png"},
        {"currency_code": "LKR", "country": "Sri Lanka", "flag": "sri-lanka.png"},
        {"currency_code": "LRD", "country": "Liberia", "flag": "liberia.png"},
        {"currency_code": "LSL", "country": "Lesotho", "flag": "lesotho.png"},
        {"currency_code": "LYD", "country": "Libya", "flag": "libya.png"},
        {"currency_code": "MAD", "country": "Morocco", "flag": "morocco.png"},
        {"currency_code": "MDL", "country": "Moldova", "flag": "moldova.png"},
        {"currency_code": "MGA", "country": "Madagascar", "flag": "madagascar.png"},
        {"currency_code": "MKD", "country": "North Macedonia", "flag": "macedonia.png"},
        {"currency_code": "MMK", "country": "Myanmar", "flag": "myanmar.png"},
        {"currency_code": "MNT", "country": "Mongolia", "flag": "mongolia.png"},
        {"currency_code": "MOP", "country": "Macau", "flag": "macau.png"},
        {"currency_code": "MRU", "country": "Mauritania", "flag": "mauritania.png"},
        {"currency_code": "MUR", "country": "Mauritius", "flag": "mauritius.png"},
        {"currency_code": "MVR", "country": "Maldives", "flag": "maldives.png"},
        {"currency_code": "MWK", "country": "Malawi", "flag": "malawi.png"},
        {"currency_code": "MXN", "country": "Mexico", "flag": "mexico.png"},
        {"currency_code": "MYR", "country": "Malaysia", "flag": "malaysia.png"},
        {"currency_code": "MZN", "country": "Mozambique", "flag": "mozambique.png"},
        {"currency_code": "NAD", "country": "Namibia", "flag": "namibia.png"},
        {"currency_code": "NGN", "country": "Nigeria", "flag": "nigeria.png"},
        {"currency_code": "NIO", "country": "Nicaragua", "flag": "nicaragua.png"},
        {"currency_code": "NOK", "country": "Norway", "flag": "norway.png"},
        {"currency_code": "NPR", "country": "Nepal", "flag": "nepal.png"},
        {"currency_code": "NZD", "country": "New Zealand", "flag": "new-zealand.png"},
        {"currency_code": "OMR", "country": "Oman", "flag": "oman.png"},
        {"currency_code": "PAB", "country": "Panama", "flag": "panama.png"},
        {"currency_code": "PEN", "country": "Peru", "flag": "peru.png"},
        {"currency_code": "PGK", "country": "Papua New Guinea", "flag": "papua-new-guinea.png"},
        {"currency_code": "PHP", "country": "Philippines", "flag": "philippines.png"},
        {"currency_code": "PKR", "country": "Pakistan", "flag": "pakistan.png"},
        {"currency_code": "PLN", "country": "Poland", "flag": "poland.png"},
        {"currency_code": "PYG", "country": "Paraguay", "flag": "paraguay.png"},
        {"currency_code": "QAR", "country": "Qatar", "flag": "qatar.png"},
        {"currency_code": "RON", "country": "Romania", "flag": "romania.png"},
        {"currency_code": "RSD", "country": "Serbia", "flag": "serbia.png"},
        {"currency_code": "RUB", "country": "Russia", "flag": "russia.png"},
        {"currency_code": "RWF", "country": "Rwanda", "flag": "rwanda.png"},
        {"currency_code": "SAR", "country": "Saudi Arabia", "flag": "saudi-arabia.png"},
        {"currency_code": "SBD", "country": "Solomon Islands", "flag": "soloman-islands.png"},
        {"currency_code": "SCR", "country": "Seychelles", "flag": "seychelles.png"},
        {"currency_code": "SDG", "country": "Sudan", "flag": "sudan.png"},
        {"currency_code": "SEK", "country": "Sweden", "flag": "sweden.png"},
        {"currency_code": "SGD", "country": "Singapore", "flag": "singapore.png"},
        {"currency_code": "SHP", "country": "Saint Helena", "flag": ""},
        {"currency_code": "SLL", "country": "Sierra Leone", "flag": "sierra-leone.png"},
        {"currency_code": "SOS", "country": "Somalia", "flag": "somalia.png"},
        {"currency_code": "SRD", "country": "Suriname", "flag": "suriname.png"},
        {"currency_code": "SSP", "country": "South Sudan", "flag": "south-sudan.png"},
        {"currency_code": "STD", "country": "Sao Tome and Principe", "flag": "sao-tome.png"},
        {"currency_code": "SVC", "country": "El Salvador", "flag": "el-salvador.png"},
        {"currency_code": "SYP", "country": "Syria", "flag": "syria.png"},
        {"currency_code": "SZL", "country": "Eswatini", "flag": "eswatini.png"},
        {"currency_code": "THB", "country": "Thailand", "flag": "thailand.png"},
        {"currency_code": "TJS", "country": "Tajikistan", "flag": "tajikistan.png"},
        {"currency_code": "TMT", "country": "Turkmenistan", "flag": "turkmenistan.png"},
        {"currency_code": "TND", "country": "Tunisia", "flag": "tunisia.png"},
        {"currency_code": "TOP", "country": "Tonga", "flag": "tonga.png"},
        {"currency_code": "TRY", "country": "Turkey", "flag": "turkey.png"},
        {"currency_code": "TTD", "country": "Trinidad and Tobago", "flag": "trinidad.png"},
        {"currency_code": "TWD", "country": "Taiwan", "flag": "taiwan.png"},
        {"currency_code": "TZS", "country": "Tanzania", "flag": "tanzania.png"},
        {"currency_code": "UAH", "country": "Ukraine", "flag": "ukraine.png"},
        {"currency_code": "UGX", "country": "Uganda", "flag": "uganda.png"},
        {"currency_code": "USD", "country": "United States", "flag": "united-states-of-america.png"},
        {"currency_code": "UYU", "country": "Uruguay", "flag": "uruguay.png"},
        {"currency_code": "UZS", "country": "Uzbekistan", "flag": "uzbekistan.png"},
        {"currency_code": "VES", "country": "Venezuela", "flag": "venezuela.png"},
        {"currency_code": "VND", "country": "Vietnam", "flag": "vietnam.png"},
        {"currency_code": "VUV", "country": "Vanuatu", "flag": "vanuatu.png"},
        {"currency_code": "WST", "country": "Samoa", "flag": "samoa.png"},
        {"currency_code": "YER", "country": "Yemen", "flag": "yemen.png"},
        {"currency_code": "ZAR", "country": "South Africa", "flag": "south-africa.png"},
        {"currency_code": "ZMW", "country": "Zambia", "flag": "zambia.png"},
        {"currency_code": "ZWG", "country": "Zimbabwe (ZiG)", "flag": "zimbabwe.png"},
        {"currency_code": "ZWL", "country": "Zimbabwe", "flag": "zimbabwe.png"}
    ]
    for country in countries:
        result.append(country)
    return result

def currency_rate_quote(from_currency_code, to_country_code):
    currency_api = requests.get(f"https://api.frankfurter.dev/v2/rate/{from_currency_code}/{to_country_code}")
    return currency_api.json()




@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', random_image=get_random_image(), countries = get_country_data())



if __name__ == '__main__':
    app.run(debug=True, port=5555)
