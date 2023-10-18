def rom_to_int(number):
    rom_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
                'CM': 900, 'M': 1000}
    acum = 0
    while number:
        for rom in reversed(rom_dict):
            if rom in number[:len(rom)]:
                acum += rom_dict[rom]
                number = number[len(rom):]
                break
    return acum