# limpiar json devices
import json

n_ram_arr = [0, 1, 1.5, 2, 3, 4, 6, 8, 10, 12]
n_storage_arr = [0, 4, 8, 16, 32, 64, 128, 256, 512]
n_display_width_arr = [120, 128, 240, 442, 480, 540, 600, 640, 720, 750, 828, 876, 1080,
                       1125, 1170, 1176, 1200, 1236, 1242, 1284, 1344, 1440, 1536, 1644, 1768, 2160, 2200, 3840]
n_display_height_arr = [160, 320, 800, 854, 960, 1024, 1280, 1334, 1352, 1440, 1480, 1498, 1500, 1512, 1520, 1528, 1544, 1548, 1560, 1570, 1600, 1620, 1640, 1680, 1792, 1920, 2040, 2142, 2152, 2160, 2180, 2208, 2220, 2232, 2240,
                        2244, 2246, 2248, 2256, 2258, 2270, 2280, 2300, 2310, 2312, 2316, 2340, 2376, 2400, 2408, 2436, 2460, 2480, 2520, 2532, 2560, 2636, 2640, 2676, 2688, 2772, 2778, 2880, 2960, 2992, 3040, 3088, 3120, 3168, 3200, 3216, 3840, 4320]

n_camera_pixels_arr = [0, 0.1, 0.2, 0.3, 1.3, 2, 3, 5, 8, 12, 13,
                       16, 19, 20, 21, 22, 23, 24, 25, 32, 40, 48, 50, 60, 64, 108]
n_video_pixels_arr = [0, 240, 288, 480, 720, 1080, 1440, 2160, 3240, 4320]
n_battery_size_arr = [600, 720, 750, 800, 860, 1000, 1020, 1150, 1200, 1300, 1350, 1400, 1470, 1500, 1530, 1550, 1600, 1700, 1750, 1800, 1821, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2210, 2227, 2250, 2280, 2300, 2350, 2400, 2410, 2450, 2460, 2500, 2510, 2540, 2600, 2620, 2630, 2650, 2658, 2670, 2700, 2716, 2730, 2750, 2760, 2770, 2800, 2815, 2850, 2860, 2870, 2880, 2900, 2915, 2920, 2942, 2950, 2965, 2970, 2980, 2990, 3000, 3010, 3020, 3030, 3040, 3046, 3050, 3060, 3070, 3075, 3080, 3090, 3100, 3110, 3120, 3130, 3140, 3150, 3160, 3174, 3180, 3200, 3210, 3225, 3230, 3240, 3250, 3260, 3300, 3315, 3320,
                      3330, 3340, 3350, 3360, 3400, 3410, 3420, 3425, 3430, 3450, 3500, 3520, 3540, 3550, 3570, 3580, 3600, 3630, 3650, 3687, 3700, 3750, 3760, 3765, 3800, 3820, 3850, 3885, 3900, 3930, 3940, 3969, 3990, 4000, 4010, 4015, 4020, 4025, 4030, 4035, 4040, 4045, 4050, 4060, 4065, 4070, 4080, 4085, 4100, 4115, 4130, 4132, 4160, 4180, 4200, 4220, 4230, 4235, 4250, 4260, 4300, 4310, 4315, 4350, 4380, 4400, 4500, 4510, 4520, 4550, 4600, 4680, 4700, 4720, 4729, 4780, 4800, 4820, 4900, 5000, 5020, 5080, 5100, 5160, 5200, 5260, 5300, 5500, 5580, 5800, 6000, 6020, 6180, 6500, 6600, 7000, 9000, 10000, 10300, 16000, 18000]

n_display_size_arr = [1.77, 1.8, 2.2, 2.4, 2.8, 3.3, 3.8, 4.0, 4.5, 4.6, 4.7, 4.95, 5.0, 5.09, 5.1, 5.15, 5.2, 5.3, 5.34, 5.4, 5.45, 5.46, 5.5, 5.6, 5.65, 5.67, 5.7, 5.71, 5.72, 5.73, 5.8, 5.81, 5.83, 5.84, 5.85, 5.86, 5.88, 5.9, 5.93, 5.94, 5.95, 5.97, 5.98, 5.99, 6.0, 6.01, 6.09, 6.1, 6.15, 6.18, 6.19, 6.2,
                      6.21, 6.22, 6.23, 6.24, 6.26, 6.28, 6.3, 6.35, 6.36, 6.38, 6.39, 6.4, 6.41, 6.42, 6.43, 6.44, 6.45, 6.47, 6.49, 6.5, 6.51, 6.52, 6.53, 6.55, 6.56, 6.57, 6.58, 6.59, 6.6, 6.62, 6.63, 6.65, 6.67, 6.7, 6.72, 6.76, 6.78, 6.8, 6.81, 6.82, 6.85, 6.89, 6.9, 6.92, 6.95, 7.0, 7.09, 7.1, 7.12, 7.2, 7.3, 7.6, 8.0]

chipset_score_arr = [0, 14, 21, 22, 23, 24, 25, 26, 28, 31, 32, 34, 35, 37, 38, 39, 40, 42, 44, 45, 48, 50, 51, 52, 53, 54, 55, 56,
                     57, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 88, 90, 92, 93, 95, 98]


def a_num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


def normalize(arr, val):
    arr.sort()
    m = max(arr)
    return (val/m * 100)


with open('C:/Users/Usuario/Downloads/bbdd/devices.json') as devices:
    data = json.load(devices)

lista = []


for d in data['RECORDS']:

    # ids numericos
    d['id'] = int(d['id'])

    # ram numerico
    ram = d['ram'].split()
    if ram != '' and ram[1] != 'MB':
        d['n_ram'] = a_num(ram[0].split('/')[0].split('-')[0])
    else:
        d['n_ram'] = a_num(0)

    # storage numerico

    n_storage = d['storage'].split(',')[0].split()[0].replace('GB', '')
    d['n_storage'] = a_num(n_storage)

    expansion = d['storage'].split(',')[1].strip()

    if (expansion != "no card slot") or (expansion == "NM") or (expansion == "Unspecified"):
        # print(expansion)
        d['expansion'] = 1
        # print('111111111111111111111111111111111111111111111111111111')
    else:
        # print(expansion)
        d['expansion'] = 0
        # print('00000000000000000000000000000000000000000000000000000')

    # resolucion numerica
    res = d['display_resolution'].split()[0].split('x')
    d['n_display_width'] = a_num(res[0])
    d['n_display_height'] = a_num(res[1])

    # camerapixeles numerico

    cam = d['camera_pixels'].strip().split()[0]
    d['n_camera_pixels'] = a_num(cam)

    # video pixels numerico
    vid = d['video_pixels']
    d['n_video_pixels'] = a_num(vid.replace('p', ''))

    # bateria mumerica
    bat = d['battery_size'].strip().replace('mAh', '').replace('.', '')
    d['n_battery_size'] = a_num(bat)

    # tamano pantalla
    tam = d['display_size'].replace('"', '')
    d['n_display_size'] = a_num(tam)

    # chipset score
    chip = d['chipset']

    tabla_chips = {
        'Exynos 7880': '64',
        'Exynos 7870 Octa': '66',
        'MT6735P': '39',
        'MT6753': '72',
        'Spreadtrum SC9832A': '34',
        '': '0',
        'Exynos 7570': '57',
        'Exynos 7580 Octa': '62',
        'Exynos 8890 Octa': '68',
        'Snapdragon 821': '67',
        'Snapdragon 653': '50',
        'Snapdragon 210': '28',
        'Snapdragon 430': '54',
        'Snapdragon 820': '63',
        'MT6580': '25',
        'Helio P10': '62',
        'MT6735': '44',
        'Snapdragon 617': '52',
        'MT6595': '63',
        'Exynos 7580': '62',
        'Snapdragon 650': '57',
        'MT6737': '53',
        'MT6750': '56',
        'Snapdragon 425': '50',
        'MT6735M': '39',
        'Kirin 620': '50',
        'Snapdragon 625': '55',
        'MT6737T': '54',
        'Kirin 655': '56',
        'Helio X25': '64',
        'Snapdragon 615': '53',
        'Snapdragon 652': '57',
        'Kirin 960': '58',
        'Spreadtrum SC9830': '34',
        'Snapdragon 810': '72',
        'Spreadtrum SC7731C': '26',
        'Helio X20': '61',
        'MT6580M': '25',
        'Spreadtrum SC6821': '24',
        'Snapdragon 626': '61',
        'Xiaomi Surge S1': '25',
        'Snapdragon 400': '26',
        'Helio P25': '69',
        'Helio X10': '62',
        'Exynos 8890': '68',
        'Helio P20': '67',
        'Exynos 3475 Quad': '28',
        'Exynos 7570 Quad': '57',
        'Snapdragon 435': '60',
        'MT8163': '44',
        'Snapdragon 410': '45',
        'Spreadtrum SC6531DA': '22',
        'MT6737M': '54',
        'Snapdragon 415': '57',
        'MT8176': '58',
        'Spreadtrum SC7731': '26',
        'MTK6261D': '28',
        'Kirin 950': '57',
        'MT6276A': '22',
        'Snapdragon 835': '74',
        'Exynos 8895': '71',
        'MT6735CP': '44',
        'MT8735B': '48',
        'Snapdragon 212': '34',
        'MT8321': '14',
        'Spreadtrum SC7731G': '26',
        'Intel Atom x5-Z8500': '29',
        'MT6572': '21',
        'Snapdragon 855': '82',
        'MT6750T': '52',
        'Apple A11 Bionic': '40',
        'Kirin 658': '63',
        'Snapdragon 425 (Wi-Fi': '50',
        'Apple A9': '50',
        'Snapdragon 630': '66',
        'MT8127': '31',
        'Spreadtrum SC9832': '34',
        'Snapdragon 660': '78',
        'Snapdragon 427': '52',
        'Kirin 659': '64',
        'MT6737&#1052;': '53',
        'MT6570': '21',
        'Apple A10X Fusion': '39',
        'Snapdragon 450': '65',
        'MT8735': '48',
        'Exynos 7885': '74',
        'Helio X30': '66',
        'Helio X23': '53',
        'Kirin 970': '73',
        'MT6738': '50',
        'MT6750S': '55',
        'Snapdragon 845': '81',
        'Helio P30': '73',
        'MT6580A': '25',
        'Helio P23': '76',
        'MT8173': '58',
        'Snapdragon 636': '72',
        'MT8161': '4',
        'MT8167D': '41',
        'Exynos 9810': '73',
        'Exynos 7872': '48',
        'MT8735A': '48',
        'MT6737VWH': '55',
        'MT6739': '48',
        'Snapdragon 205': '32',
        'Kirin 960s': '58',
        'MT8321A': '14',
        'Helio P70': '79',
        'Helio P60': '71',
        'MT6261D': '55',
        'Apple A10 Fusion': '41',
        'Spreadtrum 7701B': '25',
        'MT6750V': '53',
        'MT6737H': '54',
        'MT6737VWT': '55',
        'MT6739WA': '48',
        'Helio P22': '75',
        'Spreadtrum SC6531E': '24',
        'Helio P18': '51',
        'Helio A22': '54',
        'Snapdragon 710': '63',
        'Kirin 710': '71',
        'MT6739WW': '48',
        'Snapdragon 670': '63',
        'Spreadtrum SC9850K': '25',
        'Apple A12 Bionic': '42',
        'Kirin 980': '72',
        'Snapdragon 632': '68',
        'MT6739M': '48',
        'Apple A12X Bionic': '54',
        'Snapdragon 439': '68',
        'MT6755': '52',
        'Unisoc SC9832E': '50',
        'MT6580W': '25',
        'MT6737W': '53',
        'Snapdragon 675': '70',
        'Helio P35': '68',
        'Spreadtrum 7715A': '32',
        'Exynos 7904': '70',
        'Spreadtrum SC7731E': '23',
        'Snapdragon 865 5G': '95',
        'Exynos 9820': '75',
        'Exynos 9610': '80',
        'Spreadtrum SC9820E': '25',
        'MT6276&#1040;': '35',
        'MT6739WM': '48',
        'Exynos 7884': '64',
        'Snapdragon 712': '63',
        'Unisoc SC9863': '54',
        'Snapdragon 429': '56',
        'MT6260A': '37',
        'Snapdragon Wear 2100': '36',
        'Snapdragon SiP 1': '73',
        'Exynos 9609': '81',
        'Snapdragon 730': '69',
        'MT6261A': '38',
        'Kirin 710F': '71',
        'Helio P90': '66',
        'Unisoc SC9863A': '50',
        'Unisoc SC7731E': '45',
        'MT6761V': '56',
        'Kirin 810': '75',
        'Exynos 9825': '75',
        'Snapdragon 665': '77',
        'Helio P65': '71',
        'Snapdragon 855+': '85',
        'Snapdragon 730G': '72',
        'Helio G90T': '84',
        'Exynos 9611': '80',
        'Apple A13 Bionic': '55',
        'Exynos 7884B': '64',
        'MT6580P': '25',
        'Kirin 990 5G': '66',
        'Kirin 990': '64',
        'Helio P70M': '79',
        'Dimensity 1000L': '79',
        'Exynos 980': '68',
        'Snapdragon 765G 5G': '72',
        'MT6765V': '52',
        'Snapdragon 215': '23',
        'Helio A20': '56',
        'Exynos 990': '92',
        'Helio P95': '52',
        'Helio G70': '69',
        'MT8765': '41',
        'Snapdragon 720G': '65',
        'Helio G80': '70',
        'Unisoc SC9832': '51',
        'Apple A12Z Bionic': '57',
        'Helio A25': '63',
        'Kirin 820 5G': '73',
        'Kirin 710A': '55',
        'Helio P22': '75',
        'Dimensity 800 5G': '75',
        'Kirin 985 5G': '71',
        'Helio G85': '71',
        'Snapdragon 865 5G+': '95',
        'Helio P60': '71',
        'MT8768': '55',
        'Snapdragon 768G 5G': '79',
        'Apple A14 Bionic': '73',
        'Exynos 850': '70',
        'Exynos 980, QRNG security chipset': '68',
        'MediaTek MT8168': '41',
        'Snapdragon 678': '68',
        'Dimensity 1000+': '90',
        'Exynos 880': '68',
        'Dimensity 820 5G': '74',
        'Helio G35': '67',
        'Helio G25': '65',
        'Snapdragon 765 5G': '61',
        'Dimensity 720 5G': '62',
        'Snapdragon 460': '52',
        'Snapdragon 662': '60',
        'Dimensity 800U 5G': '75',
        'Snapdragon 750 5G': '77',
        'Snapdragon 732G': '66',
        'Helio G95': '77',
        'MT6762V': '52',
        'Snapdragon 690 5G': '80',
        'Snapdragon 750G 5G': '77',
        'MT6761WE': '72',
        'Kirin 9000 5G': '72',
        'Unisoc UMS9117': '22',
        'Kirin 9000E 5G': '74',
        'Kirin 990E 5G': '66',
        'Exynos 2100': '93',
        'Unisoc UMS512T ': '31',
        'Snapdragon 888 5G': '92',
        'Exynos 1080': '88',
        'Snapdragon 480 5G': '66',
        'MT8768E': '55',
        'Dimensity 700 5G': '73',
        'Snapdragon 870 5G': '98',
        'MT6739W': '48',
        'Helio P22T': '75',
        # '7': '111',
    }

    d['chipset_score'] = a_num(tabla_chips.get(chip))

    # brand name
    brandid = d['brand_id']

    tabla_brands = {
        '92': 'Gionee',
        '4': 'Samsung',
        '6': 'Motorola',
        '66': 'BLU',
        '85': 'XOLO',
        '94': 'Lava',
        '1': 'Nokia',
        '108': 'LeEco',
        '106': 'Google',
        '44': 'HTC',
        '80': 'Xiaomi',
        '35': 'BlackBerry',
        '2': 'Alcatel',
        '103': 'QMobile',
        '69': 'Verykool',
        '104': 'Coolpad',
        '65': 'Micromax',
        '74': 'Lenovo',
        '45': 'Asus',
        '89': 'Allview',
        '107': 'BQ',
        '53': 'Vodafone',
        '72': 'Honor',
        '82': 'Oppo',
        '62': 'ZTE',
        '73': 'Meizu',
        '9': 'Panasonic',
        '57': 'Huawei',
        '19': 'LG',
        '71': 'Plum',
        '22': 'Sharp',
        '87': 'Maxwest',
        '95': 'OnePlus',
        '98': 'Vivo',
        '79': 'Yezz',
        '101': 'Posh',
        '96': 'Wiko',
        '91': 'Archos',
        '47': 'Apple',
        '10': 'Sony',
        '100': 'YU',
        '99': 'Yota',
        '68': 'Icemobile',
        '76': 'Amazon',
        '51': 'TMobile',
        '88': 'Cat',
        '109': 'Razer',
        '105': 'Energizer',
        '110': 'Blackview',
        '32': 'Haier',
        '111': 'Ulefone',
        '54': 'Sonim',
        '112': 'Realme',
        '26': 'Palm',
        '16': 'Kyocera',
        '113': 'Infinix',
        '114': 'Tecno',
        '115': 'TCL',
        '70': 'Orange',
        '116': 'Fairphone',
        '64': 'Microsoft',
    }

    d['brand_name'] = tabla_brands.get(brandid)

    # device normed score
    dns = []
    dns.append(normalize(n_ram_arr, d['n_ram']))
    dns.append(normalize(n_storage_arr, d['n_storage']))
    dns.append(d['expansion']*10)
    dns.append(normalize(n_display_width_arr, d['n_display_width']))
    dns.append(normalize(n_display_height_arr, d['n_display_height']))
    dns.append(normalize(n_camera_pixels_arr, d['n_camera_pixels']))
    dns.append(normalize(n_video_pixels_arr, d['n_video_pixels']))
    if d['n_battery_size'] > 7000:
        dns.append(100)
    else:
        dns.append(normalize(n_battery_size_arr, d['n_battery_size']))

    dns.append(normalize(n_display_size_arr, d['n_display_size']))
    dns.append(normalize(chipset_score_arr, d['chipset_score']))

    d['device_score'] = sum(dns)

    if d['device_score'] < 100:
        d['me_gusta'] = (a_num(str(d['device_score'])[0:1]))
    else:
        d['me_gusta'] = (a_num(str(d['device_score'])[0:2]))
    # print(d['me_gusta'])

    d['os'] = d['os'].split()[0]

    lista.append(d['device_score'])
    lista = list(dict.fromkeys(lista))

    #print(d['name'], d['device_score'])

lista.sort()
print(lista)


# print(data)


def save():
    with open('out.json', 'w') as jsonfile:
        json.dump(data, jsonfile)


# save()
