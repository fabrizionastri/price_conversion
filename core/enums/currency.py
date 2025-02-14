from ..models.flexup_enum import FlexUpEnum
from django.utils.translation import gettext_lazy as _

class Currency(FlexUpEnum):
    label: str                  # label used in the dropdown menu
    short_name: str             # label used in the dropdown menu
    symbol: str                 # symbol used when displaying the prices or amounts
    unique_symbol : str         # in any situations where multiple currencies are displayed together, using this symbol will help to differentiate the currencies
    alternative_symbol: str     # alternative symbol used when displaying the prices or amounts
    ison: str                   # ISO number, might be useful for some API calls
    is_active: str              # whether the currency is active or not
    since_year: str             # since when the currency is active
    until_year: str             # until when the currency is active

    # name=  value,  label,                               short_name,   symbol,   unique_symbol,  alternative_symbol,  ison,   is_active,  since_year,  until_year
    AFN   =  'AFN',  _('Afghani'),                        _('afghani'),    '؋',      '؋',            '',                  '971',  'True',     '',          ''
    DZD   =  'DZD',  _('Algerian Dinar'),                 _('dinar'),      'DA',     'DA',           '',                  '12',   'True',     '',          ''
    ARS   =  'ARS',  _('Argentine peso'),                 _('peso'),       '$',      '$Ar',          '',                  '32',   'True',     '',          ''
    AMD   =  'AMD',  _('Armenian Dram'),                  _('dram'),       '֏',      '֏',            '',                  '51',   'True',     '',          ''
    AWG   =  'AWG',  _('Aruban florin'),                  _('florin'),     'ƒ',      'Afl',          '',                  '533',  'True',     '',          ''
    AUD   =  'AUD',  _('Australian dollar'),              _('dollar'),     '$',      '$Au',          '',                  '36',   'True',     '',          ''
    AZN   =  'AZN',  _('Azerbaijan Manat'),               _('manat'),      '₼',      '₼',            '',                  '944',  'True',     '',          ''
    BSD   =  'BSD',  _('Bahamian dollar'),                _('dollar'),     '$',      '$BS',          '',                  '44',   'True',     '',          ''
    BHD   =  'BHD',  _('Bahraini Dinar'),                 _('dinar'),      'BD',     'BD',           '',                  '48',   'True',     '',          ''
    THB   =  'THB',  _('Baht'),                           _('baht'),       '฿',      '฿',            '',                  '764',  'True',     '',          ''
    PAB   =  'PAB',  _('Balboa'),                         _('balboa'),     'B/.',    'B/.',          '',                  '590',  'True',     '',          ''
    BBD   =  'BBD',  _('Barbados Dollar'),                _('dollar'),     '$',      '$Bds',         '',                  '52',   'True',     '',          ''
    BYN   =  'BYN',  _('Belarusian ruble'),               _('ruble'),      'Rbl',    'Rbl',          'Br',                '933',  'True',     '',          ''
    BZD   =  'BZD',  _('Belize Dollar'),                  _('dollar'),     'BZ$',    'BZ$',          '',                  '84',   'True',     '',          ''
    BMD   =  'BMD',  _('Bermudian dollar'),               _('dollar'),     '$',      '$BM',          '',                  '60',   'True',     '',          ''
    BOB   =  'BOB',  _('Boliviano'),                      _('boliviano'),  '$b',     '$b',           'Bs',                '68',   'True',     '',          ''
    BRL   =  'BRL',  _('Brazilian real'),                 _('real'),       'R$',     'R$',           '',                  '986',  'True',     '',          ''
    BND   =  'BND',  _('Brunei dollar'),                  _('dollar'),     '$',      '$BN',          '',                  '96',   'True',     '',          ''
    BGN   =  'BGN',  _('Bulgarian lev'),                  _('lev'),        'lev',    'ле',           'лв',                '975',  'True',     '',          ''
    BIF   =  'BIF',  _('Burundi Franc'),                  _('franc'),      'Fr',     'FrBI',         '',                  '108',  'True',     '',          ''
    CVE   =  'CVE',  _('Cabo Verde Escudo'),              _('escudo'),     '$',      '$CV',          '',                  '132',  'True',     '',          ''
    CAD   =  'CAD',  _('Canadian dollar'),                _('dollar'),     '$',      '$CA',          '',                  '124',  'True',     '',          ''
    KYD   =  'KYD',  _('Cayman Islands Dollar'),          _('dollar'),     '$',      '$KY',          '',                  '136',  'True',     '',          ''
    XOF   =  'XOF',  _('CFA Franc BCEAO'),                _('franc'),      'Fr',     'Fr(XOF)',      '',                  '952',  'True',     '',          ''
    XAF   =  'XAF',  _('CFA Franc BEAC'),                 _('franc'),      'Fr',     'Fr(XAF)',      '',                  '950',  'True',     '',          ''
    XPF   =  'XPF',  _('CFP Franc'),                      _('franc'),      'Fr',     'FrXP',         '',                  '953',  'True',     '',          ''
    CLP   =  'CLP',  _('Chilean peso'),                   _('peso'),       '$',      '$CI',          '',                  '152',  'True',     '',          ''
    CNY   =  'CNY',  _('Chinese Yuan'),                   _('Yuan'),       '¥',      '¥',            'CN¥',               '156',  'True',     '',          ''
    COP   =  'COP',  _('Colombian peso'),                 _('peso'),       '$',      '$CO',          '',                  '170',  'True',     '',          ''
    KMF   =  'KMF',  _('Comorian Franc'),                 _('franc'),      'Fr',     'FrKM',         '',                  '174',  'True',     '',          ''
    CDF   =  'CDF',  _('Congolese franc'),                _('franc'),      'Fr',     'FrCD',         '',                  '976',  'True',     '',          ''
    BAM   =  'BAM',  _('Convertible Mark'),               _('mark'),       'KM',     'KM',           '',                  '977',  'True',     '',          ''
    NIO   =  'NIO',  _('Cordoba Oro'),                    _('oro'),        'C$',     'C$',           '',                  '558',  'True',     '',          ''
    CRC   =  'CRC',  _('Costa Rican Colon'),              _('colon'),      '₡',      '₡',            '',                  '188',  'True',     '',          ''
    HRK   =  'HRK',  _('Croatia Kuna'),                   _('kuna'),       'kn',     'kn',           '',                  '191',  'True',     '',          ''
    CUP   =  'CUP',  _('Cuban peso'),                     _('peso'),       '₱',      '₱CU',          '',                  '192',  'True',     '',          ''
    CZK   =  'CZK',  _('Czech koruna'),                   _('koruna'),     'Kč',     'Kč',           '',                  '203',  'True',     '',          ''
    GMD   =  'GMD',  _('Dalasi'),                         _('dalasi'),     'D',      'D',            '',                  '270',  'True',     '',          ''
    DKK   =  'DKK',  _('Danish krone'),                   _('krone'),      'kr',     'kr',           '',                  '208',  'True',     '',          ''
    MKD   =  'MKD',  _('Denar'),                          _('denar'),      'ден',    'ден',          '',                  '807',  'True',     '',          ''
    DJF   =  'DJF',  _('Djibouti Franc'),                 _('franc'),      'Fr',     'FrDJ',         '',                  '262',  'True',     '',          ''
    STN   =  'STN',  _('Dobra'),                          _('dobra'),      'Db',     'Db',           '',                  '930',  'True',     '',          ''
    DOP   =  'DOP',  _('Dominican peso'),                 _('peso'),       'RD$',    'RD$',          '',                  '214',  'True',     '',          ''
    VND   =  'VND',  _('Dong'),                           _('dong'),       '₫',      '₫',            '',                  '704',  'True',     '',          ''
    XCD   =  'XCD',  _('East Caribbean Dollar'),          _('dollar'),     '$',      '$XC',          '',                  '951',  'True',     '',          ''
    EGP   =  'EGP',  _('Egyptian pound'),                 _('pound'),      '£',      '£EG',          '',                  '818',  'True',     '',          ''
    SVC   =  'SVC',  _('El Salvador Colon'),              _('colon'),      '$',      '$SV',          '',                  '222',  'True',     '',          ''
    ETB   =  'ETB',  _('Ethiopian Birr'),                 _('birr'),       'Br',     'Br',           '',                  '230',  'True',     '',          ''
    EUR   =  'EUR',  _('Euro'),                           _('euro'),       '€',      '€',            '',                  '978',  'True',     '',          ''
    FKP   =  'FKP',  _('Falkland Islands pound'),         _('pound'),      '£',      '£FK',          '',                  '238',  'True',     '',          ''
    FJD   =  'FJD',  _('Fiji Dollar'),                    _('dollar'),     '$',      '$FJ',          '',                  '242',  'True',     '',          ''
    SLL   =  'SLL',  _('First Leone'),                    _('leone'),      'Le',     'Le(SLL)',      '',                  '925',  'True',     '',          ''
    HUF   =  'HUF',  _('Forint'),                         _('forint'),     'Ft',     'Ft',           '',                  '348',  'True',     '',          ''
    GHS   =  'GHS',  _('Ghana Cedi'),                     _('cedi'),       '¢',      '¢',            '',                  '936',  'True',     '',          ''
    GIP   =  'GIP',  _('Gibraltar Pound'),                _('pound'),      '£',      '£GI',          '',                  '292',  'True',     '',          ''
    HTG   =  'HTG',  _('Gourde'),                         _('gourde'),     'G',      'G',            '',                  '332',  'True',     '',          ''
    PYG   =  'PYG',  _('Guarani'),                        _('guarani'),    'Gs',     'Gs',           '',                  '600',  'True',     '',          ''
    GGP   =  'GGP',  _('Guernsey Pound'),                 _('pound'),      '£',      '£G',           '',                  '',     'True',     '',          ''
    GNF   =  'GNF',  _('Guinean Franc'),                  _('franc'),      'Fr',     'FrGN',         '',                  '324',  'True',     '',          ''
    GYD   =  'GYD',  _('Guyana Dollar'),                  _('dollar'),     '$',      '$G',           '',                  '328',  'True',     '',          ''
    HKD   =  'HKD',  _('Hong Kong Dollar'),               _('dollar'),     '$',      '$HK',          '',                  '344',  'True',     '',          ''
    UAH   =  'UAH',  _('Hryvnia'),                        _('hryvnia'),    '₴',      '₴',            '',                  '980',  'True',     '',          ''
    ISK   =  'ISK',  _('Iceland Krona'),                  _('krona'),      'kr',     'krIS',         '',                  '352',  'True',     '',          ''
    INR   =  'INR',  _('Indian rupee'),                   _('rupee'),      '₹',      '₹',            '',                  '356',  'True',     '',          ''
    IRR   =  'IRR',  _('Iranian rial'),                   _('rial'),       '﷼',      '﷼IR',          '',                  '364',  'True',     '',          ''
    IQD   =  'IQD',  _('Iraqi Dinar'),                    _('dinar'),      'ID',     'ID',           '',                  '368',  'True',     '',          ''
    IMP   =  'IMP',  _('Isle of Man Pound'),              _('pound'),      '£',      '£IM',          '',                  '',     'True',     '',          ''
    JMD   =  'JMD',  _('Jamaican dollar'),                _('dollar'),     'J$',     'J$',           '',                  '388',  'True',     '',          ''
    JEP   =  'JEP',  _('Jersey Pound'),                   _('pound'),      '£',      '£JE',          '',                  '',     'True',     '',          ''
    JOD   =  'JOD',  _('Jordanian Dinar'),                _('dinar'),      'JD',     'JD',           '',                  '400',  'True',     '',          ''
    KES   =  'KES',  _('Kenyan Shilling'),                _('shilling'),   'Sh',     'KSh',          '',                  '404',  'True',     '',          ''
    PGK   =  'PGK',  _('Kina'),                           _('kina'),       'K',      'Ki',           '',                  '598',  'True',     '',          ''
    KWD   =  'KWD',  _('Kuwaiti Dinar'),                  _('dinar'),      'KD',     'KD',           '',                  '414',  'True',     '',          ''
    AOA   =  'AOA',  _('Kwanza'),                         _('kwanza'),     'Kz',     'Kz',           '',                  '973',  'True',     '',          ''
    MMK   =  'MMK',  _('Kyat'),                           _('kyat'),       'K',      'Ky',           '',                  '104',  'True',     '',          ''
    LAK   =  'LAK',  _('Lao kip'),                        _('kip'),        '₭',      '₭',            '',                  '418',  'True',     '',          ''
    GEL   =  'GEL',  _('Lari'),                           _('lari'),       '₾',      '₾',            '',                  '981',  'True',     '',          ''
    LBP   =  'LBP',  _('Lebanese pound'),                 _('pound'),      '£',      '£LB',          'LL',                '422',  'True',     '',          ''
    ALL   =  'ALL',  _('Lek'),                            _('lek'),        'Lek',    'Lek',          '',                  '8',    'True',     '',          ''
    HNL   =  'HNL',  _('Lempira'),                        _('lempira'),    'L',      'L',            '',                  '340',  'True',     '',          ''
    LRD   =  'LRD',  _('Liberian dollar'),                _('dollar'),     '$',      '$L',           '',                  '430',  'True',     '',          ''
    LYD   =  'LYD',  _('Libyan Dinar'),                   _('dinar'),      'LD',     'LD',           '',                  '434',  'True',     '',          ''
    SZL   =  'SZL',  _('Lilangeni'),                      _('lilangeni'),  'L',      'Le',           '',                  '748',  'True',     '',          ''
    LSL   =  'LSL',  _('Loti'),                           _('loti'),       'L',      'Lm',           '',                  '426',  'True',     '',          ''
    MGA   =  'MGA',  _('Malagasy Ariary'),                _('ariary'),     'Ar',     'Ar',           '',                  '969',  'True',     '',          ''
    MWK   =  'MWK',  _('Malawi Kwacha'),                  _('kwacha'),     'K',      'MK',           '',                  '454',  'True',     '',          ''
    MYR   =  'MYR',  _('Malaysian ringgit'),              _('ringgit'),    'RM',     'RM',           '',                  '458',  'True',     '',          ''
    MUR   =  'MUR',  _('Mauritius Rupee'),                _('rupee'),      '₨',      'MRs',          '',                  '480',  'True',     '',          ''
    MXN   =  'MXN',  _('Mexican peso'),                   _('peso'),       '$',      '$MX',          '',                  '484',  'True',     '',          ''
    MDL   =  'MDL',  _('Moldovan Leu'),                   _('leu'),        'Leu',    'Leu',          '',                  '498',  'True',     '',          ''
    MAD   =  'MAD',  _('Moroccan Dirham'),                _('dirham'),     'DH',     'Dh(MA)',       '.د.م',              '504',  'True',     '',          ''
    MZN   =  'MZN',  _('Mozambique Metical'),             _('metical'),    'MT',     'MT',           '',                  '943',  'True',     '',          ''
    BOV   =  'BOV',  _('Mvdol'),                          _('Mvdol'),      'Mvdol',  'Mvdol',        '',                  '984',  'True',     '',          ''
    NGN   =  'NGN',  _('Naira'),                          _('naira'),      '₦',      '₦',            '',                  '566',  'True',     '',          ''
    ERN   =  'ERN',  _('Nakfa'),                          _('nakfa'),      'Nkf',    'Nkf',          '',                  '232',  'True',     '',          ''
    NAD   =  'NAD',  _('Namibia Dollar'),                 _('dollar'),     '$',      '$N',           '',                  '516',  'True',     '',          ''
    NPR   =  'NPR',  _('Nepalese rupee'),                 _('rupee'),      'रू',     'NRs',          '₨',                 '524',  'True',     '',          ''
    ANG   =  'ANG',  _('Netherlands Antillean guilder'),  _('guilder'),    'ƒ',      'NAƒ',          '',                  '532',  'True',     '',          ''
    ILS   =  'ILS',  _('New Israeli Sheqel'),             _('sheqel'),     '₪',      '₪',            '',                  '376',  'True',     '',          ''
    TWD   =  'TWD',  _('New Taiwan dollar'),              _('dollar'),     'NT$',    'NT$',          '',                  '901',  'True',     '',          ''
    NZD   =  'NZD',  _('New Zealand Dollar'),             _('dollar'),     '$',      '$NZ',          '',                  '554',  'True',     '',          ''
    BTN   =  'BTN',  _('Ngultrum'),                       _('ngultrum'),   'Nu',     'Nu',           '',                  '64',   'True',     '',          ''
    KPW   =  'KPW',  _('North Korean won'),               _('won'),        '₩',      '₩NK',          '',                  '408',  'True',     '',          ''
    NOK   =  'NOK',  _('Norwegian krone'),                _('krone'),      'kr',     'krNO',         '',                  '578',  'True',     '',          ''
    MRU   =  'MRU',  _('Ouguiya'),                        _('ouguiya'),    'UM',     'UM',           '',                  '929',  'True',     '',          ''
    TOP   =  'TOP',  _('Pa`anga'),                        _('pa`anga'),    'T$',     'T$',           '',                  '776',  'True',     '',          ''
    PKR   =  'PKR',  _('Pakistan Rupee'),                 _('rupee'),      '₨',      'PRs',          '',                  '586',  'True',     '',          ''
    MOP   =  'MOP',  _('Pataca'),                         _('pataca'),     'MOP$',   'MOP$',         '',                  '446',  'True',     '',          ''
    UYU   =  'UYU',  _('Peso Uruguayo'),                  _('uruguayo'),   '$U',     '$U',           '',                  '858',  'True',     '',          ''
    PHP   =  'PHP',  _('Philippine peso'),                _('peso'),       '₱',      '₱PH',          '',                  '608',  'True',     '',          ''
    PLN   =  'PLN',  _('Polish Złoty'),                   _('Złoty'),      'zł',     'zł',           'PLN',               '985',  'True',     '',          ''
    GBP   =  'GBP',  _('Pound Sterling'),                 _('sterling'),   '£',      '£GB',          '',                  '826',  'True',     '',          ''
    BWP   =  'BWP',  _('Pula'),                           _('pula'),       'P',      'P',            '',                  '72',   'True',     '',          ''
    QAR   =  'QAR',  _('Qatari Rial'),                    _('rial'),       '﷼',      '﷼QA',          '',                  '634',  'True',     '',          ''
    GTQ   =  'GTQ',  _('Quetzal'),                        _('quetzal'),    'Q',      'Q',            '',                  '320',  'True',     '',          ''
    ZAR   =  'ZAR',  _('Rand'),                           _('rand'),       'R',      'R',            '',                  '710',  'True',     '',          ''
    OMR   =  'OMR',  _('Rial Omani'),                     _('omani'),      '﷼',      '﷼OM',          '',                  '512',  'True',     '',          ''
    KHR   =  'KHR',  _('Riel'),                           _('riel'),       '៛',      '៛',            '',                  '116',  'True',     '',          ''
    RON   =  'RON',  _('Romanian leu'),                   _('leu'),        'lei',    'lei',          '',                  '946',  'True',     '',          ''
    MVR   =  'MVR',  _('Rufiyaa'),                        _('rufiyaa'),    'Rf',     'Rf',           '',                  '462',  'True',     '',          ''
    IDR   =  'IDR',  _('Rupiah'),                         _('rupiah'),     'Rp',     'Rp',           '',                  '360',  'True',     '',          ''
    RUB   =  'RUB',  _('Russian ruble'),                  _('ruble'),      '₽',      '₽',            '',                  '643',  'True',     '',          ''
    RWF   =  'RWF',  _('Rwanda Franc'),                   _('franc'),      'Fr',     'FrRW',         '',                  '646',  'True',     '',          ''
    SHP   =  'SHP',  _('Saint Helena Pound'),             _('pound'),      '£',      '£SH',          '',                  '654',  'True',     '',          ''
    SAR   =  'SAR',  _('Saudi riyal'),                    _('riyal'),      '﷼',      '﷼SA',          '',                  '682',  'True',     '',          ''
    SLE   =  'SLE',  _('Second Leone'),                   _('leone'),      'Le',     'Le(SLE)',      '',                  '925',  'True',     '',          ''
    RSD   =  'RSD',  _('Serbian dinar'),                  _('dinar'),      'Дин.',   'Дин.',         '',                  '941',  'True',     '',          ''
    SCR   =  'SCR',  _('Seychelles Rupee'),               _('rupee'),      '₨',      'SRs',          '',                  '690',  'True',     '',          ''
    SGD   =  'SGD',  _('Singapore Dollar'),               _('dollar'),     '$',      '$S',           '',                  '702',  'True',     '',          ''
    PEN   =  'PEN',  _('Sol'),                            _('sol'),        'S/.',    'S/.',          '',                  '604',  'True',     '',          ''
    SBD   =  'SBD',  _('Solomon Islands Dollar'),         _('dollar'),     '$',      '$SI',          '',                  '90',   'True',     '',          ''
    KGS   =  'KGS',  _('Som'),                            _('som'),        'som',    'лвKGS',        'лв',                '417',  'True',     '',          ''
    SOS   =  'SOS',  _('Somali shilling'),                _('shilling'),   'S',      'Sh.So.',       '',                  '706',  'True',     '',          ''
    TJS   =  'TJS',  _('Somoni'),                         _('somoni'),     'SM',     'SM',           '',                  '972',  'True',     '',          ''
    SSP   =  'SSP',  _('South Sudanese Pound'),           _('pound'),      '£',      '£SSP',         '',                  '728',  'True',     '',          ''
    LKR   =  'LKR',  _('Sri Lanka Rupee'),                _('rupee'),      'රු',     'SLRs',         '₨',                 '144',  'True',     '',          ''
    SDG   =  'SDG',  _('Sudanese Pound'),                 _('pound'),      'LS',     'LS',           '',                  '938',  'True',     '',          ''
    SRD   =  'SRD',  _('Surinam Dollar'),                 _('dollar'),     '$',      '$SR',          '',                  '968',  'True',     '',          ''
    SEK   =  'SEK',  _('Swedish krona'),                  _('krona'),      'kr',     'krSE',         '',                  '752',  'True',     '',          ''
    CHF   =  'CHF',  _('Swiss franc'),                    _('franc'),      'CHF',    'CHF',          '',                  '756',  'True',     '',          ''
    SYP   =  'SYP',  _('Syrian pound'),                   _('pound'),      '£',      '£SY',          'LS',                '760',  'True',     '',          ''
    BDT   =  'BDT',  _('Taka'),                           _('taka'),       '৳',      '৳',            '',                  '50',   'True',     '',          ''
    WST   =  'WST',  _('Tala'),                           _('tala'),       '$',      'WS$',          '',                  '882',  'True',     '',          ''
    TZS   =  'TZS',  _('Tanzanian Shilling'),             _('shilling'),   'Sh',     'TSh',          '',                  '834',  'True',     '',          ''
    KZT   =  'KZT',  _('Tenge'),                          _('tenge'),      'лв',     'лвKZT',        '',                  '398',  'True',     '',          ''
    TTD   =  'TTD',  _('Trinidad and Tobago Dollar'),     _('dollar'),     'TT$',    'TT$',          '',                  '780',  'True',     '',          ''
    MNT   =  'MNT',  _('Tugrik'),                         _('tugrik'),     '₮',      '₮',            '',                  '496',  'True',     '',          ''
    TND   =  'TND',  _('Tunisian Dinar'),                 _('dinar'),      'DT',     'DT',           '',                  '788',  'True',     '',          ''
    TRY   =  'TRY',  _('Turkish lira'),                   _('lira'),       '₺',      '₺',            '',                  '949',  'True',     '',          ''
    TMT   =  'TMT',  _('Turkmenistan New Manat'),         _('manat'),      'm',      'm',            '',                  '934',  'True',     '',          ''
    TVD   =  'TVD',  _('Tuvalu Dollar'),                  _('dollar'),     '$',      '$TV',          '',                  '',     'True',     '',          ''
    AED   =  'AED',  _('UAE Dirham'),                     _('dirham'),     'Dh',     'Dh(UAE)',      'د.إ',               '784',  'True',     '',          ''
    UGX   =  'UGX',  _('Uganda Shilling'),                _('shilling'),   'Sh',     'USh',          '',                  '800',  'True',     '',          ''
    USD   =  'USD',  _('US Dollar'),                      _('dollar'),     '$',      '$US',          '',                  '840',  'True',     '',          ''
    UZS   =  'UZS',  _('Uzbekistan Sum'),                 _('sum'),        'soum',   'лвUZS',        'лв',                '860',  'True',     '',          ''
    VUV   =  'VUV',  _('Vatu'),                           _('vatu'),       'VT',     'VT',           '',                  '548',  'True',     '',          ''
    VED   =  'VED',  _('Venezuela Bolívar Digital'),      _('bolívar'),    'Bs.D',   'Bs.D',         '',                  '926',  'True',     '2021',      ''
    VEF   =  'VEF',  _('Venezuela Bolívar Fuerte'),       _('bolívar'),    'Bs.F',   'Bs.F',         '',                  '',     'False',    '',          '2018'
    VES   =  'VES',  _('Venezuela Bolívar Soberano'),     _('bolívar'),    'Bs.S',   'Bs.S',         '',                  '928',  'False',    '2018',      '2021'
    KRW   =  'KRW',  _('Won'),                            _('won'),        '₩',      '₩SK',          '',                  '410',  'True',     '',          ''
    YER   =  'YER',  _('Yemeni rial'),                    _('rial'),       '﷼',      '﷼YE',          '',                  '886',  'True',     '',          ''
    JPY   =  'JPY',  _('Yen'),                            _('yen'),        '¥',      '¥JP',          '',                  '392',  'True',     '',          ''
    ZMW   =  'ZMW',  _('Zambian Kwacha'),                 _('kwacha'),     'K',      'ZK',           '',                  '967',  'True',     '',          ''
    ZWL   =  'ZWL',  _('Zimbabwe Dollar'),                _('dollar'),     'Z$',     'Z$',           '',                  '932',  'True',     '',          ''