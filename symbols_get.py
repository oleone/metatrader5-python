import account_info

def get_acoes(symbols):
    if symbols != None:
        for symbol in symbols:
            symbol_name = symbol.name
            symbol_description = symbol.description
            split = [*symbol_name]

            if (len(split) == 5 or (len(split) == 6 and ((split[4].isnumeric() and split[4] == '1') and (split[4].isnumeric() and split[5] == '1')))) and split[0].isalpha() and split[1].isalpha() and split[2].isalpha() and split[3].isalpha() and split[4].isnumeric():
                if "FII" not in symbol_description and "FI" not in symbol_description:
                    print(symbol_name, "-", symbol.description)

def get_fiis(symbols):
    if symbols != None:
        for symbol in symbols:
            symbol_name = symbol.name
            symbol_description = symbol.description
            symbol_name_split = [*symbol_name]

            if len(symbol_name_split) == 6 and symbol_name_split[4].isnumeric() and symbol_name_split[4] == '1' and symbol_name_split[4].isnumeric() and symbol_name_split[5] == '1' and symbol_name_split[0].isalpha() and symbol_name_split[1].isalpha() and symbol_name_split[2].isalpha() and symbol_name_split[3].isalpha() and symbol_name_split[4].isnumeric():
                if "FII" in symbol_description and "FI" in symbol_description:
                    print(symbol_name, "-", symbol_description)

def main():
    mt5 = account_info.init_meta_trader_4(3166686, "lp.12!@.LP", "XPMT5-PRD")
    symbols = mt5.symbols_get()

    get_acoes(symbols)
    # get_fiis(symbols)

if __name__ == "__main__":
    main()