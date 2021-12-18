from bokeh.sampledata.autompg import autompg_clean as df
import hvplot.pandas
import panel as pn

def exp_plot(origin, cylinders):
    return (
        df[(df.origin == origin) & (df.cyl == cylinders)]
        .sort_values(by="mpg")
        .hvplot(x="mpg", y="hp")
    )

continents = ["North America", "Asia", "Europe"]
origin = pn.widgets.Select(options=continents, name="Origin")
cylinders = pn.widgets.IntSlider(name="Cylinders", start=4, end=8, step=1)
template = pn.template.BootstrapTemplate(title="Example")

template.sidebar.append(origin)
template.sidebar.append(cylinders)
template.main.append(pn.bind(exp_plot, origin, cylinders))
template.servable()