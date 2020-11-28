import telnetlib


host='10.21.121.164'
port='2525'

# Команды
# Power (ka)
power_on = 'ka 00 01' # a 00 OK01x
power_off = 'ka 00 00' # a 00 OK00x
power_status = 'ka 00 ff' # Подтверждение:
# a 00 OK01x (On)
# a 00 OK00x (Off)

# Display Mode (kb)
one_picture = 'kb 00 00' # Подтверждение b 00 OK00x
two_pictures_left_right = 'kb 00 01' # Подтверждение b 00 OK01x
two_pictures_top_bottom = 'kb 00 02' # Подтверждение b 00 OK02x
two_pictures_pip = 'kb 00 03' # Подтверждение b 00 OK03x
four_pictures = 'kb 00 04' # Подтверждение b 00 OK04x
pictures_status = 'kb 00 ff' # Подтверждение:
# b 00 OK00x (1P)
# b 00 OK01x (2P_LR)
# b 00 OK02x (2P_TB)
# b 00 OK03x (2P_PIP)
# b 00 OK04x (4P)

# P1 Input selection (k1)
picture_one_dp = 'k1 00 01' # 1 00 OK01x (DP)
picture_one_hdmi1 = 'k1 00 02' # 1 00 OK02x (HDMI1)
picture_one_hdmi2 = 'k1 00 03' # 1 00 OK03x (HDMI2)
picture_one_hdmi3 = 'k1 00 04' # 1 00 OK04x (HDMI3)
picture_one_hdmi4 = 'k1 00 05' # 1 00 OK05x (HDMI4)
picture_one_status = 'k1 00 ff' # Подтверждение:
# 1 00 OK01x (DP)
# 1 00 OK02x (HDMI1) 
# 1 00 OK03x (HDMI2) 
# 1 00 OK04x (HDMI3) 
# 1 00 OK05x (HDMI4)

# P2 Input selection (k2)
picture_two_dp = 'k2 00 01' # 2 00 OK01x (DP)
picture_two_hdmi1 = 'k2 00 02' # 2 00 OK02x (HDMI1)
picture_two_hdmi2 = 'k2 00 03' # 2 00 OK03x (HDMI2)
picture_two_hdmi3 = 'k2 00 04' # 2 00 OK04x (HDMI3)
picture_two_hdmi4 = 'k2 00 05' # 2 00 OK05x (HDMI4)
picture_two_status = 'k2 00 ff' # Подтверждение:
# 2 00 OK01x (DP)
# 2 00 OK02x (HDMI1) 
# 2 00 OK03x (HDMI2) 
# 2 00 OK04x (HDMI3) 
# 2 00 OK05x (HDMI4)

# P3 Input selection (k3)
picture_three_dp = 'k3 00 01' # 3 00 OK01x (DP)
picture_three_hdmi1 = 'k3 00 02' # 3 00 OK02x (HDMI1)
picture_three_hdmi2 = 'k3 00 03' # 3 00 OK03x (HDMI2)
picture_three_hdmi3 = 'k3 00 04' # 3 00 OK04x (HDMI3)
picture_three_hdmi4 = 'k3 00 05' # 3 00 OK05x (HDMI4)
picture_three_status = 'k3 00 ff' # Подтверждение:
# 3 00 OK01x (DP)
# 3 00 OK02x (HDMI1) 
# 3 00 OK03x (HDMI2) 
# 3 00 OK04x (HDMI3) 
# 3 00 OK05x (HDMI4)

# P4 Input selection (k4)
picture_four_dp = 'k4 00 01' # 4 00 OK01x (DP)
picture_four_hdmi1 = 'k4 00 02' # 4 00 OK02x (HDMI1)
picture_four_hdmi2 = 'k4 00 03' # 4 00 OK03x (HDMI2)
picture_four_hdmi3 = 'k4 00 04' # 4 00 OK04x (HDMI3)
picture_four_hdmi4 = 'k4 00 05' # 4 00 OK05x (HDMI4)
picture_four_status = 'k4 00 ff' # Подтверждение:
# 4 00 OK01x (DP)
# 4 00 OK02x (HDMI1) 
# 4 00 OK03x (HDMI2) 
# 4 00 OK04x (HDMI3) 
# 4 00 OK05x (HDMI4)

# Audio selection (kc)
audio_display_mode_one_display = 'kc 00 01' # c 00 OK01x (P1)
audio_display_mode_two_display_picture_one = 'kc 00 01' # c 00 OK01x (P1)
audio_display_mode_two_display_picture_two = 'kc 00 02' # c 00 OK02x (P2)
audio_display_mode_four_display_picture_one = 'kc 00 01' # c 00 OK01x (P1)
audio_display_mode_four_display_picture_two = 'kc 00 02' # c 00 OK02x (P2)
audio_display_mode_four_display_picture_three = 'kc 00 03' # c 00 OK03x (P3)
audio_display_mode_four_display_picture_four = 'kc 00 04' # c 00 OK04x (P4)
audio_display_mode_status = 'kc 00 ff' # Подтверждение:
# c 00 OK01x (P1) 
# c 00 OK02x (P2) 
# c 00 OK03x (P3) 
# c 00 OK04x (P4)

# Screen Mute (kd) 
screen_mute_on = 'kd 00 01' # d 00 OK01x(Mute ON)
screen_mute_off = 'kd 00 00' # d 00 OK00x(Mute OFF)
screen_mute_status = 'Status' # Подтверждение:
# d 00 OK01x (Mute ON) 
# d 00 OK00x (Mute OFF)

# Audio Mute (ke)
audio_mute_on = 'ke 00 01' # e 00 OK01x (Mute ON)
audio_mute_off = 'ke 00 00' # e 00 OK00x (Mute OFF)
audio_mute_status = 'ke 00 ff' # Подтверждение:
# e 00 OK01x (Mute ON) 
# e 00 OK00x (Mute OFF)

# Audio Volume (kf)
volume_level = 20 # Указываем желаемый уровешь громкости от 0 до 100
volume_level_hex = str(hex(volume_level))[2:] # Тут мы преобразуем в hex
volume_control = 'kf 00 %s' % (volume_level_hex) # f 00 OK00x (Volume = 0, Min.)
volume_control_status = 'kf 00 ff' 
# f 00 OK2Fx (Volume = 47)

# Aspect Ratio (kg)
aspect_ratio_full = 'kg 00 00(CR)' # g 00 OK00x (Full)
aspect_ratio_16_9 = 'kg 00 01(CR)' # g 00 OK01x (16:9)
aspect_ratio_4_3 = 'kg 00 02(CR)' # g 00 OK02x (4:3)
aspect_ratio_5_4 = 'kg 00 03' # g 00 OK03x (5:4)
aspect_ratio_1_1 = 'kg 00 04' # g 00 OK04x (1:1)
aspect_ratio_status = 'kg 00 ff' # Подтверждение:
# g 00 OK00x (Full) 
# g 00 OK01x (16:9) 
# g 00 OK02x (4:3) 
# g 00 OK03x (5:4) 
# g 00 OK04x (1:1)

# Picture 
# BackLight (kh)
backlight_level = 4 # Указываем желаемый уровень яркости подсветки от 0 до 100
backlight_level_hex = str(hex(backlight_level))[2:] # Тут мы преобразуем в hex
if len(backlight_level_hex) == 1:
    backlight_control = 'kh 00 0%s' % (backlight_level_hex) # h 00 OK5Ax (BackLight = 90)
    # print('backlight_control -', backlight_control)
elif len(backlight_level_hex) == 2:
    backlight_control = 'kh 00 %s' % (backlight_level_hex) # h 00 OK5Ax (BackLight = 90)
    # print('backlight_control -', backlight_control)
backlight_control_status = 'kh 00 ff' # h 00 OK5Ax (BackLight = 90)

# Contrast (ki)
contrast_level = 50 # Указываем желаемый уровень контрасности от 0 до 100
contrast_level_hex = str(hex(contrast_level))[2:] # Тут мы преобразуем в hex
if len(contrast_level_hex) == 1:
    contrast_control = 'ki 00 0%s' % (contrast_level_hex) # i 00 OK32x (Contrast = 50)
    # print('contrast_control -', contrast_control)
elif len(contrast_level_hex) == 2:
    contrast_control = 'ki 00 %s' % (contrast_level_hex) # i 00 OK32x (Contrast = 50)
    # print('contrast_control -', contrast_control)
contrast_control_status = 'ki 00 ff' # i 00 OK32x (Contrast = 50)

# Brightness (kj)
brightness_level = 50 # Указываем желаемый уровень яркости от 0 до 100
brightness_level_hex = str(hex(brightness_level))[2:] # Тут мы преобразуем в hex
if len(brightness_level_hex) == 1:
    brightness_control = 'kj 00 0%s' % (brightness_level_hex) # j00 OK32x (Brightness = 50)
    # print('brightness_control -', brightness_control)
elif len(brightness_level_hex) == 2:
    brightness_control = 'kj 00 %s' % (brightness_level_hex) # j00 OK32x (Brightness = 50)
    # print('brightness_control -', brightness_control)
brightness_control_status = 'kj 00 ff' # j 00 OK32x (Contrast = 50)

# Sharpness (kk)
sharpness_level = 2 # Указываем желаемый уровень резкости от 0 до 4
sharpness_level_hex = str(hex(sharpness_level))[2:] # Тут мы преобразуем в hex
if len(sharpness_level_hex) == 1:
    sharpness_control = 'kk 00 0%s' % (sharpness_level_hex) # k 00 OK02x (Sharpness = 2)
    # print('sharpness_control -', sharpness_control)
elif len(sharpness_level_hex) == 2:
    sharpness_control = 'kk 00 %s' % (sharpness_level_hex) # k 00 OK02x (Sharpness = 2)
    # print('sharpness_control -', sharpness_control)
sharpness_control_status = 'kk 00 ff' # kk 00 OK02x (Sharpness = 2)

# Color
# Gamma (kl)
gamma_off = 'kl 00 00' # l 00 OK00x(Gamma=Off)
gamma_1_8 = 'kl 00 01' # l 00 OK01x(Gamma=1.8) 
gamma_2_0 = 'kl 00 02' # l 00 OK02x(Gamma=2.0)
gamma_2_1 = 'kl 00 03' # l 00 OK03x(Gamma=2.1)
gamma_2_2 = 'kl 00 04' # l 00 OK04x(Gamma=2.2)
gamma_status = 'kl 00 ff' # l 00 OK00x(Gamma=Off)

# Temperature (km)
display_temperature_9300 = 'km 00 00' # m 00 OK00x (Temperature = 9300)
display_temperature_7500 = 'km 00 01' # m 00 OK01x (Temperature = 7500)
display_temperature_6500 = 'km 00 02' # m 00 OK02x (Temperature = 6500)
display_temperature_5800 = 'km 00 03' # m 00 OK03x (Temperature = 5800)
display_temperature_sRGB = 'km 00 04' # m 00 OK04x (Temperature = sRGB)
display_temperature_status = 'km 00 ff' # m 00 OK02x (Temperature = 6500)

# Color Effect (kn)
color_effect_standart = 'kn 00 00' # n 00 OK00x (Effect = Standard)
color_effect_game = 'kn 00 01' # n 00 OK01x (Effect = Game)
color_effect_movie = 'kn 00 02' # n 00 OK02x (Effect = Movie)
color_effect_photo = 'kn 00 03' # n 00 OK03x (Effect = Photo)
color_effect_vivid = 'kn 00 04' # n 00 OK04x (Effect = Vivid)
color_effect_status = 'kn 00 ff' # n 00 OK00x (Effect = Standard)

# Local Key (mk) 
POWER_KEY = 'mk 00 00' # k 00 OK00x
MENU_KEY = 'mk 00 01' # k 00 OK01x
LEFT_KEY = 'mk 00 02' # k 00 OK02x
RIGHT_KEY = 'mk 00 03' # k 00 OK03x
DOWN_KEY = 'mk 00 04' # k 00 OK04x
UP_KEY = 'mk 00 05' # k 00 OK05x
SOURCE_KEY = 'mk 00 06' # k 00 OK06x

def send_command(command, host, port):
    print('Команда:', command)
    print('Хост:', host)
    print('Порт:', port)
    connect=telnetlib.Telnet(host, port)
    print('Connection ok')
    connect.write(b'%s\r' % (command.encode('utf-8')))
    print('Comand sended')
    print(connect.read_until('a 00 OK01x'.encode('utf-8'), timeout=1))
