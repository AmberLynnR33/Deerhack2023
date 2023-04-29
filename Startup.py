from View import View
from Model import Model

if __name__ == '__main__':
    model = Model()
    view = View()

    model.view = view
    view.model = model

    view.base_screen.mainloop()
