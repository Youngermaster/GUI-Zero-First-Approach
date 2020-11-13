from guizero import App, Text, PushButton, Picture

app = App(title="guizero")

intro = Text(app, text="Have a go with guizero and see what you can create.")
picture = Picture(app, image="test.gif")
ok = PushButton(app, text="Ok")

app.display()