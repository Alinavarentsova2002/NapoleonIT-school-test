# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    roman_int.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mgrayson <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/16 16:55:20 by mgrayson          #+#    #+#              #
#    Updated: 2020/11/16 17:16:59 by mgrayson         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class solution:
    def romanToInt(self, s: str)(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val
