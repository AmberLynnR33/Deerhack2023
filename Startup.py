from View import View
from Model import Model

if __name__ == '__main__':
    model = Model()
    view = View(model)

    model.view = view

    view.base_screen.mainloop()
