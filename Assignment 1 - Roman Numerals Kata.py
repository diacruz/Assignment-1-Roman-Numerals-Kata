{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww15860\viewh11860\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def roman_to_integer(roman):\
    roman_numerals = \{\
        'I': 1,\
        'V': 5,\
        'X': 10,\
        'L': 50,\
        'C': 100,\
        'D': 500,\
        'M': 1000\
    \}\
\
    result = 0\
    prev_value = 0\
\
    for numeral in reversed(roman):\
        value = roman_numerals.get(numeral, 0)\
\
        if value == 0:\
            print(f" Invalid Roman numeral")\
            return None\
\
        if value < prev_value:\
            result -= value\
        else:\
            result += value\
\
        prev_value = value\
\
    if result > 3000:\
        print("a number that is larger than 3000 cannot be converted.")\
        return None\
\
    return result\
    \
input = input("Enter a Roman numeral: ")\
result = roman_to_integer(input.upper())\
\
if result is not None:\
    print(f"The Roman numeral is equivalent to the digit: \{result\}")\
}