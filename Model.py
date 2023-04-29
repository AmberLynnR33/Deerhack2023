from openpyxl import Workbook, load_workbook, worksheet


class Model:
    """
    a class to represent an excel file
    === public attributes ===
    wb: the current workbook
    ws: the current worksheet (for the accessed month and date)
    cat: a dictionary of catagories and the amount spent on each
    amount_made: the amount of money the user made
    goals: this user's goals for the current month
    """
    wb: Workbook
    ws: worksheet
    cat: dict
    amount_made: float
    goals: dict
    # view: View

    def __init__(self) -> None:
        """
        initialize a new workbook
        """
        self.wb = Workbook()
        self.ws = None  # empty workbook initially
        self.cat = {'essentials': 0, 'bills': 0, 'subscriptions': 0, 'edu': 0,
                    'luxuries': 0}
        # initially all 0, since the user has not inputted anything yet
        self.amount_made = 0  # initially the user makes no money
        self.goals = {'essentials': 0, 'bills': 0, 'subscriptions': 0, 'edu': 0,
                      'luxuries': 0}
        # initialize view
        self.view = None

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
        if file_name is not None:  # handle error
            self.wb = load_workbook(f'{file_name}.xlsx')  # each application is a sheet

    def save_file(self, file_name: str) -> None:
        """
        saves the file
        """
        self.wb.save(f'{file_name}.xlsx')  # save workbook

    # we need to access the worksheets according to the month,
    # or create a new one
    # this is where we will input data
    def page_exists(self, month: int, year: int) -> None:
        '''check if the worksheet with this month and year exists'''
        if f'{year},{month}' not in self.wb.sheetnames:
            self._new_page(month, year)
        else:
            # set current sheet to this found sheet
            for sheet in self.wb:
                if sheet.title == f'{year},{month}':
                    self.ws = sheet

    def _new_page(self, month: int, year: int) -> None:
        '''
        initializes a new page in the excel
        '''
        # set current sheet to this new sheet
        self.ws = self.wb.create_sheet(f'{year},{month}')
        # add the column into the sheet, each catagory is a row
        for cat in self.cat:
            self.ws.append([cat])
        self.amount_made = 0
        for cat in self.cat:  # reset the amount spent
            self.cat[cat] = 0
        for goal in self.goals:  # reset goals
            self.goals[goal] = 0

    # *** USER SETTINGS *** #
    def add_money_out(self, amount: float, catagory: str) -> None:
        """
        add the amount spent to this specific catagory
        """
        col_counter = 1  # counter for number of columns
        row_counter = 1  # counter for number of columns
        # accumulate for total cost
        self.cat[catagory] += amount
        if self.cat[catagory] > self.goals[catagory]:
            self.spent_too_much()
        # find the empty column for that row, and add the amount to it, test
        for row in self.ws.iter_rows():
            if self.ws.cell(row_counter, 1).value == catagory:  # found row
                for col in self.ws.iter_cols(min_col=2):
                    if (self.ws.cell(row_counter, col_counter+1)).value is None:
                        break
                    col_counter += 1  # count until we reach none
                self.ws.cell(row_counter, col_counter + 1, amount)
                break
            row_counter += 1

    def add_money_in(self, amount: float) -> None:
        """
        allows the user to add the amount of money they make
        """
        self.amount_made += amount
        # add it to the spreadsheet, as a new row if amount made doesnt exist
        # get the names of the rows
        names = []
        row_counter = 1
        col_counter = 1
        for row in self.ws.iter_rows():
            names.append(self.ws.cell(row_counter, 1).value)
            if self.ws.cell(row_counter, 1).value == 'Amount Made':
                for col in self.ws.iter_cols(min_col=2):
                    if (self.ws.cell(row_counter, col_counter+1)).value is None:
                        break
                    col_counter += 1
                self.ws.cell(row_counter, col_counter, amount)
                break
            row_counter += 1
        if 'Amount Made' not in names:
            self.ws.append(['Amount Made', amount])

    def add_goal(self, amount: float, catagory: str) -> None:
        """
        allows the user to add in a goal for a specific catagory
        """
        self.goals[catagory] = amount
        # want to add this goal as a row in the excel
        names = []
        row_counter = 1
        for row in self.ws.iter_rows():
            names.append(self.ws.cell(row_counter, 1).value)
            if self.ws.cell(row_counter, 1).value == f'{catagory} goal':  # goal
                # exists, just edit
                self._edit_goals(amount, catagory, row_counter)
                break
            row_counter += 1
        if f'{catagory} goal' not in names:  # add as a row
            self.ws.append([f'{catagory} goal', amount])

    def _edit_goals(self, amount: float, catagory: str, row: int) -> None:
        """
        allows the user to edit their goal for a specific catagory
        """
        self.ws.cell(row, 2, amount)

    def total_amount_earned(self) -> float:
        """
        returns the total amount of money this user earned
        """
        return self.amount_made

    def total_spent(self, catagory: str) -> float:
        """
        returns the total amount of money spent for the specific catagory
        """
        return self.cat[catagory]

    def spent_too_much(self) -> str:
        """
        return a message if the user spends too much
        """
        return "you spent too much money!"  # edit lol

    def get_goals(self) -> dict:
        """
        return a dictionary of this user's goals for each catagory
        """
        return self.goals
