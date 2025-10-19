import menu

menu = menu.Menu()
menu.show_start_screen()


while menu.running:
    menu.new_game()
    menu.show_end_screen()