from logic import df

#template for formatting address: "123 N Maple St, Burbank, CA"
if __name__ == '__main__':
    dataframe = df()
    address = input('Enter your address/location: ')
    dataframe.get_geolocation(address)
    print(dataframe.get_odds())
