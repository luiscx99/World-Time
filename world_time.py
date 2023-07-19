import tkinter as tk
from dataclasses import dataclass
import ttkbootstrap as ttk
from datetime import datetime
from PIL import Image, ImageTk
import random 
import pytz

# world time version 0.6 by: luiscx99

class App(ttk.Window):
    # windows
    def __init__(self, title, size):
        super().__init__()
        ttk.Style("darkly")
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
        self.maxsize(size[0],size[1])
        # title_frame
        self.titlelable = Title_frame(self)
        # input_fram
        self.inputframe = Input_aframe(self)
        # output local
        self.outputlocal = Local_time(self, 'The local time is:', 'Calibri 9 bold', 'Calibri 10 bold')
        # output txt
        self.outputalltext = Output_txtframe(self, 'info', 'inverse-info', 'Calibri 11 bold', 'Calibri 13 bold', '#258fac')
        # time frame
        #image = Image.open("background.jpg")
        #global width, height
        #width, height = self.winfo_screenwidth(), self.winfo_screenheight()
        self.timeframe = Time_frame(self, 'info', 'inverse-info', 'Calibri 45 bold')
        #self.update_time =Update_time(self)
        
        
        self.mainloop()
    
    #global var
    #global pytime, pydatetime
    #pytime = pytz.timezone
    #pydatetime = datetime.now


all_zone = {'Abidjan': 'Africa/Abidjan', 'Accra': 'Africa/Accra', 'Addis Ababa': 'Africa/Addis_Ababa', 'Algiers': 'Africa/Algiers', 'Asmara': 'Africa/Asmara', 'Asmera': 'Africa/Asmera', 'Bamako': 'Africa/Bamako', 'Bangui': 'Africa/Bangui', 'Banjul': 'Africa/Banjul', 'Bissau': 'Africa/Bissau', 'Blantyre': 'Africa/Blantyre', 'Brazzaville': 'Africa/Brazzaville', 'Bujumbura': 'Africa/Bujumbura', 'Cairo': 'Africa/Cairo', 'Casablanca': 'Africa/Casablanca', 'Ceuta': 'Africa/Ceuta', 'Conakry': 'Africa/Conakry', 'Dakar': 'Africa/Dakar', 'Dar es Salaam': 'Africa/Dar_es_Salaam', 'Djibouti': 'Africa/Djibouti', 'Douala': 'Africa/Douala', 'El Aaiun': 'Africa/El_Aaiun', 'Freetown': 'Africa/Freetown', 'Gaborone': 'Africa/Gaborone', 'Harare': 'Africa/Harare', 'Johannesburg': 'Africa/Johannesburg', 'Juba': 'Africa/Juba', 'Kampala': 'Africa/Kampala', 'Khartoum': 'Africa/Khartoum', 'Kigali': 'Africa/Kigali', 'Kinshasa': 'Africa/Kinshasa', 'Lagos': 'Africa/Lagos', 'Libreville': 'Africa/Libreville', 'Lome': 'Africa/Lome', 'Luanda': 'Africa/Luanda', 'Lubumbashi': 'Africa/Lubumbashi', 'Lusaka': 'Africa/Lusaka', 'Malabo': 'Africa/Malabo', 'Maputo': 'Africa/Maputo', 'Maseru': 'Africa/Maseru', 'Mbabane': 'Africa/Mbabane', 'Mogadishu': 'Africa/Mogadishu', 'Monrovia': 'Africa/Monrovia', 'Nairobi': 'Africa/Nairobi', 'Ndjamena': 'Africa/Ndjamena', 'Niamey': 'Africa/Niamey', 'Nouakchott': 'Africa/Nouakchott', 
'Ouagadougou': 'Africa/Ouagadougou', 'Porto-Novo': 'Africa/Porto-Novo', 'Sao Tome': 'Africa/Sao_Tome', 'Timbuktu': 'Africa/Timbuktu', 'Tripoli': 'Africa/Tripoli', 'Tunis': 'Africa/Tunis', 'Windhoek': 'Africa/Windhoek', 'Adak': 'America/Adak', 'Anchorage': 'America/Anchorage', 'Anguilla': 'America/Anguilla', 'Antigua': 'America/Antigua', 'Araguaina': 'America/Araguaina', 'Buenos Aires': 'America/Buenos_Aires', 'Catamarca': 'America/Catamarca', 'ComodRivadavia': 'America/Argentina/ComodRivadavia', 'Cordoba': 'America/Cordoba', 'Jujuy': 'America/Jujuy', 'La Rioja': 'America/Argentina/La_Rioja', 'Mendoza': 'America/Mendoza', 'Rio Gallegos': 'America/Argentina/Rio_Gallegos', 'Salta': 'America/Argentina/Salta', 'San Juan': 'America/Argentina/San_Juan', 'San Luis': 'America/Argentina/San_Luis', 'Tucuman': 'America/Argentina/Tucuman', 'Ushuaia': 'America/Argentina/Ushuaia', 'Aruba': 'America/Aruba', 'Asuncion': 'America/Asuncion', 'Atikokan': 'America/Atikokan', 'Atka': 'America/Atka', 'Bahia': 'America/Bahia', 'Bahia Banderas': 'America/Bahia_Banderas', 'Barbados': 'America/Barbados', 'Belem': 'America/Belem', 'Belize': 'America/Belize', 'Blanc-Sablon': 'America/Blanc-Sablon', 'Boa Vista': 'America/Boa_Vista', 'Bogota': 'America/Bogota', 
'Boise': 'America/Boise', 'Cambridge Bay': 'America/Cambridge_Bay', 'Campo Grande': 'America/Campo_Grande', 'Cancun': 'America/Cancun', 'Caracas': 'America/Caracas', 'Cayenne': 'America/Cayenne', 'Cayman': 'America/Cayman', 'Chicago': 'America/Chicago', 'Chihuahua': 'America/Chihuahua', 'Ciudad Juarez': 'America/Ciudad_Juarez', 'Coral Harbour': 'America/Coral_Harbour', 'Costa Rica': 'America/Costa_Rica', 'Creston': 'America/Creston', 'Cuiaba': 'America/Cuiaba', 'Curacao': 'America/Curacao', 'Danmarkshavn': 'America/Danmarkshavn', 'Dawson': 'America/Dawson', 'Dawson Creek': 'America/Dawson_Creek', 'Denver': 'America/Denver', 'Detroit': 'America/Detroit', 'Dominica': 'America/Dominica', 'Edmonton': 'America/Edmonton', 'Eirunepe': 'America/Eirunepe', 'El Salvador': 'America/El_Salvador', 'Ensenada': 'America/Ensenada', 'Fort Nelson': 'America/Fort_Nelson', 'Fort Wayne': 'America/Fort_Wayne', 'Fortaleza': 'America/Fortaleza', 'Glace Bay': 'America/Glace_Bay', 'Godthab': 'America/Godthab', 'Goose Bay': 'America/Goose_Bay', 'Grand Turk': 'America/Grand_Turk', 'Grenada': 'America/Grenada', 'Guadeloupe': 'America/Guadeloupe', 'Guatemala': 'America/Guatemala', 'Guayaquil': 'America/Guayaquil', 'Guyana': 'America/Guyana', 'Halifax': 'America/Halifax', 'Havana': 'America/Havana', 'Hermosillo': 'America/Hermosillo', 'Indianapolis': 'America/Indianapolis', 'Knox': 'America/Indiana/Knox', 'Marengo': 'America/Indiana/Marengo', 'Petersburg': 'America/Indiana/Petersburg', 'Tell City': 'America/Indiana/Tell_City', 'Vevay': 'America/Indiana/Vevay', 'Vincennes': 'America/Indiana/Vincennes', 'Winamac': 'America/Indiana/Winamac', 'Inuvik': 'America/Inuvik', 'Iqaluit': 'America/Iqaluit', 'Jamaica': 'Jamaica', 'Juneau': 'America/Juneau', 'Kentucky Louisville': 'America/Kentucky/Louisville', 'Kentucky Monticello': 'America/Kentucky/Monticello', 'Knox IN': 'America/Knox_IN', 'Kralendijk': 'America/Kralendijk', 'La Paz': 'America/La_Paz', 
'Lima': 'America/Lima', 'Los Angeles': 'America/Los_Angeles', 'Louisville': 'America/Louisville', 'Lower Princes': 'America/Lower_Princes', 'Maceio': 'America/Maceio', 'Managua': 'America/Managua', 'Manaus': 'America/Manaus', 'Marigot': 'America/Marigot', 'Martinique': 'America/Martinique', 'Matamoros': 'America/Matamoros', 'Mazatlan': 'America/Mazatlan', 'Menominee': 'America/Menominee', 'Merida': 'America/Merida', 'Metlakatla': 'America/Metlakatla', 'Mexico City': 'America/Mexico_City', 'Miquelon': 'America/Miquelon', 'Moncton': 'America/Moncton', 
'Monterrey': 'America/Monterrey', 'Montevideo': 'America/Montevideo', 'Montreal': 'America/Montreal', 'Montserrat': 'America/Montserrat', 'Nassau': 'America/Nassau', 'New York': 'America/New_York', 'Nipigon': 'America/Nipigon', 'Nome': 'America/Nome', 'Noronha': 'America/Noronha', 'Beulah': 'America/North_Dakota/Beulah', 'Center': 'America/North_Dakota/Center', 'New Salem': 'America/North_Dakota/New_Salem', 'Nuuk': 'America/Nuuk', 'Ojinaga': 'America/Ojinaga', 'Panama': 'America/Panama', 'Pangnirtung': 'America/Pangnirtung', 'Paramaribo': 'America/Paramaribo', 'Phoenix': 'America/Phoenix', 'Port-au-Prince': 'America/Port-au-Prince', 'Port of Spain': 'America/Port_of_Spain', 'Porto Acre': 'America/Porto_Acre', 'Porto Velho': 'America/Porto_Velho', 'Puerto Rico': 'America/Puerto_Rico', 'Punta Arenas': 'America/Punta_Arenas', 'Rainy River': 'America/Rainy_River', 'Rankin Inlet': 'America/Rankin_Inlet', 'Recife': 'America/Recife', 'Regina': 'America/Regina', 'Resolute': 'America/Resolute', 'Rio Branco': 'America/Rio_Branco', 'Rosario': 'America/Rosario', 'Santa Isabel': 'America/Santa_Isabel', 'Santarem': 'America/Santarem', 'Santiago': 'America/Santiago', 'Santo Domingo': 'America/Santo_Domingo', 'Sao Paulo': 'America/Sao_Paulo', 'Scoresbysund': 'America/Scoresbysund', 'Shiprock': 'America/Shiprock', 'Sitka': 'America/Sitka', 'St Barthelemy': 'America/St_Barthelemy', 'St Johns': 'America/St_Johns', 'St Kitts': 'America/St_Kitts', 'St Lucia': 'America/St_Lucia', 'St Thomas': 'America/St_Thomas', 'St Vincent': 'America/St_Vincent', 'Swift Current': 'America/Swift_Current', 'Tegucigalpa': 'America/Tegucigalpa', 'Thule': 'America/Thule', 'Thunder Bay': 'America/Thunder_Bay', 'Tijuana': 'America/Tijuana', 'Toronto': 'America/Toronto', 'Tortola': 'America/Tortola', 'Vancouver': 'America/Vancouver', 'Virgin': 'America/Virgin', 'Whitehorse': 'America/Whitehorse', 'Winnipeg': 'America/Winnipeg', 'Yakutat': 'America/Yakutat', 'Yellowknife': 'America/Yellowknife', 'Casey': 'Antarctica/Casey', 'Davis': 'Antarctica/Davis', 'DumontDUrville': 'Antarctica/DumontDUrville', 'Macquarie': 'Antarctica/Macquarie', 'Mawson': 'Antarctica/Mawson', 'McMurdo': 'Antarctica/McMurdo', 'Palmer': 'Antarctica/Palmer', 'Rothera': 'Antarctica/Rothera', 'South Pole': 'Antarctica/South_Pole', 'Syowa': 'Antarctica/Syowa', 'Troll': 'Antarctica/Troll', 'Vostok': 'Antarctica/Vostok', 'Longyearbyen': 'Arctic/Longyearbyen', 'Aden': 'Asia/Aden', 'Almaty': 'Asia/Almaty', 'Amman': 'Asia/Amman', 'Anadyr': 'Asia/Anadyr', 'Aqtau': 'Asia/Aqtau', 'Aqtobe': 'Asia/Aqtobe', 'Ashgabat': 'Asia/Ashgabat', 'Ashkhabad': 'Asia/Ashkhabad', 'Atyrau': 'Asia/Atyrau', 'Baghdad': 'Asia/Baghdad', 'Bahrain': 'Asia/Bahrain', 'Baku': 'Asia/Baku', 'Bangkok': 'Asia/Bangkok', 'Barnaul': 'Asia/Barnaul', 'Beirut': 'Asia/Beirut', 'Bishkek': 'Asia/Bishkek', 'Brunei': 'Asia/Brunei', 'Calcutta': 'Asia/Calcutta', 'Chita': 'Asia/Chita', 'Choibalsan': 'Asia/Choibalsan', 'Chongqing': 'Asia/Chongqing', 'Chungking': 'Asia/Chungking', 'Colombo': 'Asia/Colombo', 'Dacca': 'Asia/Dacca', 'Damascus': 'Asia/Damascus', 'Dhaka': 'Asia/Dhaka', 'Dili': 'Asia/Dili', 'Dubai': 'Asia/Dubai', 'Dushanbe': 'Asia/Dushanbe', 'Famagusta': 'Asia/Famagusta', 'Gaza': 'Asia/Gaza', 'Harbin': 'Asia/Harbin', 'Hebron': 'Asia/Hebron', 'Ho Chi Minh': 'Asia/Ho_Chi_Minh', 'Hong Kong': 'Asia/Hong_Kong', 'Hovd': 'Asia/Hovd', 'Irkutsk': 'Asia/Irkutsk', 'Istanbul': 'Europe/Istanbul', 'Jakarta': 'Asia/Jakarta', 'Jayapura': 'Asia/Jayapura', 'Jerusalem': 'Asia/Jerusalem', 'Kabul': 'Asia/Kabul', 'Kamchatka': 'Asia/Kamchatka', 'Karachi': 'Asia/Karachi', 'Kashgar': 'Asia/Kashgar', 'Kathmandu': 'Asia/Kathmandu', 'Katmandu': 'Asia/Katmandu', 'Khandyga': 'Asia/Khandyga', 'Kolkata': 'Asia/Kolkata', 'Krasnoyarsk': 'Asia/Krasnoyarsk', 'Kuala Lumpur': 'Asia/Kuala_Lumpur', 'Kuching': 'Asia/Kuching', 'Kuwait': 'Asia/Kuwait', 'Macao': 'Asia/Macao', 'Macau': 'Asia/Macau', 'Magadan': 'Asia/Magadan', 'Makassar': 'Asia/Makassar', 'Manila': 'Asia/Manila', 'Muscat': 'Asia/Muscat', 'Nicosia': 'Europe/Nicosia', 'Novokuznetsk': 'Asia/Novokuznetsk', 'Novosibirsk': 'Asia/Novosibirsk', 'Omsk': 'Asia/Omsk', 'Oral': 'Asia/Oral', 'Phnom Penh': 'Asia/Phnom_Penh', 'Pontianak': 'Asia/Pontianak', 'Pyongyang': 'Asia/Pyongyang', 'Qatar': 'Asia/Qatar', 'Qostanay': 'Asia/Qostanay', 'Qyzylorda': 'Asia/Qyzylorda', 'Rangoon': 'Asia/Rangoon', 'Riyadh': 'Asia/Riyadh', 'Saigon': 'Asia/Saigon', 'Sakhalin': 'Asia/Sakhalin', 'Samarkand': 'Asia/Samarkand', 'Seoul': 'Asia/Seoul', 'Shanghai': 'Asia/Shanghai', 'Singapore': 'Singapore', 'Srednekolymsk': 'Asia/Srednekolymsk', 'Taipei': 'Asia/Taipei', 'Tashkent': 'Asia/Tashkent', 'Tbilisi': 'Asia/Tbilisi', 'Tehran': 'Asia/Tehran', 'Tel Aviv': 'Asia/Tel_Aviv', 'Thailand': 'Asia/Bangkok', 'Thimbu': 'Asia/Thimbu', 'Thimphu': 'Asia/Thimphu', 'Tokyo': 'Asia/Tokyo', 'Tomsk': 'Asia/Tomsk', 'Ujung Pandang': 'Asia/Ujung_Pandang', 'Ulaanbaatar': 'Asia/Ulaanbaatar', 'Ulan Bator': 'Asia/Ulan_Bator', 'Urumqi': 'Asia/Urumqi', 'Ust-Nera': 'Asia/Ust-Nera', 'Vientiane': 'Asia/Vientiane', 'Vladivostok': 'Asia/Vladivostok', 'Yakutsk': 'Asia/Yakutsk', 'Yangon': 'Asia/Yangon', 'Yekaterinburg': 'Asia/Yekaterinburg', 'Yerevan': 'Asia/Yerevan', 'Azores': 'Atlantic/Azores', 'Bermuda': 'Atlantic/Bermuda', 'Canary': 'Atlantic/Canary', 'Cape Verde': 'Atlantic/Cape_Verde', 'Faeroe': 'Atlantic/Faeroe', 'Faroe': 'Atlantic/Faroe', 'Jan Mayen': 'Atlantic/Jan_Mayen', 'Madeira': 'Atlantic/Madeira', 'Reykjavik': 'Atlantic/Reykjavik', 'South Georgia': 'Atlantic/South_Georgia', 'St Helena': 'Atlantic/St_Helena', 'Stanley': 'Atlantic/Stanley', 'Australia': 'Australia/ACT', 'Australia Adelaide': 'Australia/Adelaide', 'Australia Brisbane': 'Australia/Brisbane', 'Australia Broken Hill': 
'Australia/Broken_Hill', 'Australia Canberra': 'Australia/Canberra', 'Australia Currie': 'Australia/Currie', 'Australia Darwin': 'Australia/Darwin', 'Australia Eucla': 'Australia/Eucla', 'Australia Hobart': 'Australia/Hobart', 'Australia LHI': 'Australia/LHI', 'Australia Lindeman': 'Australia/Lindeman', 'Australia Lord Howe': 'Australia/Lord_Howe', 'Australia Melbourne': 'Australia/Melbourne', 'Australia NSW': 'Australia/NSW', 'Australia North': 'Australia/North', 'Australia Perth': 'Australia/Perth', 'Australia Queensland': 'Australia/Queensland', 'Australia South': 'Australia/South', 'Sydney': 'Australia/Sydney', 'Australia Tasmania': 'Australia/Tasmania', 'Australia Victoria': 'Australia/Victoria', 'Australia West': 'Australia/West', 'Australia Yancowinna': 'Australia/Yancowinna', 'Brazil Acre': 'Brazil/Acre', 'Brazil DeNoronha': 'Brazil/DeNoronha', 'Brazil East': 'Brazil/East', 'Brazil West': 'Brazil/West', 'CET': 'CET', 'CST6CDT': 'CST6CDT', 'Canada Atlantic': 'Canada/Atlantic', 'Canada Central': 'Canada/Central', 'Canada Eastern': 'Canada/Eastern', 'Canada Mountain': 'Canada/Mountain', 'Canada Newfoundland': 'Canada/Newfoundland', 'Canada Pacific': 'Canada/Pacific', 'Canada Saskatchewan': 'Canada/Saskatchewan', 'Canada Yukon': 'Canada/Yukon', 'Chile Continental': 'Chile/Continental', 'Chile EasterIsland': 'Chile/EasterIsland', 'Cuba': 'Cuba', 'EET': 'EET', 'EST': 'EST', 'EST5EDT': 'EST5EDT', 'Egypt': 'Egypt', 'Eire': 'Eire', 'Etc GMT': 'Etc/GMT', 'Etc GMT+0': 'Etc/GMT+0', 'Etc GMT+1': 'Etc/GMT+1', 
'Etc GMT+10': 'Etc/GMT+10', 'Etc GMT+11': 'Etc/GMT+11', 'Etc GMT+12': 'Etc/GMT+12', 'Etc GMT+2': 'Etc/GMT+2', 'Etc GMT+3': 'Etc/GMT+3', 'Etc GMT+4': 'Etc/GMT+4', 'Etc GMT+5': 'Etc/GMT+5', 'Etc GMT+6': 'Etc/GMT+6', 'Etc GMT+7': 'Etc/GMT+7', 'Etc GMT+8': 'Etc/GMT+8', 'Etc GMT+9': 'Etc/GMT+9', 'Etc GMT-0': 'Etc/GMT-0', 'Etc GMT-1': 'Etc/GMT-1', 'Etc GMT-10': 'Etc/GMT-10', 'Etc GMT-11': 'Etc/GMT-11', 'Etc GMT-12': 'Etc/GMT-12', 'Etc GMT-13': 'Etc/GMT-13', 'Etc GMT-14': 'Etc/GMT-14', 'Etc GMT-2': 'Etc/GMT-2', 'Etc GMT-3': 'Etc/GMT-3', 'Etc GMT-4': 'Etc/GMT-4', 'Etc GMT-5': 'Etc/GMT-5', 'Etc GMT-6': 'Etc/GMT-6', 'Etc GMT-7': 'Etc/GMT-7', 'Etc GMT-8': 'Etc/GMT-8', 'Etc GMT-9': 'Etc/GMT-9', 'Etc GMT0': 'Etc/GMT0', 'Etc Greenwich': 'Etc/Greenwich', 'Etc UCT': 'Etc/UCT', 'Etc UTC': 'Etc/UTC', 'Etc Universal': 'Etc/Universal', 'Etc Zulu': 'Etc/Zulu', 'Amsterdam': 'Europe/Amsterdam', 'Andorra': 'Europe/Andorra', 'Astrakhan': 'Europe/Astrakhan', 'Athens': 'Europe/Athens', 'Belfast': 'Europe/Belfast', 'Belgrade': 'Europe/Belgrade', 'Berlin': 'Europe/Berlin', 'Bratislava': 'Europe/Bratislava', 'Brussels': 'Europe/Brussels', 'Bucharest': 'Europe/Bucharest', 'Budapest': 'Europe/Budapest', 'Busingen': 'Europe/Busingen', 'Chisinau': 'Europe/Chisinau', 'Copenhagen': 'Europe/Copenhagen', 'Dublin': 'Europe/Dublin', 'Gibraltar': 'Europe/Gibraltar', 'Guernsey': 'Europe/Guernsey', 'Helsinki': 'Europe/Helsinki', 'Isle of Man': 'Europe/Isle_of_Man', 'Jersey': 'Europe/Jersey', 'Kaliningrad': 'Europe/Kaliningrad', 'Kiev': 'Europe/Kiev', 'Kirov': 'Europe/Kirov', 'Kyiv': 'Europe/Kyiv', 'Lisbon': 'Europe/Lisbon', 'Ljubljana': 'Europe/Ljubljana', 'London': 'Europe/London', 'Luxembourg': 'Europe/Luxembourg', 'Madrid': 'Europe/Madrid', 'Malta': 'Europe/Malta', 'Mariehamn': 'Europe/Mariehamn', 'Minsk': 'Europe/Minsk', 'Monaco': 'Europe/Monaco', 'Moscow': 'Europe/Moscow', 'Oslo': 'Europe/Oslo', 'Paris': 'Europe/Paris', 'Podgorica': 'Europe/Podgorica', 'Prague': 'Europe/Prague', 'Riga': 'Europe/Riga', 'Rome': 'Europe/Rome', 'Samara': 'Europe/Samara', 'San Marino': 'Europe/San_Marino', 'Sarajevo': 'Europe/Sarajevo', 'Saratov': 'Europe/Saratov', 'Simferopol': 'Europe/Simferopol', 'Skopje': 'Europe/Skopje', 'Sofia': 'Europe/Sofia', 'Stockholm': 'Europe/Stockholm', 'Tallinn': 'Europe/Tallinn', 'Tirane': 'Europe/Tirane', 'Tiraspol': 'Europe/Tiraspol', 'Ulyanovsk': 'Europe/Ulyanovsk', 'Uzhgorod': 'Europe/Uzhgorod', 'Vaduz': 'Europe/Vaduz', 'Vatican': 'Europe/Vatican', 'Vienna': 'Europe/Vienna', 'Vilnius': 'Europe/Vilnius', 'Volgograd': 'Europe/Volgograd', 'Warsaw': 'Europe/Warsaw', 'Zagreb': 'Europe/Zagreb', 'Zaporozhye': 'Europe/Zaporozhye', 'Zurich': 'Europe/Zurich', 'GB': 'GB', 'GB-Eire': 'GB-Eire', 'GMT': 'GMT', 'GMT+0': 'GMT+0', 'GMT-0': 'GMT-0', 'GMT0': 'GMT0', 'Greenwich': 'Greenwich', 'HST': 'HST', 'Hongkong': 'Hongkong', 'Iceland': 'Iceland', 'Antananarivo': 'Indian/Antananarivo', 'Chagos': 'Indian/Chagos', 'Christmas': 'Indian/Christmas', 'Cocos': 'Indian/Cocos', 'Comoro': 'Indian/Comoro', 'Kerguelen': 'Indian/Kerguelen', 'Mahe': 'Indian/Mahe', 'Maldives': 'Indian/Maldives', 'Mauritius': 'Indian/Mauritius', 'Mayotte': 'Indian/Mayotte', 'Reunion': 'Indian/Reunion', 'Iran': 
'Iran', 'Israel': 'Israel', 'Japan': 'Japan', 'Kwajalein': 'Kwajalein', 'Libya': 'Libya', 'MET': 'MET', 'MST': 'MST', 'MST7MDT': 'MST7MDT', 'Mexico BajaNorte': 'Mexico/BajaNorte', 'Mexico BajaSur': 'Mexico/BajaSur', 'Mexico': 'Mexico/General', 'NZ': 'NZ', 'NZ-CHAT': 'NZ-CHAT', 
'Navajo': 'Navajo', 'PRC': 'PRC', 'PST8PDT': 'PST8PDT', 'Pacific Apia': 'Pacific/Apia', 'Pacific Auckland': 'Pacific/Auckland', 'Pacific Bougainville': 'Pacific/Bougainville', 'Pacific Chatham': 'Pacific/Chatham', 'Pacific Chuuk': 'Pacific/Chuuk', 'Pacific Easter': 'Pacific/Easter', 'Pacific Efate': 'Pacific/Efate', 'Pacific Enderbury': 'Pacific/Enderbury', 'Pacific Fakaofo': 'Pacific/Fakaofo', 'Pacific Fiji': 'Pacific/Fiji', 'Pacific Funafuti': 'Pacific/Funafuti', 'Pacific Galapagos': 'Pacific/Galapagos', 'Pacific Gambier': 'Pacific/Gambier', 'Pacific Guadalcanal': 'Pacific/Guadalcanal', 'Pacific Guam': 'Pacific/Guam', 'Pacific Honolulu': 'Pacific/Honolulu', 'Pacific Johnston': 'Pacific/Johnston', 'Pacific Kanton': 'Pacific/Kanton', 'Pacific Kiritimati': 'Pacific/Kiritimati', 'Pacific Kosrae': 'Pacific/Kosrae', 'Pacific Kwajalein': 'Pacific/Kwajalein', 'Pacific Majuro': 'Pacific/Majuro', 'Pacific Marquesas': 'Pacific/Marquesas', 'Pacific Midway': 'Pacific/Midway', 'Pacific Nauru': 'Pacific/Nauru', 'Pacific Niue': 'Pacific/Niue', 'Pacific Norfolk': 'Pacific/Norfolk', 'Pacific Noumea': 'Pacific/Noumea', 'Pacific Pago Pago': 'Pacific/Pago_Pago', 'Pacific Palau': 'Pacific/Palau', 'Pacific Pitcairn': 'Pacific/Pitcairn', 'Pacific Pohnpei': 'Pacific/Pohnpei', 'Pacific Ponape': 'Pacific/Ponape', 'Pacific Port Moresby': 'Pacific/Port_Moresby', 'Pacific Rarotonga': 'Pacific/Rarotonga', 'Pacific Saipan': 'Pacific/Saipan', 'Pacific Samoa': 'Pacific/Samoa', 'Pacific Tahiti': 'Pacific/Tahiti', 'Pacific Tarawa': 'Pacific/Tarawa', 'Pacific Tongatapu': 'Pacific/Tongatapu', 'Pacific Truk': 'Pacific/Truk', 'Pacific Wake': 'Pacific/Wake', 'Pacific Wallis': 'Pacific/Wallis', 'Pacific Yap': 'Pacific/Yap', 'Poland': 'Poland', 'Portugal': 'Portugal', 'ROC': 'ROC', 'ROK': 'ROK', 'Turkey': 'Turkey', 'UCT': 'UCT', 'US Alaska': 'US/Alaska', 'US Aleutian': 'US/Aleutian', 'US Arizona': 'US/Arizona', 'US Central': 'US/Central', 'US East-Indiana': 'US/East-Indiana', 'US Eastern': 'US/Eastern', 'US Hawaii': 'US/Hawaii', 'US Indiana-Starke': 'US/Indiana-Starke', 'US Michigan': 'US/Michigan', 'US Mountain': 'US/Mountain', 'US Pacific': 'US/Pacific', 'US Samoa': 'US/Samoa', 'UTC': 'UTC', 'Universal': 'Universal', 'W-SU': 'W-SU', 'WET': 'WET', 'Zulu': 'Zulu'}


TXT_T = 'This is the current time in:'
pytime = pytz.timezone
pydatetime = datetime.now
backup_country = {}

def country_title_c():
    inputstr = entry_str.get()
    strinput = inputstr.title()
    return strinput

# Get Time
def get_time():
    global country_tz, current_time_in, TXT_T
    #print(gettime_zone)
    check_error(0)
    gettime_zone = all_zone[country_title_c()]
    country_tz = pytime(gettime_zone)
    timeIn = pydatetime(country_tz)
    backup_country[1] = gettime_zone
    current_time_in = timeIn.strftime("%I:%M %p")
    check_error(1)

    #print(backup_country[1])
    output_ctime()

# set country time 
def output_ctime():
    output_str.set(country_title_c())
    output_txt.set(TXT_T)
    output_timestr.set(current_time_in)
    entry_str.set('')
    upd_localtime()

# local time
def upd_localtime():
    local = pydatetime()
    global current_day
    current_day = local.strftime("%m/%d/%Y, %I:%M %p")
    output_local_time_str.set(current_day)
# return to Local_time
    return current_day

# set default time 
def default_time():
    default_zone, country_zone = random.choice(list(all_zone.items()))
    save_zone = pytime(country_zone)
    save_time = pydatetime(save_zone)
    backup_country[1] = country_zone
    output_str.set(default_zone)
    default_time_in = save_time.strftime("%I:%M %p")
    output_timestr.set(default_time_in)
    output_txt.set(TXT_T)

def setup_error_frame(type: str):
    if type == 'error':
            emptyframe.pack_forget()
            errorLable.config(state='error')
            errorLable.pack(before=input_entry)
            entry_str.set('')
    elif type == 'ok':
            errorLable.pack_forget()
            emptyframe.pack(before=input_entry)
            errorLable.config(state='noerror')

# check error
def check_error(val: bool):
    #getstate = errorLable.cget('state')
    if not entry_str.get() and not val:
            setup_error_frame('error')
    elif entry_str.get() and not val:
        strinput = country_title_c()
        if strinput in all_zone:
        #   print(strinput)
            setup_error_frame('ok')
            print('ok')
        else:
        #   print('error')
            setup_error_frame('error')

# get backgroud image
def get_styleimg(img: str, wdth: int, hght: int):
    image = Image.open(img)
    image = image.resize((wdth, hght))
    image = ImageTk.PhotoImage(image)
    return image

class Title_frame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        ttk.Label(self, text='World Time', font='Calibri 24 bold').pack(pady=10)
        ttk.Label(self, text='Get the time from any country in the world', font='Calibri 10 bold').pack()
        self.pack()

class Input_aframe(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, width=210, height=100)
        self.pack_propagate(False)
        self.pack(padx=50)
        self.input_all()
        
    def input_all(self):
        global entry_str, input_entry, errorLable, emptyframe
        entry_str = tk.StringVar()
        input_entry = ttk.Entry(self, textvariable=entry_str)
        input_entry.bind('<Return>', lambda event:get_time())
        input_button = ttk.Button(self, text='Get Time', command=get_time)
        #savestr = tk.StringVar()
        emptyframe = ttk.Frame(self, width=30, height=19)
        errorLable = ttk.Label(self, state='noerror', text='Type the correct timezone or country', font='Calibri 10 bold', foreground='red')
        emptyframe.pack()
        input_entry.pack(pady=5)
        input_button.pack(pady=5)

class Local_time(ttk.Frame):
    def __init__(self, master, Ltext: str, Lfont: str, timef: str):
        super().__init__(master, width=540, height=40)
        self.pack_propagate(False)
        global output_local_time_str
        output_local_time_str = tk.StringVar()
        output_local_time_str.set(upd_localtime())
        localttx = ttk.Label(self, text=Ltext, font=Lfont)
        localtimetxt = ttk.Label(self, textvariable=output_local_time_str, font=timef)
        localttx.pack(side='top', fill='x')
        localtimetxt.pack(side='top', fill='x')
        self.pack(padx=7)
       
class Output_txtframe(ttk.Frame):
    def __init__(self, master, style: str, invstyle: str, fontstr: str, fonttxt: str, fg: str):
        super().__init__(master, bootstyle=style, width=450, height=46)
        self.pack_propagate(False)
        global output_txt, output_str
        output_txt = tk.StringVar()
        output_str = tk.StringVar()
#       self.image = Image.open()
#       self.image = self.image.resize((450, 32))
#       self.image = ImageTk.PhotoImage(self.image)
        self.image = get_styleimg("outputtext.png", 450, 23)
        self.image2 = get_styleimg("outputtext2.png", 450, 23)
        #ttk.Frame(self, width=90, height=10).pack(side='left')
        #ttk.Frame(self, width=90, height=10).pack(side='right')         
        ttk.Label(self, border='0', image=self.image, textvariable=output_txt, font=fontstr, foreground='#027696', compound='center').pack(expand=True, side='top')
        ttk.Label(self, border='0', image=self.image2, bootstyle=invstyle, textvariable=output_str, font=fonttxt, foreground=fg, compound='center').pack(expand=True, side='top')
        self.pack()  

class Time_frame(ttk.Frame):
    def __init__(self, master, stylet: str, invtext: str, tfont: str):
        super().__init__(master, bootstyle=stylet, width=450, height=190)
        self.pack_propagate(False)
        global output_timestr
        #self.image = Image.open("timezone.png")
#        self.image = self.image.resize((450, 390))
#        self.image = ImageTk.PhotoImage(self.image)
        self.image = get_styleimg("timezone.png", 450, 199)
        output_timestr = tk.StringVar()
        #tk.Label(self, image=bgimg).pack(expand=True)
        
        ttk.Label(self, border='0', image=self.image, textvariable=output_timestr, font=tfont, compound='center', foreground='#126D90').pack(ipadx='5', side='top')
        self.pack()

        self.after(600, self.utime_frame)
        # update time
    def utime_frame(self):
        if backup_country == {}:
        # default time
            default_time()
        else:
            get_savezone = pytime(backup_country[1])
            get_timeIn = pydatetime(get_savezone)
            update_time_in = get_timeIn.strftime("%I:%M %p")
            output_timestr.set(update_time_in)
            output_local_time_str.set(upd_localtime())

        self.after(60000, self.utime_frame)

        
App('World Time', (450,410))