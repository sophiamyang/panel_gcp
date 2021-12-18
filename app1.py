from bokeh.sampledata.autompg import autompg_clean as df
import hvplot.pandas
import panel as pn

bootstrap = pn.template.BootstrapTemplate(title='Example')
select_origin = pn.widgets.Select(
    options=["North America", "Asia", "Europe"], name="origin"
)
select_cyl = pn.widgets.IntSlider(name="cyl", start=4, end=8, step=1)


@pn.depends(select_origin, select_cyl)
def exp_plot(select_origin, select_cyl):
    return (
        df[(df.origin == select_origin) & (df.cyl == select_cyl)]
        .sort_values(by="mpg")
        .hvplot(x="mpg", y="hp")
    )

bootstrap.sidebar.append(select_origin)
bootstrap.sidebar.append(select_cyl)
bootstrap.main.append(exp_plot)

bootstrap.servable()
