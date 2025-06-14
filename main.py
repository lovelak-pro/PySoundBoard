from pygame import mixer
import os
import keyboard
from colorama import init, Fore, Style, Back

init(autoreset=True)

os.system('cls')
os.system('title PySoundBoard V-0.1.1')
os.system('mode con: cols=90 lines=30')
mixer.init()

sounds = [
    ('FBI Open UP', 'num 1', 'sfx\\fbi-open-up-sfx.mp3', (0, 0)),
    ('Anime Ahh', 'num 2', 'sfx\\anime-ahh.mp3', (1, 0)),
    ('Fart Moan', 'num 3', 'sfx\\fart-moan3.mp3', (2, 0)),
    ('Ara Ara', 'num 4', 'sfx\\ara-ara.mp3', (3, 0)),
    ('Emotional Damage', 'num 5', 'sfx\\emotional-damage-meme.mp3', (4, 0)),
    ('Ew Brother Ew', 'num 6', 'sfx\\eww-brother-eww.mp3', (5, 0)),
    ('Yes OMG Remix', 'num 7', 'sfx\\yes-omg-remix.mp3', (6, 0)),
    ('Yes Mommy', 'num 8', 'sfx\\yes_mommy.mp3', (7, 0)),
    ('Yes Daddy', 'num 9', 'sfx\\yes_daddy.mp3', (0, 1)),
    ('Thank you Anime', 'num 0', 'sfx\\thankyou_anime.mp3', (1, 1)),
    ('Yes Yes No No KSI', 'num 1+num 2', 'sfx\\yes-yes-yes-yes-no-no-no-no.mp3', (2, 1)),
    ('Yamate Kudasai', 'num 2+num 3', 'sfx\\yamate-kudasai.mp3', (3, 1)),
    ('Wee Wee Wee', 'num 4+num 5', 'sfx\\weeeee_original_1193597514938524841.mp3', (4, 1)),
    ('noob_', 'num 5+num 6', 'sfx\\noob sound.mp3', (5, 1)),
    ('Ta Ta Bye Bye', 'num 7+num 8', 'sfx\\byebye-indian.mp3', (6, 1)),
    ('The Rizz Sound', 'num 8+num 9', 'sfx\\the-weekend-rizz-extended.mp3', (7, 1)),
    ('Dog Laughing', 'num 1+num 4', 'sfx\\laughing-dog-meme.mp3', (0, 2)),
    ('Sad Violin', 'num 2+num 5', 'sfx\\worlds-smallest-violin.mp3', (1, 2)),
    ('What The Dog Doin', 'num 3+num 6', 'sfx\\what-the-dog-doin.mp3', (2, 2)),
    ('Snore Mimimi', 'num 4+num 7', 'sfx\\snore-mimimimimimi.mp3', (3, 2)),
    ('Meme Ending', 'num 5+num 8', 'sfx\\meme-de-creditos-finales.mp3', (4, 2)),
    ('Thank you my friend', 'num 6+num 9', 'sfx\\thank_you_my_friend.mp3', (5, 2)),
    ('Hub Intro', 'num /', 'sfx\\hub-intro-sound.mp3', (6, 2)),
    ('Im Sponge Bob', 'num *', 'sfx\\im-spongebob.mp3', (7, 2)),
    ('Limit On Talking', 'num /+num *', 'sfx\\limit-on-talking.mp3', (0, 3)),
    ('Sorry Indian', 'num +', 'sfx\\sorry-indian.mp3', (1, 3)),
    ('Spiderman Meme', 'num .', 'sfx\\spiderman-meme-song.mp3', (2, 3)),
    ('Run Meme', 'num -', 'sfx\\run-vine-sound-effect.mp3', (3, 3)),
    ('Gay Echo', 'num -+num *', 'sfx\\gay-echo.mp3', (4, 3)),
]


print(f''' {Fore.GREEN}    ______      _____                       _______                     _ 
     | ___ \\    /  ___|                     | | ___ \\                   | |
     | |_/ /   _\\ `--.  ___  _   _ _ __   __| | |_/ / ___   __ _ _ __ __| |
     |  __/ | | |`--. \\/ _ \\| | | | '_ \\ / _` | ___ \\/ _ \\ / _` | '__/ _` |
 {Fore.WHITE}    | |  | |_| /\\__/ / (_) | |_| | | | | (_| | |_/ / (_) | (_| | | | (_| |
     \\_|   \\__, \\____/ \\___/ \\__,_|_| |_|\\__,_\\____/ \\___/ \\__,_|_|  \\__,_|
            __/ |                                                          
           |___/                                                           

 {Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[0][1]} ) : {sounds[0][0]} \t\t\t{Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[15][1]} ) : {sounds[15][0]} {Back.RESET}
 {Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[1][1]} ) : {sounds[1][0]} \t\t\t{Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[16][1]} ) : {sounds[16][0]} {Back.RESET}
 {Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[2][1]} ) : {sounds[2][0]} \t\t\t{Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[17][1]} ) : {sounds[17][0]} {Back.RESET}
 {Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[3][1]} ) : {sounds[3][0]} \t\t\t\t{Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[18][1]} ) : {sounds[18][0]} {Back.RESET}
 {Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[4][1]} ) : {sounds[4][0]} \t\t{Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[19][1]} ) : {sounds[19][0]} {Back.RESET}
 {Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[5][1]} ) : {sounds[5][0]} \t\t\t{Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[20][1]} ) : {sounds[20][0]} {Back.RESET}
 {Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[6][1]} ) : {sounds[6][0]} \t\t\t{Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[21][1]} ) : {sounds[21][0]} {Back.RESET}
 {Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[7][1]} ) : {sounds[7][0]} \t\t\t{Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[22][1]} ) : {sounds[22][0]} {Back.RESET}
 {Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[8][1]} ) : {sounds[8][0]} \t\t\t{Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[23][1]} ) : {sounds[23][0]} {Back.RESET}
 {Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[9][1]} ) : {sounds[9][0]} \t\t\t{Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[24][1]} ) : {sounds[24][0]} {Back.RESET}
 {Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[10][1]} ) : {sounds[10][0]} \t\t{Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[25][1]} ) : {sounds[25][0]} {Back.RESET}
 {Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[11][1]} ) : {sounds[11][0]} \t\t{Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[26][1]} ) : {sounds[26][0]} {Back.RESET}
 {Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[12][1]} ) : {sounds[12][0]} \t\t{Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[27][1]} ) : {sounds[27][0]} {Back.RESET}
 {Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[13][1]} ) : {sounds[13][0]} \t\t\t{Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[28][1]} ) : {sounds[28][0]} {Back.RESET}
 {Back.CYAN}{Style.BRIGHT}Button > {Back.RED}{Style.BRIGHT} ( {sounds[14][1]} ) : {sounds[14][0]}

\n\n{Back.MAGENTA}{Style.BRIGHT} Use Ctrl + C to stop the program...
''')


paused = False

def toggle_pause():
    global paused
    paused = not paused
    if paused:
        print(f"{Fore.YELLOW}{Back.BLACK} [PAUSED] Soundboard is paused. Press F12 to resume.")
    else:
        print(f"{Fore.GREEN}{Back.BLACK} [RESUMED] Soundboard is active.")

def playSound(path):
    if not paused:
        mixer.music.load(path)
        mixer.music.play()

# ...existing code...

# Map numpad scan codes to numpad key names
numpad_scan_codes = {
    82: 'num 0',
    79: 'num 1',
    80: 'num 2',
    81: 'num 3',
    75: 'num 4',
    76: 'num 5',
    77: 'num 6',
    71: 'num 7',
    72: 'num 8',
    73: 'num 9',
    53: 'num /',
    55: 'num *',
    74: 'num -',
    78: 'num +',
    83: 'num .',
}

def event_to_numpad(event):
    # Only return a numpad key name if the scan code matches
    return numpad_scan_codes.get(event.scan_code, None)

def on_key_press(event):
    if paused:
        return
    key = event_to_numpad(event)
    if not key:
        return  # Ignore non-numpad keys
    for text in sounds:
        hotkey = text[1]
        # Single-key hotkey
        if '+' not in hotkey and key == hotkey:
            playSound(text[2])
        # Combo hotkey
        elif '+' in hotkey:
            combo = [k.strip() for k in hotkey.split('+')]
            if key in combo:
                try:
                    if all(keyboard.is_pressed(k) for k in combo):
                        playSound(text[2])
                except ValueError:
                    pass

# ...existing code...

keyboard.on_press(on_key_press)
keyboard.add_hotkey('F12', toggle_pause)

print(f"{Fore.CYAN}PySoundBoard loaded. Use numpad keys to play sounds. F12 to pause/resume.")
keyboard.wait()