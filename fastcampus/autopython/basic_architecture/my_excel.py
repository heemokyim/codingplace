class Excel:
    excel_file=''

    def save_to_excel(self,list_data):
        for data in list_data:
            print('save ' + data + ' to '+self.excel_file)
