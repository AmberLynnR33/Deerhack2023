from openpyxl import Workbook, load_workbook, worksheet
# open or create a new file
# if a file exists:
class Model:
    wb = Workbook()
    def new_file(self) -> None:
        """
        initializes a new file
        """
        self.wb = Workbook()

    # otherwise, create new workbook
    def open_file(self, file_name: str) -> None:
        """
        opens an existing file
        return None if the path is invalid
        """
        wb = load_workbook(file_name) # each application is a sheet

    ws = wb.active  # to view columns
    ws.title = 'Budgeting Data'
    def save_file(self) -> None:
        """
        saves the file
        """
        wb.save('path-name.xlsx')  # save workbook

    # we need to access the worksheets according to the month, or create a new one
    def page_exists(self, month: int, year: int) -> None:
        '''check if the worksheet with this month and year exists'''
        if f'{year}:{month}' not in self.wb.sheetnames:
            self._new_page(month, year)

    def _new_page(self, month: int, year: int) -> None:
        '''
        initializes a new page in the excel
        '''
        self.wb.create_sheet(f'{year}:{month}')  # check with amber
