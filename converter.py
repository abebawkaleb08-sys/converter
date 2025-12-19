class Converter:


    def init(self, date, month, year):
        
        self.date = date
        self.month = month
        self.year = year


    def convert_to_eth(self):
        
        # december

        self.date -= 9
        self.month -=8
        self.year -= 7

        return f"{self.date}/{self.month}/{self.year}"
    def convert_to_ger(self):
        
         self.date += 9
         self.month +=8
         self.year += 7

         return f"{self.date}/{self.month}/{self.year}"

# decmber


converter = Converter(19, 12, 2025)

print(converter.convert_to_eth())