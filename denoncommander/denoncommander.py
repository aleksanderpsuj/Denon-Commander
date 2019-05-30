import denonavr
import os
import time
import config as CONFIG

# Setup connection
denon = denonavr.DenonAVR(CONFIG.CONNECTION.IP)


# define clear
def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')

    # for mac and linux
    else:
        os.system('clear')


# Power Check Function
def power_check():
    if denon.power == 'ON':
        menu()
    if denon.power == 'OFF':
        print("::: Device is OFF")
        question_power = input("::: Turn device on? (Yes[y] No[n]): ").lower()
        if question_power in ['y', 'yes']:
            try:
                denon.power_on()
                print("::: Power is ON, going to menu...")
                time.sleep(2)
                menu()
            except:
                print("::: Error: I can't turn on device, please try manually")
        if question_power in ['n', 'no']:
            print("Exiting...")


def load_default():
    denon.update()
    denon.set_volume(int(CONFIG.DEFAULT.VOLUME))
    denon.set_input_func(CONFIG.DEFAULT.INPUT)
    denon.set_sound_mode(CONFIG.DEFAULT.SOUND_MODE)
    print("::: Default config loaded, going back to menu...")
    time.sleep(2)
    menu()


# Universal "Going Back" Function
def going_back_volume_control():
    print("Done! Going back...")
    time.sleep(1)
    clear()
    volume_control()


# Volume control feature
def volume_control():
    denon.update()
    current_volume = denon.volume
    muted = denon.muted
    sound_mode = denon.sound_mode
    print("::: Current Volume:", str(current_volume))
    print("::: Muted:", str(muted))
    print("::: Sound Mode:", str(sound_mode))
    print("\n::: 1 |=> Change Volume")
    print("::: 2 |=> Mute/Unmute")
    print("::: 3 |=> Sound Mode")
    print("::: 9 |=> Back to menu\n")
    question = input("::: Select point from menu: ")
    if question in ['1']:
        volume_inp = input("::: Change volume to [-80 - 18]: ")
        denon.set_volume(int(volume_inp))
        going_back_volume_control()
    if question in ['2']:
        mute = denon.muted
        if not mute:
            denon.mute(mute=True)
        if mute:
            denon.mute(mute=False)
        going_back_volume_control()
    if question in ['3']:
        sound_mode_list = denon.sound_mode_list
        print(sound_mode_list)
        mode_inp = input("::: Select mode from list above: ")
        denon.set_sound_mode(str(mode_inp))
        going_back_volume_control()
    elif question in ['9']:
        menu()
    else:
        print("Please select point from menu.")
        time.sleep(2)
        clear()
        volume_control()


# Universal "Going Back" Function
def going_back_track_control():
    print("Done! Going back...")
    time.sleep(1)
    clear()
    track_control()


# Track control feature
def track_control():
    denon.update()
    title = denon.title
    artist = denon.artist
    album = denon.album
    state = denon.state
    print("::: Title:", str(title))
    print("::: Artist:", str(artist))
    print("::: Album:", str(album))
    print("::: State:", str(state))
    print("\n::: 1 |=> Next Track")
    print("::: 2 |=> Previous Track")
    print("::: 3 |=> Play/Pause")
    print("::: 9 |=> Back to menu\n")
    question = input("::: Select point from menu: ")
    if question in ['1']:
        denon.next_track()
        going_back_track_control()
    elif question in ['2']:
        denon.previous_track()
        going_back_track_control()
    elif question in ['3']:
        denon.toggle_play_pause()
        going_back_track_control()
    elif question in ['9']:
        menu()
    else:
        print("Please select point from menu.")
        time.sleep(2)
        clear()
        track_control()


# Universal "Going Back" Function
def going_back_input_control():
    print("Done! Going back...")
    time.sleep(1)
    clear()
    input_control()


# Input control feature
def input_control():
    denon.update()
    current_input = denon.input_func
    print("::: Current Input:", str(current_input))
    print("\n::: 1 |=> Set Input")
    print("::: 9 |=> Back to menu\n")
    question = input("::: Select point from menu: ")
    if question in ['1']:
        print("Input List:", denon.input_func_list)
        question_input = input("Change input to: ")
        denon.set_input_func(str(question_input))
        going_back_input_control()
    elif question in ['9']:
        menu()
    else:
        print("Please select point from menu.")
        time.sleep(2)
        clear()
        input_control()


# Menu
def menu():
    clear()
    print(
        '____________________________\n'
        ':::', CONFIG.APP.APPLICATION, CONFIG.APP.VERSION, ':::\n'
        ':::   ', CONFIG.APP.AUTHOR, '  :::\n'
        '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯'
    )

    print("::: INFO :::")
    print("::: POWER: " + denon.power)
    print("::: NAME: " + denon.name)
    print("\n::: MENU :::")
    print("::: 1 |=> Volume Control")
    print("::: 2 |=> Track Control")
    print("::: 3 |=> Input Control")
    print("::: 8 |=> Load Default Config")
    print("::: 9 |=> Quit\n")
    question = input("::: Select point from menu: ")
    if question in ['1']:
        clear()
        volume_control()

    if question in ['2']:
        clear()
        track_control()

    if question in ['3']:
        clear()
        input_control()

    if question in ['8']:
        clear()
        load_default()
    # MENU END
    elif question in ['9']:
        exit(code="Exiting...")
    else:
        print("Please select point from menu.")
        time.sleep(2)
        clear()
        menu()


# MENU END


if __name__ == '__main__':
    power_check()
