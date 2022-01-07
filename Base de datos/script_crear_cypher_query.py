import json


with open('C:/Users/Usuario/Downloads/bbdd/out.json') as devices:
    data = json.load(devices)

file = open("myfile.txt", "w")
strg = ''

bateria = [600, 720, 750, 800, 860, 1000, 1020, 1150, 1200, 1300, 1350, 1400, 1470, 1500, 1530, 1550, 1600, 1700, 1750, 1800, 1821, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2210, 2227, 2250, 2280, 2300, 2350, 2400, 2410, 2450, 2460, 2500, 2510, 2540, 2600, 2620, 2630, 2650, 2658, 2670, 2700, 2716, 2730, 2750, 2760, 2770, 2800, 2815, 2850, 2860, 2870, 2880, 2900, 2915, 2920, 2942, 2950, 2965, 2970, 2980, 2990, 3000, 3010, 3020, 3030, 3040, 3046, 3050, 3060, 3070, 3075, 3080, 3090, 3100, 3110, 3120, 3130, 3140, 3150, 3160, 3174, 3180, 3200, 3210, 3225, 3230, 3240, 3250, 3260, 3300, 3315, 3320, 3330, 3340, 3350, 3360, 3400, 3410, 3420, 3425, 3430, 3450, 3500, 3520, 3540, 3550, 3570, 3580, 3600, 3630, 3650, 3687, 3700, 3750, 3760, 3765, 3800, 3820, 3850, 3885, 3900, 3930, 3940, 3969, 3990, 4000, 4010, 4015, 4020, 4025, 4030, 4035, 4040, 4045, 4050, 4060, 4065, 4070, 4080, 4085, 4100, 4115, 4130, 4132, 4160, 4180, 4200, 4220, 4230, 4235, 4250, 4260, 4300, 4310, 4315, 4350, 4380, 4400, 4500, 4510, 4520, 4550, 4600, 4680, 4700, 4720, 4729, 4780, 4800, 4820, 4900, 5000, 5020, 5080, 5100, 5160, 5200, 5260, 5300, 5500, 5580, 5800, 6000, 6020, 6180, 6500, 6600, 7000, 9000, 10000, 10300, 16000, 18000]


for x in bateria:
    strg += f"CREATE ({'bt_'+str(x)}:Capacidad_bateria{{capacidad:'{x}'}})\n"
    # print(strg)


brand_name = ['Alcatel', 'Allview', 'Apple', 'Archos', 'Asus', 'BLU', 'BQ', 'BlackBerry', 'Blackview', 'Cat', 'Coolpad', 'Energizer', 'Fairphone', 'Gionee', 'Google', 'HTC', 'Haier', 'Honor', 'Huawei', 'Infinix', 'Kyocera', 'LG', 'Lava', 'LeEco', 'Lenovo', 'Maxwest', 'Meizu', 'Micromax', 'Motorola', 'Nokia', 'OnePlus', 'Oppo', 'Orange', 'Palm', 'Panasonic', 'Plum', 'Posh', 'QMobile', 'Razer', 'Realme', 'Samsung', 'Sharp', 'Sonim', 'Sony', 'TMobile', 'TCL', 'Tecno', 'Ulefone', 'Verykool', 'Vivo', 'Vodafone', 'Wiko', 'XOLO', 'Xiaomi', 'YU', 'Yezz', 'Yota', 'ZTE']


for x in brand_name:
    strg += f"CREATE ({x}:brand_name{{brand_name:'{x}'}})\n"
    # print(strg)


expansion = ['expansion', 'no_expansion']

for x in expansion:
    strg += f"CREATE ({x}:expansion{{Has_expansion:'{x}'}})\n"
    # print(strg)


n_ram = [0, 1, 1.5, 2, 3, 4, 6, 8, 10, 12]

for x in n_ram:
    strg += f"CREATE ({'r_'+str(x).replace('.','_')}:n_ram{{n_ram:'{x}'}})\n"
    # print(strg)


n_camera_pixels = [0, 0.1, 0.2, 0.3, 1.3, 2, 3, 5, 8, 12, 13, 16, 19, 20, 21, 22, 23, 24, 25, 32, 40, 48, 50, 60, 64, 108]

for x in n_camera_pixels:
    strg += f"CREATE ({'ncp_'+str(x).replace('.','_')}:n_camera_pixels{{n_camera_pixels:'{x}'}})\n"
    # print(strg)


n_display_size = [1.77, 1.8, 2.2, 2.4, 2.8, 3.3, 3.8, 4.0, 4.5, 4.6, 4.7, 4.95, 5.0, 5.09, 5.1, 5.15, 5.2, 5.3, 5.34, 5.4, 5.45, 5.46, 5.5, 5.6, 5.65, 5.67, 5.7, 5.71, 5.72, 5.73, 5.8, 5.81, 5.83, 5.84, 5.85, 5.86, 5.88, 5.9, 5.93, 5.94, 5.95, 5.97, 5.98, 5.99, 6.0, 6.01, 6.09, 6.1, 6.15, 6.18, 6.19, 6.2, 6.21, 6.22, 6.23, 6.24, 6.26, 6.28, 6.3, 6.35, 6.36, 6.38, 6.39, 6.4, 6.41, 6.42, 6.43, 6.44, 6.45, 6.47, 6.49, 6.5, 6.51, 6.52, 6.53, 6.55, 6.56, 6.57, 6.58, 6.59, 6.6, 6.62, 6.63, 6.65, 6.67, 6.7, 6.72, 6.76, 6.78, 6.8, 6.81, 6.82, 6.85, 6.89, 6.9, 6.92, 6.95, 7.0, 7.09, 7.1, 7.12, 7.2, 7.3, 7.6, 8.0]

for x in n_display_size:
    strg += f"CREATE ({'nds_'+str(x).replace('.','_')}:n_display_size{{n_display_size:'{x}'}})\n"
    # print(strg)


os = ['Android', 'Feature', 'KaiOS', 'Microsoft', 'Tizen', 'iOS']

for x in os:
    strg += f"CREATE ({x}_os:os{{os:'{x}'}})\n"
    # print(strg)


aaa = ''

for d in data['RECORDS']:

    strg += f"CREATE ({'SP'+str(d['id'])}:SmartPhone{{id:'{d['id']}', brand_id:'{d['brand_id']}', name:'{d['name']}', picture:'{d['picture']}', released_at:'{d['released_at']}', body:'{d['body']}', os:'{d['os']}', storage:'{d['storage']}', display_size:'{d['display_size']}', display_resolution:'{d['display_resolution']}', camera_pixels:'{d['camera_pixels'].strip()}', video_pixels:'{d['video_pixels']}', ram:'{d['ram'].strip()}', chipset:'{d['chipset']}', battery_size:'{d['battery_size'].strip()}', battery_type:'{d['battery_type']}', specifications:'{d['specifications']}', deleted_at:'{d['deleted_at']}', created_at:'{d['created_at']}', updated_at:'{d['updated_at']}', n_ram:{d['n_ram']}, n_storage:{d['n_storage']}, expansion:'{d['expansion']}', n_display_width:{d['n_display_width']}, n_display_height:{d['n_display_height']}, n_camera_pixels:{d['n_camera_pixels']}, n_video_pixels:{d['n_video_pixels']}, n_battery_size:{d['n_battery_size']}, n_display_size:{d['n_display_size']}, chipset_score:{d['chipset_score']}, brand_name:'{d['brand_name']}', device_score:{str(round(d['device_score'],3))}, me_gusta:{d['me_gusta']}}})\n"

    strg += f"CREATE ({'SP'+str(d['id'])})-[:HAS_BRAND]->({d['brand_name']})\n"

    if d['expansion'] == 1:
        strg += f"CREATE ({'SP'+str(d['id'])})-[:HAS]->(expansion)\n"
    else:
        strg += f"CREATE ({'SP'+str(d['id'])})-[:HAS]->(no_expansion)\n"

    strg += f"CREATE ({'SP'+str(d['id'])})-[:HAS_RAM]->({'r_'+str(d['n_ram']).replace('.','_')})\n"

    strg += f"CREATE ({'SP'+str(d['id'])})-[:HAS_CAMERA_PIXELS]->({'ncp_'+str(d['n_camera_pixels']).replace('.','_')})\n"

    strg += f"CREATE ({'SP'+str(d['id'])})-[:HAS_BATTERY]->({'bt_'+str(d['n_battery_size'])})\n"

    strg += f"CREATE ({'SP'+str(d['id'])})-[:HAS_DISPLAY_SIZE]->({'nds_'+str(d['n_display_size']).replace('.','_')})\n"

    strg += f"CREATE ({'SP'+str(d['id'])})-[:HAS_OS]->({d['os']}_os)\n"

    aaa += "MATCH (n {id: '"+str(d['id'])+"'}) SET n.device_score = " + \
        str(round(d['device_score'], 2))+" WITH n "

    # break

aaa += "RETURN n.id"
# print(aaa)
print(strg)
file.write(strg)
file.close()


'''
[
  {uuid: 'foo1', props:{enabled: true}},
  {uuid: 'foo2', props:{example: 'foo'}},
  {uuid: 'foo3', props:{}}
]

UNWIND {data} AS d
MERGE (x {uuid: d.uuid})
SET x += d.props;

'''
